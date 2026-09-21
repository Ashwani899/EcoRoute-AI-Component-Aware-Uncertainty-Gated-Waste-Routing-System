OBJECT_COMPONENTS = {
    "plastic bottle": [
        {"name": "Bottle body", "material": "PET", "condition": "clean"},
        {"name": "Cap", "material": "PP", "condition": "clean"}
    ],
    "paper cup": [
        {"name": "Cup fiber body", "material": "paper", "condition": "clean"},
        {"name": "Polymer lining", "material": "polymer", "condition": "clean"},
        {"name": "Liquid residue", "material": "organic", "condition": "wet"}
    ],
    "juice carton": [
        {"name": "Fiber layer", "material": "paper", "condition": "clean"},
        {"name": "Polymer layer", "material": "polymer", "condition": "clean"},
        {"name": "Barrier layer", "material": "aluminum", "condition": "clean"}
    ],
    "snack packet": [
        {"name": "Flexible film", "material": "polymer", "condition": "clean"},
        {"name": "Metallized barrier", "material": "aluminum", "condition": "clean"},
        {"name": "Food residue", "material": "organic", "condition": "wet"}
    ],
    "coffee cup with lid": [
        {"name": "Cup body", "material": "paper", "condition": "wet"},
        {"name": "Plastic lid", "material": "PP", "condition": "clean"},
        {"name": "Beverage residue", "material": "organic", "condition": "wet"}
    ],
    "phone charger": [
        {"name": "Cable and plug", "material": "electronics", "condition": "clean"},
        {"name": "Metal contacts", "material": "metal", "condition": "clean"}
    ],
    "battery": [
        {"name": "Battery cell", "material": "battery", "condition": "clean"}
    ],
    "banana peel": [
        {"name": "Food peel", "material": "organic", "condition": "wet"}
    ],
    "glass bottle": [
        {"name": "Glass body", "material": "glass", "condition": "clean"}
    ],
    "used tissue": [
        {"name": "Tissue", "material": "sanitary", "condition": "used"}
    ],
    "paint can": [
        {"name": "Container", "material": "metal", "condition": "hazardous"},
        {"name": "Paint residue", "material": "hazardous", "condition": "hazardous"}
    ]
}


def decompose(item_label, condition):
    key = item_label.lower().strip()
    components = OBJECT_COMPONENTS.get(key)
    if components:
        result = []
        for item in components:
            row = dict(item)
            if condition in {"contaminated", "mixed"} and row["material"] not in {"organic", "hazardous", "battery", "electronics", "sanitary"}:
                row["condition"] = condition
            result.append(row)
        return result
    return [{"name": item_label, "material": item_label.lower(), "condition": condition}]
