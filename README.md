# EcoRoute AI

**Component-aware, uncertainty-gated waste-routing prototype** developed as an AI-for-sustainability project.

EcoRoute AI explores a practical limitation of single-label waste classification: one discarded object can contain several materials in different conditions. Rather than assigning the whole object to one bin, the prototype decomposes it into components, estimates contamination and uncertainty, and proposes a route for each component using a configurable policy file.

## Why it matters

A takeaway cup, for example, may contain a fiber body, a polymer lining, a plastic lid, and leftover liquid. A single “recyclable” label can hide important differences. EcoRoute AI models the item as a set of component-level decisions and can ask for clarification when the available evidence is uncertain.

## Prototype workflow

1. Accept a text description and optionally an image.
2. Recognize the item using the text path and optional image model.
3. Estimate item condition and contamination risk.
4. Decompose the object into material-bearing components.
5. Apply the configurable campus policy to each component.
6. Withhold a high-impact route when confidence is insufficient and request clarification.
7. Store local correction feedback and allow an audit record to be exported.

## Repository layout

```text
.
└── ecoroute_ai/
    ├── app.py                 # Streamlit application
    ├── evaluate.py            # Small, hand-selected text evaluation
    ├── core/
    │   ├── engine.py          # Analysis and multimodal orchestration
    │   ├── components.py      # Component decomposition
    │   ├── policy_engine.py   # Policy-constrained route selection
    │   ├── text_model.py      # Text analysis
    │   └── vision_model.py    # Optional image model
    ├── data/
    │   ├── campus_policy.json # Illustrative, configurable policy data
    │   └── examples.json
    └── docs/                  # Technical specification and project notes
```

## Run locally

From the repository root:

```bash
cd ecoroute_ai
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Text analysis does not require downloading the optional vision model. The image path uses a CLIP model that is downloaded on first use.

## Evaluation

From the `ecoroute_ai/` directory:

```bash
python -m pytest -q
python evaluate.py
```

The included evaluation script checks a small set of hand-selected text examples. Its output is a prototype diagnostic, **not** a representative benchmark or evidence of real-world waste-sorting accuracy.

## Technical notes

- The policy data is illustrative and should be replaced with verified local campus rules, collection contracts, and applicable regulations before deployment.
- Image recognition and text analysis can be uncertain; the application exposes confidence-related signals and a clarification path rather than treating every prediction as authoritative.
- Feedback is stored locally by the prototype. Review data retention and privacy requirements before deploying it for multiple users.
- The project is a decision-support prototype, not an operational waste-management service.

## Detailed documentation

- [Developer README and setup notes](ecoroute_ai/README.md)
- [Technical specification](ecoroute_ai/docs/TECHNICAL_SPEC.md)
- [Project report](ecoroute_ai/docs/PROJECT_REPORT.md)
- [Research sources](ecoroute_ai/docs/RESEARCH_SOURCES.md)
- [Invention disclosure notes](ecoroute_ai/docs/INVENTION_DISCLOSURE.md)

## Context

Built in the **AI for Sustainability Virtual Internship** programme with 1M1B, AICTE, and IBM SkillsBuild (remote; July–September 2026).

## License

No license file is currently included in this repository. Do not assume reuse, modification, or redistribution rights until a license is explicitly added.
