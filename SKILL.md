---
name: yitong-ppt
description: "Create academic and project presentations with evidence-led visual storytelling. Use for 学术汇报, 组会, 论文分享, 答辩, 项目汇报, 领导汇报, 整页图片视觉稿, or editable PPTX. Supports complete-slide image drafts, image-first editable reconstruction, and direct editing of existing decks."
---

# 异瞳PPT

Use two views: check what supports the claim, then what the audience will understand. Turn the current task's material into concrete visual explanations: the problem, what was done, the evidence, and its meaning. A polished slide must communicate more than a row of boxes or a paragraph of technical names.

## Select content and output

- **Academic report**: papers, tutorials, group meetings, defenses, and research talks. Read [academic-report.md](references/academic-report.md).
- **Project report**: progress, leadership/client updates, engineering reviews, and proposals. Read [project-report.md](references/project-report.md).
- For mixed reports, follow the primary audience; borrow only useful page types from the other route.

Read [design-system.md](references/design-system.md) for new or substantially redesigned pages. For dense technical storytelling, football-style reports, or learning from a reference deck, also read [visual-storytelling.md](references/visual-storytelling.md).

Choose the output from the user's request, without asking them to select a production mode unnecessarily:

| User intent | Production path | Deliverable |
| --- | --- | --- |
| 整页图片稿、先看视觉效果、图片式PPT | Generate complete slides with [image-first-workflow.md](references/image-first-workflow.md). Stop at images when that is the requested scope. | Ordered slide images and a contact sheet |
| 先图片后可编辑、原包风格、高质量科研汇报重设计 | Establish the whole-slide visual direction, then reconstruct it with [editable-delivery.md](references/editable-delivery.md). | Editable PPTX and previews; include drafts when requested |
| 更新现有PPT、沿用母版、快速修改 | Edit native slides directly; use whole-slide exploration only if it resolves a real design problem. | Editable PPTX and relevant previews |

An explicit request for complete-slide images applies to all requested pages, including tables or results. Do not silently substitute an outline, HTML screenshot, or isolated diagram for an image-generation request. When output is unspecified, preserve an existing approved deck; for a new dense technical deck, start with one representative whole-slide draft when image generation is available, then reuse its design language.

## Workflow

1. Read the current documents, figures, experiments, and existing deck. Separate measured results, interpretation, plans, and missing evidence. Do not inherit historical numbers from a style reference.
2. Infer audience and duration where possible. Plan the opening overview, the few main work packages, and the closing findings and next steps. Give every page one question, one main visual, and one supported answer.
3. Design the argument before the decoration. Show a real scene or failure, explain the operation in plain language, and place the matching evidence beside it. Use the page archetypes rather than converting the experiment log into slides.
4. For the image path, supply actual style references and current content assets to the image tool and generate a complete 16:9 page. Follow the per-page content contract and prompt in [image-first-workflow.md](references/image-first-workflow.md). Keep the chosen typography, frame language, and density consistent across pages.
5. Inspect the draft for factual and visual defects. Correct those defects; do not run repeated cosmetic variants once the page communicates clearly. Continue through the requested scope without routine approval stops.
6. For editable delivery, rebuild native text, diagrams, charts, and tables without flattening the whole page or degrading the approved visual composition. Preserve real photos and source figures. Follow [editable-delivery.md](references/editable-delivery.md).
7. Inspect the actual deliverable. For PPTX, render the affected pages; for image delivery, inspect every final image. Verify readability, crops, relationships, numbers, and comparison scope.

## Communication and evidence

- Write formal, understandable slide text. Translate implementation names into what the method does; explain a necessary technical term at its first use.
- Show the strongest relevant comparison and the unresolved problem. Keep variant histories, tensor dimensions, run IDs, and repetitive caveats in notes or an appendix unless the audience needs them.
- Keep essential scope beside the result: dataset/split, evaluation target, and tolerance when they change its meaning. Put full provenance in notes; do not make the slide a footnote wall.
- Never invent results, identities, timestamps, citations, heatmaps, completion status, or ownership. Generated visuals are illustrations, not measured evidence.
- Do not add staff assignments to a research presentation unless requested. Do not copy private reference decks or new unpublished results into the public skill repository.

## Tool and delivery boundaries

Use available image-generation and presentation tools; this skill supplies the production instructions, not a bundled image model. If a required tool is unavailable, state the limitation and offer the closest concrete deliverable without claiming generation or editability. Follow tool permissions and any required cost consent.

For image-only scope, complete checked images are a valid final delivery. For editable scope, image drafts are intermediate: deliver the PPTX with rendered previews and briefly identify raster regions or material evidence gaps. Do not stop at the draft when end-to-end delivery is authorized.
