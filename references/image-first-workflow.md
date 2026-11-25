# Whole-slide image workflow

Produce the full composition in one image-generation call per page: title, visual explanation, evidence, and a supported takeaway where useful. This is not a request for disconnected illustrations. It works for one page or a whole deck, and can end at images or continue to editable PowerPoint.

## 1. Establish a page contract

Use a compact planning record; do not add a planning slide to the deck:

- **Audience and question**: what must the reader understand from this page?
- **Exact text**: short title, module headings, essential labels, and one evidence-based result sentence. Separate exact visible text from instructions to the image model.
- **Supported content**: the actual operation, inputs, outputs, measured comparison, conditions, and limitations.
- **Assets**: current real scenes, crops, sequences, paper figures, and data-rendered charts; identify each asset's role.
- **Layout**: choose an archetype from [visual-storytelling.md](visual-storytelling.md), the reading direction, and the region that should dominate.
- **Missing evidence**: omit the affected claim or use an explicitly illustrative region; do not let the model fill gaps with plausible facts.

First inspect the supplied reference pages visually. A text extraction cannot establish their composition. Inspect local images before passing them to image tools. Attach an appropriate style page and the necessary current assets, using the tool's supported reference mechanism. A path written inside the prompt is not an attached image.

Distinguish **STYLE REFERENCE** from **CONTENT SOURCE**. The first supplies layout and visual language; only the second supplies task facts. Existing repository case images are historical style examples, not proof of new results.

## 2. Generate the complete slide

Use this prompt as a starting point, replacing every bracketed field and removing unused modules:

```text
生成一张完整的16:9中文科研／项目汇报幻灯片，包含标题、主体内容和必要的结论。
不是海报、网页或若干独立素材。面向[听众]，本页要回答：[具体问题]。

风格参考：[已附参考页及用途]。只学习其构图、分区、字体层级和视觉密度。
内容素材：[已附真实画面／人物裁剪／连续帧／论文图／数据图及各自用途]。

页面标题（原样使用）：[标题]
实际问题：[场景中可见的问题]
我们做的工作：[用日常语言说明的操作，不堆模型缩写]
方法关系：[真实输入→操作→输出，以及必须保留的连接关系]
实验依据：[已核对的数值、单位、比较对象、数据范围；没有则删去]
本页结论：[由本页证据支持的一句话；若与标题重复则不再另列]
其余上屏文字（按分区列出）：[短标题、短句与图中标注]

版式：[例如上方约六成为横向方法图，下方约三成为同条件结果对照]
主要视觉：[真实全景+对应人物放大／连续帧+动作发生时刻／方法图+结果对照]
阅读顺序：[左→右或上→下]。放大框对应真实位置，箭头表达明确关系。

视觉语言：白底，黑色大标题左对齐，下方一条横线；用两至三个清晰分区承载
主要内容，分区需要时使用黑色圆角框；红色只强调难点、关键操作或结果变化。
优先让真实画面、局部放大、时间序列和紧凑图表解释工作。图像面积可从约
55%–65%起步，但以内容可读为准。正文简短、字号可读，不用小字塞满页面。
若用户已给出其他母版，以母版为准。

不要：把实验台账搬上屏；画一串没有实际操作含义的方框；给每个概念配图标；
添加画外音式小字、重复结论、大段说明、装饰性卡片、与主题无关的猫咪。
禁止补造：[未提供的数字、ID、时间、置信度、热图、方法模块或结论]。
参考图里的球队、方法名和成绩不得带入本页。
```

For several pages, establish one representative design, then generate each page with its own content contract and the same visual grammar. For an explicit whole-deck image request, generate every requested slide; do not limit delivery to the representative page. Reuse layouts where they fit, but do not force identical boxes onto every kind of content.

## 3. Preserve facts and inspect the image

- Check Chinese characters, exact numbers, units, category labels, arrows, crop correspondence, and time order against the page contract.
- Keep real evidence intact. Generated reconstructions of photos, plots, or heatmaps cannot substantiate an experimental claim. Use the actual assets, or restore the original evidence regions in the final composition and verify the result.
- A measured chart must be rendered from its data and checked, not accepted because generated bars look convincing. Do not guess or repaint an unreadable value.
- Explain a low result with a visible failure or verified diagnostic; mark an untested explanation as a hypothesis.
- Fix a concrete defect locally where possible. Do not accept incorrect text in an image-only final deliverable, and do not loop over cosmetic alternatives after a satisfactory result.

## 4. Deliver or reconstruct

- **Images requested**: deliver ordered complete-slide PNGs (or equivalent) plus a contact sheet for several pages. State that these are image slides. A PPT containing one bitmap per page is an image deck, not an editable deck.
- **Images then editable PPTX requested**: continue with [editable-delivery.md](editable-delivery.md), preserving the approved composition. Do not wait for confirmation unless the user explicitly asked to review first or a material decision is missing.
- **Tool unavailable**: explain that actual image generation could not be performed. Provide a ready-to-use page specification or a native slide alternative, clearly identified as such.
