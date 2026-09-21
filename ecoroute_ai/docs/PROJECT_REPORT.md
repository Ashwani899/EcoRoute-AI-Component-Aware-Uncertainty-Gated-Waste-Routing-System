# EcoRoute AI

## Title
Component-Aware Uncertainty-Gated Waste Routing System

## SDG alignment
Primary: SDG 12 - Responsible Consumption and Production.

## Problem statement
How might we use AI to determine the material and condition of a waste item, decompose multi-material items into separable components, and route each component through the correct campus waste stream so that segregation becomes more reliable and recoverable material is less likely to be contaminated?

## Affected users
Students, faculty, housekeeping teams, campus sustainability teams and waste collection partners.

## Current gap
Most disposal interfaces ask for one bin decision. That breaks down when an object contains multiple materials or when its recyclability changes because of residue or contamination.

## Proposed solution
EcoRoute AI accepts text and optionally an image. It fuses evidence, estimates condition and contamination, decomposes the detected item into material-bearing components, and sends every component through a policy-controlled routing layer.

The system can also refuse to make an unconditional route when uncertainty is high. It asks one targeted clarification question, then recomputes the route.

## Technical contribution
The core addition is component-level waste representation plus policy-constrained selective routing. The same physical item can therefore generate several disposal actions, while the system can defer a high-impact decision when evidence is weak.

## Prototype demonstration
Example: coffee cup with lid and leftover drink.

The system can represent the object as:

- paper/fiber cup body
- PP plastic lid
- organic liquid residue

It then maps each component to a route instead of sending the entire object to one bin.

## Responsible AI

Fairness: test across varied packaging styles, lighting and languages.

Transparency: expose candidate predictions, condition scores, route reason and policy source.

Privacy: avoid collecting identity data; store only what is needed for evaluation.

Safety: do not give hazardous-material instructions beyond the verified local policy layer; uncertain items should be held for review.

Human oversight: staff can override and record corrections.

## Expected impact

Better source separation, fewer contamination-causing decisions, clearer user guidance, and structured data for campus waste audits.

The prototype should be evaluated using item-level accuracy, component-level routing accuracy, false-recycling rate, clarification rate, unsafe-route rate and time per decision.
