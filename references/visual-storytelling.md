# Visual storytelling: lessons from football algorithm reports

The strength of the football examples is the connection between scene, operation, and evidence. Black frames and red text alone do not reproduce it. Reuse the visual reasoning below with the current task's own content; none of the example metrics, methods, or identities is a default.

## What the reference pages do well

| Page pattern | What the audience sees | Reusable construction |
| --- | --- | --- |
| Three-task overview | Identity tracking, local action, and match understanding form a progression | Three related columns, each containing an input scene, a concrete operation, and one output/result |
| Tracking method and verification | A person disappears, returns, and is associated with the same identity | A before/absence/after sequence above the evidence used for association; matched results beside a real output |
| Local-event diagnosis | Overall scores coexist with specific difficult classes | A compact main comparison above a class chart and two or three evidence-backed failure examples |
| Event recognition and clip output | What a correct detection, confusion, and miss actually look like | Real scene + corresponding person crop + short label on one side; event time → player → output clip on the other |
| Method adaptation and benefit | What was changed and whether it helped | A large horizontal input/operation/output mechanism above a smaller matched result comparison |
| Match-understanding prototype | A camera image becomes a structured representation | Original scene beside field map, identity/position/phase outputs, and the actual prototype status |
| Closing summary | What is established and what should be done next | One compact row per work package: achieved finding, remaining problem, next concrete step |

Use the existing public [overview](../assets/cases/football-overview.png), [diagnosis](../assets/cases/football-local-event-diagnosis.png), and [method/result](../assets/cases/football-player-attribution.png) images as visual examples. Their historical claims are not revalidated by this skill.

## Build explanatory visuals, not box diagrams

- **Scene → local crop**: the large scene establishes context; a visible rectangle and connector show which person or region was enlarged. Use the exact corresponding crop.
- **Sequence → change**: three to five real frames show the action or identity transition. Mark the moment or change that matters; the time axis must agree with the source.
- **Input → operation → observable output**: show what the model receives, what is changed, and what the output contains. Name each operation in a short verb phrase.
- **Output → structured fields**: show only supported fields such as action, time, person, or clip. Do not fabricate a player ID or confidence to make the interface look complete.
- **Mechanism → result**: use spatial alignment to connect the changed module to its measured effect. Do not imply a causal ablation if training budget, data, or evaluation also changed.

For a new mechanism, start with its real logic and enrich it with meaningful crops, feature views, or temporal strips only when they exist. A heatmap-like texture is not a feature visualization. Keep an illustrative mechanism visibly distinct from experimental output.

## Select a layout by the question

1. **What is the whole system doing?** Three parallel task columns, or one clear end-to-end route. Put a real input and output in each part; avoid a grid of abstract nouns.
2. **Why is this difficult?** Two or three genuine failure scenes with enlarged evidence and a one-line explanation.
3. **What did we change?** A dominant method region (roughly 55%–65% of the body), then a smaller result region. Separate method names from the plain-language operation.
4. **What works and what remains weak?** One main comparison, a compact diagnostic, and the concrete unresolved failure. Avoid an exhaustive run table.
5. **How does the output get used?** A short visual sequence from input through detection/association to the actual output artifact.

Do not require all five layouts in every deck. Combine related pages when the argument remains readable. Dense means more explanatory evidence, not smaller text or more boxes.

## Make the wording understandable

Prefer “先定位动作发生时刻，再确认参与球员，输出可回看的片段” to “实现多维语义协同与结构化读出”.

Prefer “同时看球员近景和整段比赛画面，判断谁在何时做了什么” to a list of token counts, readout heads, and backbone names for a general audience.

Prefer “远处球员裁剪后只有很少像素，腿部动作难以分辨” to “外域表征质量存在瓶颈”; show the real crop when that explanation is verified.

Use a concrete title, a short operation caption, and a result sentence only if it adds information. A strong bottom conclusion is useful on a dense evidence page; it is not mandatory on every slide. Remove narration such as “当前关键”“值得注意”“本页展示” and statements that merely restate the heading.

For a leadership audience, emphasize measures, results, and remaining difficulty. For a technical audience, retain the mechanism necessary to assess the claim. Never trade an essential evaluation condition for a cleaner-looking result.
