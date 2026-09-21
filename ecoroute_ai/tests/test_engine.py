from core.components import decompose
from core.policy_engine import build_routing_plan


def test_composite_item():
    components = decompose("coffee cup with lid", "wet")
    names = [x["name"] for x in components]
    assert "Cup body" in names
    assert "Plastic lid" in names
    assert len(components) == 3


def test_battery_route():
    components = decompose("battery", "clean")
    plan = build_routing_plan(components, 0.05)
    assert plan[0]["route"] == "battery"


def test_contamination_fallback():
    components = decompose("plastic bottle", "clean")
    plan = build_routing_plan(components, 0.85)
    assert plan[0]["route"] == "residual"
