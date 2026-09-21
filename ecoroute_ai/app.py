import json
from pathlib import Path

import streamlit as st
from PIL import Image

from core.engine import analyze_multimodal, analyze_text, save_feedback
from core.vision_model import image_hash, predict_image

BASE = Path(__file__).resolve().parent

st.set_page_config(page_title="EcoRoute AI", page_icon="♻", layout="wide")

st.title("EcoRoute AI")
st.caption("Component-aware waste routing with uncertainty-gated decisions")

with st.sidebar:
    st.subheader("System settings")
    threshold = st.slider("Selective-routing confidence threshold", 0.40, 0.80, 0.58, 0.01)
    st.caption("Prototype policy data is illustrative. Replace it with verified campus rules before deployment.")
    st.caption("No personal data is required for the core workflow.")

col1, col2 = st.columns([1, 1])
with col1:
    item_text = st.text_input("Describe the item", placeholder="e.g. coffee cup with plastic lid and leftover drink")
with col2:
    image_file = st.file_uploader("Optional image", type=["jpg", "jpeg", "png", "webp"])

run = st.button("Analyze disposal path", use_container_width=True, type="primary")

if run:
    if not item_text.strip() and image_file is None:
        st.warning("Add a description or an image.")
    else:
        image = Image.open(image_file).convert("RGB") if image_file is not None else None
        with st.spinner("Analyzing material, condition, and component routes..."):
            if image is None:
                result = analyze_text(item_text)
                source = "text"
            else:
                image_result = predict_image(image)
                result = analyze_multimodal(item_text, image_result)
                result["image_hash"] = image_hash(image)
                source = "multimodal"
        result["selective_routing"] = result["selective_routing"] or result["confidence"] < threshold
        st.session_state["result"] = result
        st.session_state["source"] = source

result = st.session_state.get("result")
if result:
    a, b, c, d = st.columns(4)
    a.metric("Detected item", result["item"].title())
    b.metric("Confidence", f"{result['confidence'] * 100:.1f}%")
    c.metric("Contamination risk", f"{result['contamination_risk'] * 100:.1f}%")
    d.metric("Uncertainty", f"{result['uncertainty'] * 100:.1f}%")

    if result["selective_routing"]:
        st.warning("The system is withholding a high-impact disposal decision because the evidence is uncertain.")
        st.write(result["clarification_question"])
        answer = st.radio("Clarification", ["Yes", "No", "Not sure"], horizontal=True)
        if st.button("Apply clarification"):
            if answer == "Yes":
                result["contamination_risk"] = max(result["contamination_risk"], 0.75)
            elif answer == "No":
                result["contamination_risk"] = min(result["contamination_risk"], 0.15)
            result["selective_routing"] = False if answer != "Not sure" else True
            if not result["selective_routing"]:
                from core.policy_engine import build_routing_plan
                result["routing_plan"] = build_routing_plan(result["components"], result["contamination_risk"])
            st.session_state["result"] = result
            st.rerun()

    st.subheader("Component-level route")
    for row in result["routing_plan"]:
        with st.container(border=True):
            left, right = st.columns([1, 2])
            left.write(f"**{row['component']}**")
            left.write(f"Material route: {row['route'].replace('_', ' ').title()}")
            right.write(f"**Container:** {row['container']}")
            right.write(row["action"])
            st.caption(row["reason"])

    st.subheader("Model evidence")
    st.write("Top candidates")
    for label, score in result["top_candidates"]:
        st.progress(min(1.0, float(score)), text=f"{label.title()} - {score * 100:.1f}%")

    with st.expander("Condition evidence"):
        for label, score in result["condition_scores"]:
            st.write(f"{label.title()}: {score * 100:.1f}%")

    f1, f2 = st.columns(2)
    with f1:
        if st.button("Prediction was correct"):
            save_feedback(result["input"], result["item"], result["item"])
            st.success("Feedback stored locally.")
    with f2:
        correction = st.selectbox("Correct label", ["plastic bottle", "paper cup", "juice carton", "snack packet", "coffee cup with lid", "phone charger", "battery", "banana peel", "glass bottle", "used tissue", "paint can", "mixed waste"])
        if st.button("Save correction"):
            save_feedback(result["input"], result["item"], correction)
            st.success("Correction stored locally for future evaluation.")

    audit = dict(result)
    st.download_button("Download audit record", json.dumps(audit, indent=2), file_name="ecoroute_audit.json", mime="application/json")

st.divider()
st.markdown("**SDG 12:** Responsible Consumption and Production")
st.caption("Core technical idea: decompose a detected item into material-bearing components, estimate condition and contamination, then route each component through a local policy graph. High uncertainty triggers clarification instead of an unconditional disposal command.")
