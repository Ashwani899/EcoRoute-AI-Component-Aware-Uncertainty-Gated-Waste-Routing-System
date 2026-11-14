import pytest

from core.components import decompose
from core.engine import analyze_text
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


def test_unknown_material_requires_manual_review():
    plan = build_routing_plan(
        [{"name": "unknown composite", "material": "unlisted_composite", "condition": "clean"}],
        0.05,
    )
    assert plan[0]["route"] == "manual_review"
    assert "staff review" in plan[0]["container"].lower()
    assert "do not guess" in plan[0]["action"].lower()


def test_empty_text_is_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        analyze_text("   ")
