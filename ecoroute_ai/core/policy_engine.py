from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
POLICY_PATH = BASE / "data" / "campus_policy.json"
POLICY = json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def _score_route(material, condition, candidate):
    route = POLICY["routes"].get(candidate, {})
    allowed = set(route.get("accepted_materials", []))
    value = 0.0
    if material in allowed:
        value += 0.65
    if condition in route.get("accepted_conditions", []):
        value += 0.25
    if condition in route.get("blocked_conditions", []):
        value -= 0.60
    value += route.get("priority", 0.0)
    return value


def route_component(component, material, condition, contamination):
    candidates = [
        name for name, rule in POLICY["routes"].items()
        if material in rule.get("accepted_materials", [])
        and name != "manual_review"
    ]
    if not candidates:
        route = "manual_review"
        rule = POLICY["routes"][route]
        return {
            "component": component,
            "route": route,
            "container": rule["container"],
            "action": rule.get("default_action", "Check local waste guidance before disposal"),
            "reason": rule["reason"],
        }

    scored = [(name, _score_route(material, condition, name)) for name in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    route = scored[0][0]
    rule = POLICY["routes"][route]
    action = rule.get("default_action", "Dispose according to campus policy")
    if contamination >= rule.get("contamination_threshold", 1.0):
        fallback = rule.get("contamination_route", route)
        if fallback not in POLICY["routes"]:
            fallback = "manual_review"
        route = fallback
        rule = POLICY["routes"][route]
        action = rule.get("contamination_action", rule.get("default_action", action))
    return {
        "component": component,
        "route": route,
        "container": rule["container"],
        "action": action,
        "reason": rule["reason"],
    }


def build_routing_plan(components, contamination):
    plan = []
    for component in components:
        plan.append(route_component(
            component["name"],
            component["material"],
            component.get("condition", "clean"),
            contamination
        ))
    return plan
