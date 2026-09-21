const pptxgen = require('pptxgenjs');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'EcoRoute AI';
pptx.subject = 'AI for Sustainability Virtual Internship';
pptx.title = 'EcoRoute AI';
pptx.company = 'Student Project';
pptx.lang = 'en-US';
pptx.theme = {
  headFontFace: 'Aptos Display',
  bodyFontFace: 'Aptos',
  lang: 'en-US'
};
pptx.defineSlideMaster({
  title: 'MASTER',
  background: { color: 'F6F8F4' },
  objects: [
    { rect: { x: 0, y: 0, w: 13.333, h: 0.18, fill: { color: '1F6B4F' }, line: { color: '1F6B4F' } } },
    { text: { text: 'EcoRoute AI', options: { x: 0.55, y: 7.15, w: 2, h: 0.2, fontSize: 9, color: '6A746F', margin: 0 } } },
    { text: { text: 'AI for Sustainability Virtual Internship', options: { x: 8.5, y: 7.15, w: 4.2, h: 0.2, fontSize: 9, color: '6A746F', align: 'right', margin: 0 } } }
  ],
  slideNumber: { x: 12.83, y: 7.15, color: '6A746F', fontSize: 9 }
});

function addTitle(slide, title, subtitle='') {
  slide.addText(title, { x: 0.65, y: 0.52, w: 12.0, h: 0.55, fontSize: 28, bold: true, color: '173A2F', margin: 0 });
  if (subtitle) slide.addText(subtitle, { x: 0.68, y: 1.13, w: 11.8, h: 0.36, fontSize: 13, color: '60736B', margin: 0 });
}
function addBox(slide, x, y, w, h, title, body, accent='1F6B4F') {
  slide.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.08, fill: { color: 'FFFFFF' }, line: { color: 'D5DDD8', width: 1.2 } });
  slide.addShape(pptx.ShapeType.rect, { x, y, w: 0.08, h, fill: { color: accent }, line: { color: accent } });
  slide.addText(title, { x: x+0.22, y: y+0.16, w: w-0.4, h: 0.32, fontSize: 16, bold: true, color: '173A2F', margin: 0 });
  slide.addText(body, { x: x+0.22, y: y+0.58, w: w-0.4, h: h-0.72, fontSize: 11.5, color: '44534D', margin: 0.02, breakLine: false, valign: 'top' });
}
function addArrow(slide, x, y, w, label='') {
  slide.addShape(pptx.ShapeType.chevron, { x, y, w, h: 0.45, fill: { color: '79A994' }, line: { color: '79A994' } });
  if (label) slide.addText(label, { x: x-0.1, y: y+0.49, w: w+0.2, h: 0.25, fontSize: 8.5, color: '6A746F', align: 'center', margin: 0 });
}

let slide = pptx.addSlide('MASTER');
slide.background = { color: 'EDF5F1' };
slide.addText('EcoRoute AI', { x: 0.8, y: 1.15, w: 7.2, h: 0.8, fontSize: 42, bold: true, color: '173A2F', margin: 0 });
slide.addText('Component-Aware Uncertainty-Gated Waste Routing System', { x: 0.83, y: 2.08, w: 8.4, h: 0.75, fontSize: 22, color: '1F6B4F', bold: true, margin: 0 });
slide.addText('AI + Sustainability project for practical campus waste segregation', { x: 0.85, y: 3.05, w: 6.7, h: 0.45, fontSize: 15, color: '4E625A', margin: 0 });
slide.addShape(pptx.ShapeType.roundRect, { x: 9.3, y: 1.15, w: 2.7, h: 2.7, fill: { color: 'FFFFFF' }, line: { color: 'C4D8CE', width: 1.5 } });
slide.addText('ONE ITEM', { x: 9.66, y: 1.48, w: 2.0, h: 0.32, fontSize: 13, bold: true, color: '6A746F', align: 'center', margin: 0 });
slide.addText('->', { x: 10.15, y: 1.94, w: 1.0, h: 0.4, fontSize: 24, bold: true, color: '1F6B4F', align: 'center', margin: 0 });
slide.addText('MATERIAL\nCOMPONENTS', { x: 9.56, y: 2.38, w: 2.1, h: 0.75, fontSize: 16, bold: true, color: '173A2F', align: 'center', margin: 0 });
slide.addText('->', { x: 10.15, y: 3.05, w: 1.0, h: 0.4, fontSize: 24, bold: true, color: '1F6B4F', align: 'center', margin: 0 });
slide.addText('ROUTES', { x: 9.66, y: 3.42, w: 2.0, h: 0.32, fontSize: 15, bold: true, color: '173A2F', align: 'center', margin: 0 });
slide.addText('Primary SDG: 12 - Responsible Consumption and Production', { x: 0.85, y: 4.25, w: 7.2, h: 0.38, fontSize: 14, bold: true, color: '173A2F', margin: 0 });
slide.addText('Name: ____________________   College: ____________________', { x: 0.85, y: 5.12, w: 7.5, h: 0.3, fontSize: 12, color: '53625D', margin: 0 });

slide = pptx.addSlide('MASTER');
addTitle(slide, '1. Problem', 'Why a single-bin answer is often too simple');
addBox(slide, 0.7, 1.75, 3.75, 3.55, 'The everyday problem', 'Students dispose of packaging, food containers, electronics and mixed-material products without knowing which parts belong in which stream. A one-label classifier can hide material combinations and contamination.');
addBox(slide, 4.78, 1.75, 3.75, 3.55, 'A practical example', 'A takeaway coffee cup can contain a fiber body, polymer lining, a plastic lid and liquid residue. Treating it as one object can send recoverable parts into the wrong stream.','6B8A7B');
addBox(slide, 8.86, 1.75, 3.75, 3.55, 'Project question', 'How might we use AI to identify the item, separate its material-bearing components conceptually and choose a safe local route for each component?','4B7D6A');

slide = pptx.addSlide('MASTER');
addTitle(slide, '2. Proposed solution', 'A decision pipeline rather than a single prediction');
const xs = [0.55, 2.72, 4.89, 7.06, 9.23, 11.4];
const titles = ['Input', 'Recognition', 'Condition', 'Decompose', 'Route', 'Audit'];
const bodies = ['Text + optional image', 'Multimodal evidence fusion', 'Clean / wet / contaminated / mixed', 'Material-bearing components', 'Policy-constrained routing', 'Decision record + correction'];
for (let i=0;i<xs.length;i++) addBox(slide, xs[i], 2.0, 1.75, 2.35, titles[i], bodies[i], i===4 ? 'C27738' : '1F6B4F');
for (let i=0;i<xs.length-1;i++) addArrow(slide, xs[i]+1.82, 2.95, 0.27);
slide.addText('Core technical addition: one detected object can produce several component-level routes, while uncertain cases are held for clarification instead of receiving an unconditional disposal command.', { x: 1.3, y: 5.1, w: 10.7, h: 0.85, fontSize: 17, bold: true, color: '173A2F', align: 'center', margin: 0.03 });

slide = pptx.addSlide('MASTER');
addTitle(slide, '3. What makes the project technically distinctive', 'The differentiation is in the decision mechanism');
addBox(slide, 0.7, 1.6, 5.75, 1.65, 'A. Component-aware representation', 'Instead of forcing the whole object into one class, the system builds a list of components, each with a material and condition.');
addBox(slide, 6.85, 1.6, 5.75, 1.65, 'B. Policy-constrained routing graph', 'The route is selected after the component state is known. Local rules are stored separately from the model so policy can change without retraining the vision model.','6B8A7B');
addBox(slide, 0.7, 3.6, 5.75, 1.65, 'C. Uncertainty-gated action', 'Confidence and normalized uncertainty are combined. A consequential route is withheld when the evidence is weak.','C27738');
addBox(slide, 6.85, 3.6, 5.75, 1.65, 'D. Targeted clarification', 'The system asks one high-information question chosen from the ambiguous states, then recomputes the route.','5D7E95');
addBox(slide, 3.8, 5.6, 5.75, 1.15, 'E. Local feedback loop', 'Corrections are stored as evaluation data without requiring a cloud account.','7A6F4F');

slide = pptx.addSlide('MASTER');
addTitle(slide, '4. Technical workflow', 'How the prototype computes the final routing plan');
const steps = [
  ['1', 'Evidence', 'Image embedding + text evidence'],
  ['2', 'Fusion', 'Weighted probability merge'],
  ['3', 'Condition', 'State and contamination score'],
  ['4', 'Decomposition', 'Component list for the detected object'],
  ['5', 'Policy graph', 'Accepted materials, blocked states, priorities'],
  ['6', 'Selective action', 'Clarify when uncertainty crosses threshold'],
  ['7', 'Output', 'Per-component container + reason + action']
];
let y = 1.55;
for (const [n,t,b] of steps) {
  slide.addShape(pptx.ShapeType.ellipse, { x: 0.75, y, w: 0.55, h: 0.55, fill: { color: '1F6B4F' }, line: { color: '1F6B4F' } });
  slide.addText(n, { x: 0.75, y: y+0.1, w: 0.55, h: 0.3, fontSize: 12, bold: true, color: 'FFFFFF', align: 'center', margin: 0 });
  slide.addText(t, { x: 1.55, y: y-0.02, w: 2.2, h: 0.3, fontSize: 15, bold: true, color: '173A2F', margin: 0 });
  slide.addText(b, { x: 3.7, y: y-0.02, w: 7.8, h: 0.3, fontSize: 12, color: '56665F', margin: 0 });
  y += 0.77;
}

slide = pptx.addSlide('MASTER');
addTitle(slide, '5. Prototype demonstration', 'Composite item example: takeaway coffee cup with lid and leftover drink');
addBox(slide, 0.7, 1.55, 3.3, 4.3, 'Observed item', 'Coffee cup with plastic lid and leftover drink\n\nPredicted item: Coffee cup with lid\nConfidence: 68.1%\n\nSelective routing: ON', '1F6B4F');
addArrow(slide, 4.2, 3.0, 0.65);
addBox(slide, 5.0, 1.45, 3.1, 1.35, 'Component 1', 'Cup body\nWet paper/fiber\n-> Residual waste bin', '6B8A7B');
addBox(slide, 5.0, 3.05, 3.1, 1.35, 'Component 2', 'Plastic lid\nClean PP\n-> Dry recycling bin', '6B8A7B');
addBox(slide, 5.0, 4.65, 3.1, 1.35, 'Component 3', 'Beverage residue\nOrganic + wet\n-> Organic waste bin', 'C27738');
addArrow(slide, 8.35, 3.0, 0.65);
addBox(slide, 9.1, 1.75, 3.55, 3.7, 'Why this matters', 'The system does not assume the whole object belongs in one bin. It turns the detected object into a component routing plan and exposes the reasoning behind every route.');

slide = pptx.addSlide('MASTER');
addTitle(slide, '6. Responsible AI', 'Built into the workflow, not added as a final paragraph');
addBox(slide, 0.75, 1.65, 2.85, 3.9, 'Fairness', 'Evaluate different packaging styles, lighting conditions, object orientations and language variations.','5D7E95');
addBox(slide, 3.95, 1.65, 2.85, 3.9, 'Transparency', 'Show top candidates, condition scores, route rules and reasons so users can inspect the decision.','6B8A7B');
addBox(slide, 7.15, 1.65, 2.85, 3.9, 'Privacy', 'The core workflow does not require identity data. Feedback is stored locally in the prototype.','7A6F4F');
addBox(slide, 10.35, 1.65, 2.25, 3.9, 'Safety', 'Hazardous items use a dedicated policy route. Uncertain high-impact cases are held for clarification.','C27738');
slide.addText('These principles directly match the internship guide: fairness, transparency, ethics and privacy are mandatory project considerations.', { x: 1.2, y: 6.0, w: 10.8, h: 0.45, fontSize: 13, bold: true, color: '173A2F', align: 'center', margin: 0 });

slide = pptx.addSlide('MASTER');
addTitle(slide, '7. Practical deployment', 'Designed for a campus first, then expandable');
addBox(slide, 0.75, 1.65, 3.65, 3.85, 'Phase 1: Campus pilot', 'Mobile or kiosk interface\nVerified campus policy file\nSmall local waste dataset\nFeedback by housekeeping team');
addBox(slide, 4.85, 1.65, 3.65, 3.85, 'Phase 2: Edge deployment', 'Camera at disposal station\nCompact vision model\nOffline inference\nQR or location-aware collection points','6B8A7B');
addBox(slide, 8.95, 1.65, 3.65, 3.85, 'Phase 3: Operations layer', 'Waste audit dashboard\nContamination trends\nRoute-level analytics\nModel calibration from verified corrections','C27738');

slide = pptx.addSlide('MASTER');
addTitle(slide, '8. Evaluation plan', 'Measure the technical system, not just the demo');
const metrics = [
  ['Item recognition', 'Accuracy, macro F1', 'How often is the object identified correctly?'],
  ['Component routing', 'Component-level accuracy', 'Are the individual materials sent to the intended stream?'],
  ['Contamination control', 'False recycling rate', 'How often does contaminated material enter dry recycling?'],
  ['Selective routing', 'Unsafe-route rate', 'How often does the system make a high-impact decision with weak evidence?'],
  ['Usability', 'Decision time', 'Can a student reach a usable route quickly?']
];
let my = 1.55;
for (const [m,k,d] of metrics) {
  slide.addShape(pptx.ShapeType.roundRect, { x: 0.75, y: my, w: 11.8, h: 0.85, fill: { color: 'FFFFFF' }, line: { color: 'D5DDD8', width: 1 } });
  slide.addText(m, { x: 1.0, y: my+0.18, w: 2.2, h: 0.27, fontSize: 13, bold: true, color: '173A2F', margin: 0 });
  slide.addText(k, { x: 3.4, y: my+0.18, w: 2.6, h: 0.27, fontSize: 12, color: '1F6B4F', bold: true, margin: 0 });
  slide.addText(d, { x: 6.1, y: my+0.18, w: 5.9, h: 0.27, fontSize: 11.2, color: '56665F', margin: 0 });
  my += 1.02;
}

slide = pptx.addSlide('MASTER');
addTitle(slide, '9. Patent-oriented technical position', 'The patent angle should be the mechanism, not “AI for waste”');
addBox(slide, 0.75, 1.55, 3.75, 4.3, 'Crowded elements', 'Image-based waste classification\nConfidence thresholds\nAutomatic bin routing\nUser correction / retraining\nMulti-sensor classification', 'C27738');
addBox(slide, 4.8, 1.55, 3.75, 4.3, 'Project-specific combination', 'Component-aware representation\nPer-component condition state\nPolicy-constrained routing graph\nUncertainty-triggered clarification\nAuditable component-level route plan','1F6B4F');
addBox(slide, 8.85, 1.55, 3.75, 4.3, 'What must be validated', 'Novelty over worldwide prior art\nInventive step / non-obviousness\nExact technical effect\nClaim scope\nFreedom to operate', '5D7E95');
slide.addText('Preliminary landscape review identified related disclosures. This project is not being presented as guaranteed patentable; a patent professional should complete a claim-level search before filing.', { x: 1.2, y: 6.05, w: 10.9, h: 0.5, fontSize: 11.5, color: '58665F', italic: true, align: 'center', margin: 0 });

slide = pptx.addSlide('MASTER');
addTitle(slide, '10. Internship alignment', 'Why the project satisfies the supplied guideline');
addBox(slide, 0.75, 1.55, 3.75, 4.55, 'Problem + SDG', 'Real campus sustainability problem\nPrimary SDG 12\nClear affected users\nMeasurable expected impact');
addBox(slide, 4.8, 1.55, 3.75, 4.55, 'AI + prototype', 'AI-based recognition\nCondition inference\nComponent decomposition\nDecision support\nPrompt/clarification workflow\nAudit output','6B8A7B');
addBox(slide, 8.85, 1.55, 3.75, 4.55, 'Responsible design', 'Fairness\nTransparency\nPrivacy\nSafety\nHuman override\nLocal policy verification','C27738');
slide.addText('Deliverables included in the project folder: runnable prototype, technical specification, project report, patent-oriented note, tests and evaluation script.', { x: 1.0, y: 6.35, w: 11.3, h: 0.35, fontSize: 12, bold: true, color: '173A2F', align: 'center', margin: 0 });

pptx.writeFile({ fileName: '/mnt/data/ecoroute_ai/EcoRoute_AI_Project.pptx' });
