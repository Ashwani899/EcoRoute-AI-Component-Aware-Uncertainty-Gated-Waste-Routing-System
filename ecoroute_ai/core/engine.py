from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import math

from .components import decompose
from .policy_engine import build_routing_plan
from .text_model import predict_from_text

BASE = Path(__file__).resolve().parents[1]
FEEDBACK_PATH = BASE / "data" / "feedback.json"


def _entropy(top):
    if not top:
        return 1.0
    values = [max(1e-9, x[1]) for x in top]
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs) / math.log(max(2, len(probs)))


def _contamination(condition_probs):
    scores = dict(condition_probs)
    return min(1.0, scores.get("wet", 0) * 0.45 + scores.get("contaminated", 0) * 0.65 + scores.get("mixed", 0) * 0.75)


def _question(top):
    labels = {x[0] for x in top[:2]}
    if "paper cup" in labels or "coffee cup with lid" in labels:
        return "Is there visible liquid or food residue inside the item?"
    if "plastic bottle" in labels or "juice carton" in labels:
        return "Is the container mostly empty and free of visible food or liquid residue?"
    if "battery" in labels or "phone charger" in labels:
        return "Does the item contain or belong to an electrical or battery-powered device?"
    if "mixed waste" in labels:
        return "Is the item made from more than one material that cannot be separated by hand?"
    return "Is the item clean and dry, with no visible hazardous or biological residue?"


def _load_feedback():
    if not FEEDBACK_PATH.exists():
        return []
    return json.loads(FEEDBACK_PATH.read_text(encoding="utf-8"))


def save_feedback(item_text, predicted, corrected):
    rows = _load_feedback()
    rows.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "item_text": item_text,
        "predicted": predicted,
        "corrected": corrected
    })
    FEEDBACK_PATH.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def analyze_text(item_text):
    if not isinstance(item_text, str) or not item_text.strip():
        raise ValueError("Provide a non-empty item description.")
    label, confidence, top = predict_from_text(item_text)
    if not label or not top:
        raise ValueError("The item description could not be classified.")
    condition = "clean"
    text = item_text.lower()
    if any(x in text for x in ["dirty", "greasy", "food residue", "with food", "used"]):
        condition = "contaminated"
    elif any(x in text for x in ["wet", "liquid", "leftover"]):
        condition = "wet"
    components = decompose(label, condition)
    contamination = 0.75 if condition == "contaminated" else 0.45 if condition == "wet" else 0.10
    entropy = _entropy(top)
    return _result(item_text, label, confidence, top, [(condition, 1.0)], components, contamination, entropy)


def analyze_multimodal(item_text, image_result):
    image_label, image_confidence, image_top, condition_probs = image_result
    text_label, text_confidence, text_top = predict_from_text(item_text)
    image_weight = 0.68 if image_confidence >= 0.55 else 0.45
    text_weight = 1.0 - image_weight
    merged = {}
    for label, score in image_top:
        merged[label] = merged.get(label, 0.0) + score * image_weight
    for label, score in text_top:
        merged[label] = merged.get(label, 0.0) + score * text_weight
    ranked = sorted(merged.items(), key=lambda x: x[1], reverse=True)[:4]
    if not ranked:
        raise ValueError("The image and text inputs did not produce a classification.")
    label = ranked[0][0]
    confidence = ranked[0][1] / max(1e-9, sum(x[1] for x in ranked))
    condition = max(condition_probs, key=lambda x: x[1]) if condition_probs else "clean"
    contamination = _contamination(condition_probs)
    entropy = _entropy(ranked)
    components = decompose(label, condition)
    return _result(item_text, label, confidence, ranked, condition_probs, components, contamination, entropy)


def _result(item_text, label, confidence, top, condition_probs, components, contamination, entropy):
    routing = build_routing_plan(components, contamination)
    selective = confidence < 0.58 or entropy > 0.55
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": item_text,
        "item": label,
        "confidence": confidence,
        "top_candidates": top,
        "condition": condition_probs[0][0] if condition_probs else "clean",
        "condition_scores": condition_probs,
        "contamination_risk": contamination,
        "uncertainty": entropy,
        "selective_routing": selective,
        "clarification_question": _question(top) if selective else None,
        "components": components,
        "routing_plan": routing,
        "feedback_count": len(_load_feedback())
    }
