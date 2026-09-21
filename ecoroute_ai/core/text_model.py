from pathlib import Path
import json
import re
import math

BASE = Path(__file__).resolve().parents[1]
DATA = json.loads((BASE / "data" / "examples.json").read_text(encoding="utf-8"))
LABELS = list(DATA.keys())


def _tokens(text):
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def predict_from_text(text):
    tokens = _tokens(text)
    if not tokens:
        return None, 0.0, []
    scores = []
    for label, examples in DATA.items():
        label_tokens = set()
        for example in examples:
            label_tokens.update(_tokens(example))
        overlap = len(tokens & label_tokens)
        phrase_bonus = sum(1 for example in examples if example in text.lower())
        score = overlap + phrase_bonus * 2.0
        scores.append((label, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    raw = [max(0.01, s) for _, s in scores]
    exp_values = [math.exp(min(v, 12.0)) for v in raw]
    total = sum(exp_values)
    probs = [(label, value / total) for (label, _), value in zip(scores, exp_values)]
    return probs[0][0], probs[0][1], probs[:4]
