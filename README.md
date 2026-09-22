# 异瞳PPT · Yitong PPT

一个面向 Codex 的通用汇报 PPT Skill：从材料审阅、叙事规划、页面架构，到图片版视觉探索、可编辑 PPTX 重建和最终渲染检查。

它不是固定模板，也不会替你编造内容。它关注三件事：**讲清楚、证据可追溯、最终可编辑**。

## 适用场景

- 学术汇报：论文分享、方向 Tutorial、组会、答辩、学术会议。
- 项目汇报：立项、阶段进展、领导或客户汇报、工程评审、交付总结、路演。
- 已有 PPT 优化：保持原有品牌或母版，重构叙事、版式、图表和架构图。

## 核心特点

- 自动区分学术汇报与项目汇报，不把两套叙事硬拼在一起。
- 先建立事实与证据边界，再做页面规划。
- 简单页面直接做成可编辑对象；复杂架构页可先生成整页视觉草案，再重建为可编辑 PPTX。
- 默认采用白底、黑色结构、红色强调的“异瞳”视觉语言，也会优先服从用户提供的品牌模板。
- 区分实测结果、估算、目标、计划和概念示意。
- 最终通过渲染结果检查溢出、遮挡、字体、图表、引用和可编辑性。

## 安装

直接复制该页面网址给codex等agent，告诉它——“请帮我安装这个skill，并告诉我如何正确使用”。

### Windows PowerShell

```powershell
$SkillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
git clone https://github.com/tangyouci/yitong-ppt.git (Join-Path $SkillsRoot 'yitong-ppt')
```

### macOS / Linux

```bash
SKILLS_ROOT="${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/tangyouci/yitong-ppt.git "$SKILLS_ROOT/yitong-ppt"
```

安装后重启 Codex，使 Skill 重新加载。

## 使用

直接在请求中写 `$yitong-ppt`，并提供材料、受众、时长和希望得到的结果。例如：

```text
Use $yitong-ppt to turn this paper into a 15-minute Chinese group-meeting presentation. Focus on motivation, method logic, experiments, limitations, and one follow-up idea. Deliver an editable PPTX.
```

```text
使用 $yitong-ppt，把这些周报、指标和截图整理成 10 页项目阶段汇报。面向领导，突出问题、已完成工作、证据、风险和下一步决策，输出可编辑 PPTX。
```

更多示例见 [examples/prompts.md](examples/prompts.md)。

## 工作方式

```text
材料与证据
   ↓
受众、时长与汇报目标
   ↓
学术 / 项目 路由
   ↓
页面地图与关键结论
   ↓
直接编辑 或 复杂页视觉草案
   ↓
可编辑 PPTX 重建
   ↓
渲染检查与交付
```

## 依赖与兼容性

- 必需：支持 Skills 的 Codex 环境。
- PPTX 创建、读取和渲染能力取决于当前 Codex 环境可用的演示文稿工具。
- 图片生成和 PowerPoint 实时控制是可选增强能力，不是安装本 Skill 的硬依赖。
- 本仓库不包含私人项目素材、商业字体、受限模板或未经许可的第三方图片。

## 仓库结构

```text
yitong-ppt/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
│  ├─ academic-report.md
│  ├─ project-report.md
│  ├─ design-system.md
│  ├─ image-first-workflow.md
│  └─ editable-delivery.md
└─ examples/prompts.md
```

## 设计边界

- 不虚构实验、指标、引用、日期、人物、项目进度或商业结果。
- AI 生成图只作为设计探索或概念示意，不当作实验和业务证据。
- 不默认把整页图片当最终 PPT；用户要求可编辑时，应重建主要结构和文字。
- 引用外部图片、论文图表、品牌素材时，应遵守原始许可和署名要求。

## License

[MIT](LICENSE)

