from core.engine import analyze_text

examples = [
    "coffee cup with plastic lid and leftover drink",
    "clean plastic water bottle",
    "AA battery",
    "phone charger",
    "banana peel",
    "paint can"
]

for value in examples:
    result = analyze_text(value)
    print("Input:", value)
    print("Detected:", result["item"])
    print("Confidence:", f"{result['confidence'] * 100:.1f}%")
    print("Selective routing:", result["selective_routing"])
    for row in result["routing_plan"]:
        print(f"{row['component']} -> {row['container']}")
    print()
