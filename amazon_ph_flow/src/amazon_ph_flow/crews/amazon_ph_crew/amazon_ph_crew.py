"""
Amazon PH Market Intelligence Crew
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A comprehensive **7-agent specialized workforce** for Amazon Philippines
market analysis, strategy, and execution planning, using CrewAI v1.15.1
with OpenRouter free LLMs.

4-Phase Architecture:
  Phase 1 — Foundation Research  (Researcher, Analyst, Consumer Researcher)
  Phase 2 — Strategic Development (Strategist, Partnership Specialist)
  Phase 3 — Design & Content      (UX/UI Designer, Content Creator)
  Phase 4 — Execution & SEO       (Marketing Copywriter, SEO Specialist)

LLM: OpenRouter free tier — requires OPENROUTER_API_KEY in .env
"""

import os

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

# ── Load .env ───────────────────────────────────────────────────────
load_dotenv()

# ── LLM Configuration ───────────────────────────────────────────────
# Using OpenRouter free models for cost-effective operation.
# Each agent gets its own LLM to avoid rate-limit contention.
# Switch model by changing OPENROUTER_FREE_MODEL env var.
DEFAULT_MODEL = os.getenv("OPENROUTER_FREE_MODEL", "meta-llama/llama-3.3-70b-instruct:free")


def make_llm(model: str = None):
    """Create an OpenRouter LLM config string."""
    model_name = model or DEFAULT_MODEL
    return f"openrouter/{model_name}"


# ── Shared Tools ────────────────────────────────────────────────────
# Tools are instantiated once and shared across agents.
# If SERPER_API_KEY is not set, tools will be gracefully skipped at runtime.
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

try:
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    shared_tools = [search_tool, scrape_tool]
except Exception:
    shared_tools = []


@CrewBase
class AmazonPHCrew:
    """
    Amazon Philippines Market Intelligence Crew

    7 agents, 9 tasks, 4 phases — sequential execution.
    Each agent uses an OpenRouter free model for cost efficiency.
    """

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ── Phase 1: Foundation Research Agents ─────────────────────────

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=shared_tools,
            llm=make_llm(),
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst"],
            tools=shared_tools,
            llm=make_llm(),
        )

    @agent
    def consumer_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["consumer_researcher"],
            tools=shared_tools,
            llm=make_llm(),
        )

    # ── Phase 2: Strategic Development Agents ───────────────────────

    @agent
    def strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["strategist"],
            tools=shared_tools,
            llm=make_llm(),
        )

    @agent
    def partnership_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["partnership_specialist"],
            tools=shared_tools,
            llm=make_llm(),
        )

    # ── Phase 3: Design & Content Agents ────────────────────────────

    @agent
    def ux_ui_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["ux_ui_designer"],
            tools=shared_tools,
            llm=make_llm(),
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["content_creator"],
            tools=shared_tools,
            llm=make_llm(),
        )

    # ── Phase 4: Execution Agents ───────────────────────────────────

    @agent
    def marketing_copywriter(self) -> Agent:
        return Agent(
            config=self.agents_config["marketing_copywriter"],
            tools=shared_tools,
            llm=make_llm(),
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config["seo_specialist"],
            tools=shared_tools,
            llm=make_llm(),
        )

    # ── Phase 1: Foundation Research Tasks ──────────────────────────

    @task
    def market_opportunities(self) -> Task:
        return Task(config=self.tasks_config["market_opportunities"])

    @task
    def competitive_landscape(self) -> Task:
        return Task(config=self.tasks_config["competitive_landscape"])

    @task
    def consumer_behavior(self) -> Task:
        return Task(config=self.tasks_config["consumer_behavior"])

    # ── Phase 2: Strategic Development Tasks ────────────────────────

    @task
    def strategy_development(self) -> Task:
        return Task(config=self.tasks_config["strategy_development"])

    @task
    def partnership_opportunities(self) -> Task:
        return Task(config=self.tasks_config["partnership_opportunities"])

    # ── Phase 3: Design & Content Tasks ─────────────────────────────

    @task
    def ux_ui_design(self) -> Task:
        return Task(config=self.tasks_config["ux_ui_design"])

    @task
    def content_strategy(self) -> Task:
        return Task(config=self.tasks_config["content_strategy"])

    # ── Phase 4: Execution Tasks ────────────────────────────────────

    @task
    def marketing_copy(self) -> Task:
        return Task(config=self.tasks_config["marketing_copy"])

    @task
    def seo_optimization(self) -> Task:
        return Task(config=self.tasks_config["seo_optimization"])

    # ── Crew Assembly ──────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Assemble the Amazon PH Market Intelligence Crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
