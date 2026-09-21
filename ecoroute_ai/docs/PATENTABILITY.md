# Preliminary Patentability and Prior-Art Note

## Scope

This document is a project-level novelty review, not a legal opinion, patentability opinion, freedom-to-operate opinion or filing recommendation.

## What is already crowded

Recent disclosures already cover AI-based waste classification from images, confidence thresholds, routing to waste streams, user correction and feedback loops, and multi-sensor waste classification. Those concepts should not be presented by themselves as the inventive contribution.

## Candidate technical contribution

EcoRoute AI centers on a different system boundary:

1. Detect an item using multimodal evidence.
2. Represent the item as a set of material-bearing components.
3. Estimate the state and contamination of each component.
4. Apply a policy-constrained routing graph to each component.
5. Withhold a consequential route when evidence uncertainty is high.
6. Ask a targeted clarification question that changes the routing state.
7. Export an auditable decision record and store user corrections for future calibration.

The strongest project-specific technical angle is therefore the transformation from an item-level classification into a component-level routing plan under uncertainty and local policy constraints.

## Preliminary prior-art observations

A 2026 U.S. patent describes an AI model for waste classification and includes a confidence threshold before initiating control signals for physical sorting. This means confidence-gated classification itself is not sufficient as a novelty position.

A 2025 U.S. application describes AI-based waste identification and user-driven new-classification or feedback workflows. Feedback-driven learning therefore should not be treated as the sole inventive point.

A published waste-sorting patent application describes combining multiple sensor signals and computational models and selecting categories from category probabilities. Generic sensor fusion and probabilistic categorization are also established.

A 2025 U.S. application describes a smart waste container that identifies discarded objects, estimates material categories and uses thresholds to route items to waste streams. Automated bin routing is consequently an established field.

## Filing-oriented next step

Before any patent filing, the component decomposition representation, the condition-specific component state, the policy graph, the uncertainty-triggered clarification mechanism and the resulting technical effect should be searched claim-by-claim against worldwide patent databases and non-patent literature. A patent professional should determine novelty, inventive step/non-obviousness, claim scope and filing strategy.

## Suggested invention title

Component-Aware Uncertainty-Gated Waste Routing System Using Multimodal Material Evidence and Policy-Constrained Decomposition
