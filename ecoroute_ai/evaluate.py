from core.engine import analyze_text

CASES = [
    ("plastic water bottle", "plastic bottle"),
    ("coffee cup with plastic lid and leftover drink", "coffee cup with lid"),
    ("banana peel", "banana peel"),
    ("phone charger", "phone charger"),
    ("AA battery", "battery"),
    ("glass bottle", "glass bottle"),
    ("paint can", "paint can"),
]

correct = 0
for text, expected in CASES:
    result = analyze_text(text)
    passed = result["item"] == expected
    correct += int(passed)
    print(f"{text}: predicted={result['item']} expected={expected} pass={passed}")

print(f"Text prototype accuracy={correct / len(CASES):.2%}")
