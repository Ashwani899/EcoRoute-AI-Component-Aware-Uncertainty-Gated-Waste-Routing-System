# Invention disclosure draft

## Working title
Component-Aware Uncertainty-Gated Waste Routing System Using Multimodal Material Evidence and Policy-Constrained Decomposition

## Technical problem
Conventional waste assistants typically map an observed item to a single category. Multi-material objects and condition-dependent recyclability make a single route insufficient. A system is needed that can convert one observed item into a structured set of separable material components and determine a route for each component while limiting unsafe decisions caused by uncertainty.

## Proposed architecture

Input layer -> multimodal evidence layer -> object state layer -> component decomposition layer -> policy graph -> uncertainty gate -> clarification loop -> component route plan -> audit and feedback layer

## Distinctive mechanism

The system maintains a component representation instead of only an item label. Each component can carry its own material and condition state. The policy graph operates on the component state, not only on the parent object.

The uncertainty gate evaluates the evidence before a route is surfaced as a final action. When uncertainty is high, the system selects a question that separates the most consequential candidate states. The answer updates the state and recomputes the routing graph.

## Example

A takeaway coffee cup is represented as cup body, polymer lining, lid and beverage residue. These components can have different material and condition states, producing different routes.

## Technical effect to measure

The prototype should be evaluated for lower false-recycling decisions, higher component-level routing accuracy and lower unsafe-route rate than a single-label baseline.

## Future implementation

A production system can replace zero-shot vision with an edge model trained on verified campus data, extract policy rules from signed documents, and connect route outputs to physical collection points or actuators.

## Patent caution

The wording above is a technical disclosure draft. It is not a legal claim set. Patentability depends on novelty, inventive step/non-obviousness, enablement and other jurisdiction-specific requirements. The preliminary search already found related systems for AI waste classification, confidence gating, feedback and sensor-fusion sorting, so a filing should focus on the exact component-state and routing mechanism and be preceded by a professional prior-art search.
