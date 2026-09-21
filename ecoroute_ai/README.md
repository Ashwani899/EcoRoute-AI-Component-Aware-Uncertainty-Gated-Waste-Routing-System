# EcoRoute AI

EcoRoute AI is a campus waste-disposal decision-support prototype built around a technical concept that goes beyond one-label waste classification.

## Problem

A waste item is often not a single material. A coffee cup may contain a fiber body, polymer lining, plastic lid and liquid residue. A single class such as "recyclable" can therefore produce a poor disposal instruction.

## Technical addition

EcoRoute AI creates a component-level waste representation and routes each component through a configurable policy graph.

The pipeline is:

1. Text and optional image input
2. Multimodal item recognition
3. Condition estimation
4. Contamination-risk estimation
5. Component decomposition
6. Policy-constrained routing per component
7. Uncertainty-gated clarification
8. Local correction logging and audit export

The key prototype idea is the combination of component decomposition and selective routing. The system can turn one detected object into multiple material-bearing actions instead of forcing a single bin decision.

## Example

Input: coffee cup with plastic lid and leftover drink

Output:

- Cup fiber body -> residual or verified fiber stream depending on local policy
- Plastic lid -> dry recycling
- Beverage residue -> organic stream

The exact route is controlled by `data/campus_policy.json` rather than hard-coded into the classifier.

## Run

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

For macOS/Linux, activate the virtual environment with `source .venv/bin/activate`.

Text analysis works without downloading the vision model. The optional image path downloads `openai/clip-vit-base-patch32` on first use.

## Test

```bash
python -m pytest -q
python evaluate.py
```

## Files

`app.py` - Streamlit interface
`core/engine.py` - multimodal fusion, uncertainty and feedback logic
`core/vision_model.py` - optional CLIP vision module
`core/components.py` - component decomposition rules
`core/policy_engine.py` - policy graph and route selection
`data/campus_policy.json` - configurable local policy layer
`data/examples.json` - lightweight text examples
`docs/PATENTABILITY.md` - preliminary novelty and prior-art notes
`docs/TECHNICAL_SPEC.md` - technical specification

## Important deployment note

The policy JSON is a prototype. A real deployment should replace it with verified campus rules, collection contracts and local regulatory requirements.
