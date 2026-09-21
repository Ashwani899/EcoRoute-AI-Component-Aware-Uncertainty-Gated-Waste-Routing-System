from __future__ import annotations

import hashlib
from PIL import Image

MODEL_NAME = "openai/clip-vit-base-patch32"
OBJECT_LABELS = [
    "a photo of a plastic bottle",
    "a photo of a paper cup",
    "a photo of a juice carton",
    "a photo of a snack packet",
    "a photo of a coffee cup with lid",
    "a photo of a phone charger",
    "a photo of a battery",
    "a photo of a banana peel",
    "a photo of a glass bottle",
    "a photo of a used tissue",
    "a photo of a paint can",
    "a photo of mixed waste"
]
OBJECT_KEYS = [
    "plastic bottle",
    "paper cup",
    "juice carton",
    "snack packet",
    "coffee cup with lid",
    "phone charger",
    "battery",
    "banana peel",
    "glass bottle",
    "used tissue",
    "paint can",
    "mixed waste"
]
CONDITION_LABELS = [
    "a clean dry waste item",
    "a wet waste item with liquid residue",
    "a food contaminated waste item",
    "a damaged or mixed waste item"
]
CONDITION_KEYS = ["clean", "wet", "contaminated", "mixed"]

_model = None
_processor = None


def image_hash(image: Image.Image):
    data = image.convert("RGB").tobytes()
    return hashlib.sha256(data).hexdigest()[:16]


def _load():
    global _model, _processor
    if _model is None:
        from transformers import CLIPModel, CLIPProcessor
        _processor = CLIPProcessor.from_pretrained(MODEL_NAME)
        _model = CLIPModel.from_pretrained(MODEL_NAME)
        _model.eval()
    return _model, _processor


def _rank(image, labels):
    import torch
    model, processor = _load()
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = outputs.logits_per_image.softmax(dim=1)[0]
    values = probs.tolist()
    order = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
    return [(i, float(values[i])) for i in order]


def predict_image(image: Image.Image):
    object_rank = _rank(image, OBJECT_LABELS)
    condition_rank = _rank(image, CONDITION_LABELS)
    object_results = [(OBJECT_KEYS[i], score) for i, score in object_rank[:4]]
    condition_results = [(CONDITION_KEYS[i], score) for i, score in condition_rank[:4]]
    return object_results[0][0], object_results[0][1], object_results, condition_results
