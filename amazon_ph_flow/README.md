# amazon-ph-flow Crew

> **Last updated:** 2026-08-21

The `amazon-ph-flow` Crew is a multi-agent research workflow built on [crewAI](https://crewai.com). It produces the 8-output Amazon PPC market research captured in `output/01-market-opportunities.md` through `output/08-marketing-copy.md`.

## What it does

The flow runs 8 research tasks in sequence, each producing a markdown output:

| # | Output | Purpose |
|---|--------|---------|
| 01 | [Market Opportunities](./output/01-market-opportunities.md) | PH Amazon PPC training market sizing |
| 02 | [Competitive Landscape](./output/02-competitive-landscape.md) | Competitor analysis |
| 03 | [Consumer Behavior](./output/03-consumer-behavior.md) | VA / career-shifter personas |
| 04 | [Strategy Development](./output/04-strategy-development.md) | Channel + content strategy |
| 05 | [Partnership Opportunities](./output/05-partnership-opportunities.md) | VA agencies, Amazon seller communities |
| 06 | [UX/UI Design](./output/06-ux-ui-design.md) | Landing page + funnel design notes |
| 07 | [Content Strategy](./output/07-content-strategy.md) | 12-week content calendar skeleton |
| 08 | [Marketing Copy](./output/08-marketing-copy.md) | Tagline + ad copy variants |

The outputs feed directly into `MASTER-PLAN.md`, `marketing/MARKETING-STRATEGY.md`, `seo/SEO-PLAN.md`, and `content-calendar/CONTENT-CALENDAR.md`.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### Customizing

- Add your `OPENAI_API_KEY` to `.env` (already in `.gitignore`)
- Modify `src/amazon_ph_flow/config/agents.yaml` to define your agents
- Modify `src/amazon_ph_flow/config/tasks.yaml` to define your tasks
- Modify `src/amazon_ph_flow/crew.py` to add your own logic, tools and specific args
- Modify `src/amazon_ph_flow/main.py` to add custom inputs for your agents and tasks

## Running the Project

From the project root:

```bash
crewai run
```

This command initializes the `amazon-ph-flow` Flow as defined in your configuration and writes outputs to `output/`.

## Maintenance Notes

- The 8 outputs in `output/` are **frozen snapshots** from the original run. Re-running the flow will overwrite them — archive before re-running if you need to preserve history.
- The original CrewAI template used `{{crew_name}}` placeholders that were never filled in; the canonical crew name is `amazon-ph-flow` (used throughout the codebase and outputs).

## Support

- crewAI documentation: https://docs.crewai.com
- crewAI GitHub: https://github.com/joaomdmoura/crewai
- Project Amazon PH docs: see [`../AGENTS.md`](../AGENTS.md) and [`../docs/`](../docs/)
