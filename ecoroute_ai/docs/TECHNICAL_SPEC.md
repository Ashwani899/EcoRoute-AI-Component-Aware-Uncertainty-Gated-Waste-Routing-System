# EcoRoute AI Technical Specification

## 1. System objective

Convert an uncertain waste observation into a safe, component-level disposal plan rather than a single categorical bin prediction.

## 2. Input layer

The prototype accepts a text description and optionally an RGB image. The text path is a lightweight retrieval-style classifier. The image path uses CLIP zero-shot image-text similarity.

## 3. Evidence fusion

For a multimodal request, object probabilities from the image model and text probabilities from the local text model are normalized and combined. The image contribution is increased when its top-class confidence is above a minimum reliability threshold.

## 4. Condition model

The vision branch scores condition prompts such as clean, wet, food-contaminated and mixed. A contamination score is derived from those condition probabilities.

## 5. Component decomposition

The item label is mapped to zero or more material-bearing components. Composite examples are represented as separate components. Each component has a material and condition state.

## 6. Policy graph

Each component is evaluated against a configurable route graph. Route scores use accepted materials, accepted conditions, blocked conditions and route priority. Contamination can force a component onto a fallback route.

## 7. Selective routing

The system computes normalized entropy over the leading candidate probabilities. If confidence is low or uncertainty is high, it does not present the route as unconditional. Instead it produces one clarification question chosen to separate the most consequential states.

## 8. Feedback memory

User confirmations and corrections are appended to a local JSON log. The log is designed as a future calibration and retraining dataset while retaining the prototype's core operation without a cloud account.

## 9. Auditability

Each analysis can be exported as a JSON record containing source, prediction, confidence, condition scores, contamination score, components and route decisions.

## 10. Deployment path

A production build could replace the zero-shot model with a campus-trained edge model, replace the example policy JSON with signed policy documents, connect validated collection-point locations and add an edge camera or mobile interface.
