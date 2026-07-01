#!/usr/bin/env python
"""
Amazon PH Market Intelligence Flow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Implements the 4-phase orchestration for the Amazon.PH Crew:

  Phase 1 → Foundation Research  (Tasks 1-3)
  Phase 2 → Strategic Development (Tasks 4-5)
  Phase 3 → Design & Content      (Tasks 6-7)
  Phase 4 → Execution & SEO       (Tasks 8-9)

Uses CrewAI Flows with state management, enhanced documentation
logging, and OpenRouter free LLMs.

Usage:
    crewai run              # run the full 4-phase flow
    crewai plot             # visualize the flow graph
    python -m amazon_ph_flow.main  # direct execution
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from amazon_ph_flow.crews.amazon_ph_crew.amazon_ph_crew import AmazonPHCrew

# ── Load .env ────────────────────────────────────────────────────────────
load_dotenv()

# ── Flow State Model ────────────────────────────────────────────────────


class AmazonPHState(BaseModel):
    """Persistent state carried across all 4 phases of the workflow."""

    # Research topic
    topic: str = "Amazon Philippines Market Entry"

    # Phase completion flags
    phase_1_complete: bool = False
    phase_2_complete: bool = False
    phase_3_complete: bool = False
    phase_4_complete: bool = False

    # Phase 1 — Foundation Research outputs
    market_report: str = ""
    competitive_report: str = ""
    consumer_report: str = ""

    # Phase 2 — Strategic Development outputs
    strategy_report: str = ""
    partnership_report: str = ""

    # Phase 3 — Design & Content outputs
    design_report: str = ""
    content_report: str = ""

    # Phase 4 — Execution & SEO outputs
    copy_report: str = ""
    seo_report: str = ""

    # Execution metadata
    started_at: str = ""
    completed_at: str = ""


# ── Enhanced Documentation System — SecondBrain Integration ─────────────


class ExecutionLogger:
    """Comprehensive execution logging per the implementation guide."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.log_path = output_dir / "execution-log.jsonl"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def log(self, phase: str, task: str, agent: str, status: str, detail: str = ""):
        """Log a task execution event."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "phase": phase,
            "task": task,
            "agent": agent,
            "status": status,
            "detail": detail[:200],
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
        icon = {"started": "▶️", "completed": "✅", "failed": "❌", "skipped": "⏭️"}.get(
            status, "📌"
        )
        print(f"  {icon} [{phase}] {task} → {status}")


def _print_banner():
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   🛒  AMAZON PHILIPPINES MARKET INTELLIGENCE CREW      ║")
    print("║   7 Agents · 9 Tasks · 4 Phases · OpenRouter Free      ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    model = os.getenv("OPENROUTER_FREE_MODEL", "meta-llama/llama-3.3-70b-instruct:free")
    has_key = bool(os.getenv("OPENROUTER_API_KEY"))
    print(f"   🤖 LLM: {model}")
    print(f"   🔑 OpenRouter API Key: {'✅ Set' if has_key else '❌ MISSING — set OPENROUTER_API_KEY in .env'}")
    print(f"   🔄 Process: Sequential · 4 Phases")
    print()


# ── Flow Definition ─────────────────────────────────────────────────────


class AmazonPHFlow(Flow[AmazonPHState]):
    """
    Amazon PH Market Intelligence Flow

    Orchestrates the entire 4-phase workflow with:
    - Sequential task execution with phase barriers
    - Enhanced documentation logging
    - State management across all phases
    - Consolidated master report generation
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        output_dir = Path("output")
        self.logger = ExecutionLogger(output_dir)

    # ── Phase 0: Initialize ──────────────────────────────────────────

    @start()
    def prepare_topic(self, crewai_trigger_payload: dict | None = None):
        """Initialize the flow — set topic from trigger or default."""
        _print_banner()
        self.state.started_at = datetime.utcnow().isoformat()

        if crewai_trigger_payload and "topic" in crewai_trigger_payload:
            self.state.topic = crewai_trigger_payload["topic"]
            print(f"   📌 Topic from trigger: {self.state.topic}")
        else:
            print(f"   📌 Topic: {self.state.topic}")

        print(f"   🕐 Started: {self.state.started_at}")
        print()

    # ── Phase 1: Foundation Research (Tasks 1-3) ─────────────────────

    @listen(prepare_topic)
    def phase_1_market_opportunities(self):
        """Task 1: Market opportunities analysis — Agent: Researcher."""
        self.logger.log("Phase 1", "Market Opportunities Analysis", "Researcher", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Market Opportunities"})
        )
        self.state.market_report = result.raw
        self.logger.log("Phase 1", "Market Opportunities Analysis", "Researcher", "completed")
        return result

    @listen(phase_1_market_opportunities)
    def phase_1_competitive_landscape(self):
        """Task 2: Competitive landscape — Agent: Analyst."""
        self.logger.log("Phase 1", "Competitive Landscape Analysis", "Analyst", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Competitive Landscape"})
        )
        self.state.competitive_report = result.raw
        self.logger.log("Phase 1", "Competitive Landscape Analysis", "Analyst", "completed")
        return result

    @listen(phase_1_competitive_landscape)
    def phase_1_consumer_behavior(self):
        """Task 3: Consumer behavior — Agent: Consumer Researcher."""
        self.logger.log("Phase 1", "Consumer Behavior Analysis", "Consumer Researcher", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Consumer Behavior"})
        )
        self.state.consumer_report = result.raw
        self.state.phase_1_complete = True
        self.logger.log("Phase 1", "Consumer Behavior Analysis", "Consumer Researcher", "completed")
        print("\n   ✅ PHASE 1 COMPLETE — Foundation Research done.\n")
        return result

    # ── Phase 2: Strategic Development (Tasks 4-5) ───────────────────

    @listen(phase_1_consumer_behavior)
    def phase_2_strategy_development(self):
        """Task 4: Go-to-market strategy — Agent: Strategist."""
        self.logger.log("Phase 2", "Strategy Development", "Strategist", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Go-to-Market Strategy"})
        )
        self.state.strategy_report = result.raw
        self.logger.log("Phase 2", "Strategy Development", "Strategist", "completed")
        return result

    @listen(phase_2_strategy_development)
    def phase_2_partnership_opportunities(self):
        """Task 5: Partnerships — Agent: Partnership Specialist."""
        self.logger.log("Phase 2", "Partnership Opportunities", "Partnership Specialist", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Partnership Opportunities"})
        )
        self.state.partnership_report = result.raw
        self.state.phase_2_complete = True
        self.logger.log("Phase 2", "Partnership Opportunities", "Partnership Specialist", "completed")
        print("\n   ✅ PHASE 2 COMPLETE — Strategy & Partnerships done.\n")
        return result

    # ── Phase 3: Design & Content (Tasks 6-7) ────────────────────────

    @listen(phase_2_partnership_opportunities)
    def phase_3_ux_ui_design(self):
        """Task 6: UX/UI design — Agent: UX/UI Designer."""
        self.logger.log("Phase 3", "UX/UI Design", "UX/UI Designer", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — UX/UI Design"})
        )
        self.state.design_report = result.raw
        self.logger.log("Phase 3", "UX/UI Design", "UX/UI Designer", "completed")
        return result

    @listen(phase_3_ux_ui_design)
    def phase_3_content_strategy(self):
        """Task 7: Content strategy — Agent: Content Creator."""
        self.logger.log("Phase 3", "Content Strategy", "Content Creator", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Content Strategy"})
        )
        self.state.content_report = result.raw
        self.state.phase_3_complete = True
        self.logger.log("Phase 3", "Content Strategy", "Content Creator", "completed")
        print("\n   ✅ PHASE 3 COMPLETE — Design & Content done.\n")
        return result

    # ── Phase 4: Execution & SEO (Tasks 8-9) ─────────────────────────

    @listen(phase_3_content_strategy)
    def phase_4_marketing_copy(self):
        """Task 8: Marketing copy — Agent: Marketing Copywriter."""
        self.logger.log("Phase 4", "Marketing Copy", "Marketing Copywriter", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — Marketing Copy"})
        )
        self.state.copy_report = result.raw
        self.logger.log("Phase 4", "Marketing Copy", "Marketing Copywriter", "completed")
        return result

    @listen(phase_4_marketing_copy)
    def phase_4_seo_optimization(self):
        """Task 9: SEO — Agent: SEO Specialist."""
        self.logger.log("Phase 4", "SEO Optimization", "SEO Specialist", "started")
        result = (
            AmazonPHCrew()
            .crew()
            .kickoff(inputs={"topic": f"{self.state.topic} — SEO Strategy"})
        )
        self.state.seo_report = result.raw
        self.state.phase_4_complete = True
        self.state.completed_at = datetime.utcnow().isoformat()
        self.logger.log("Phase 4", "SEO Optimization", "SEO Specialist", "completed")
        print("\n   ✅ PHASE 4 COMPLETE — Execution & SEO done.\n")
        return result

    # ── Final: Consolidate & Save ────────────────────────────────────

    @listen(phase_4_seo_optimization)
    def save_consolidated_report(self):
        """Consolidate all 9 task outputs into a master report."""
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║   📦  GENERATING CONSOLIDATED MASTER REPORT            ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print()

        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)

        report = f"""# Amazon Philippines Market Intelligence — Master Report

**Topic:** {self.state.topic}
**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
**Execution Duration:** {self.state.started_at} → {self.state.completed_at}
**Process:** Sequential · 7 Agents · 9 Tasks · 4 Phases

---

## 📊 Phase 1: Foundation Research

### 1. Market Opportunities
{self.state.market_report}

---

### 2. Competitive Landscape
{self.state.competitive_report}

---

### 3. Consumer Behavior
{self.state.consumer_report}

---

## 🎯 Phase 2: Strategic Development

### 4. Go-to-Market Strategy
{self.state.strategy_report}

---

### 5. Partnership Opportunities
{self.state.partnership_report}

---

## 🎨 Phase 3: Design & Content

### 6. UX/UI Design Recommendations
{self.state.design_report}

---

### 7. Content Strategy
{self.state.content_report}

---

## ✍️ Phase 4: Execution & SEO

### 8. Marketing Copy
{self.state.copy_report}

---

### 9. SEO Optimization
{self.state.seo_report}

---

*Generated by Amazon PH CrewAI Flow — 7 agents, 9 tasks, 4 phases*
"""

        report_path = output_dir / "amazon-ph-master-report.md"
        report_path.write_text(report)
        print(f"   📄 Master report: {report_path.resolve()}")
        print(f"   📄 Execution log:  {(output_dir / 'execution-log.jsonl').resolve()}")
        print()
        print("╔══════════════════════════════════════════════════════════╗")
        print("║   ✅  AMAZON PH WORKFLOW COMPLETE                      ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print()


# ── Entry Points ────────────────────────────────────────────────────────


def kickoff():
    """Entry point for `crewai run`."""
    flow = AmazonPHFlow()
    flow.kickoff()


def plot():
    """Entry point for `crewai plot` — generates flow diagram."""
    flow = AmazonPHFlow()
    flow.plot()


def run_with_trigger():
    """Run with a JSON trigger payload from CLI."""
    if len(sys.argv) < 2:
        raise Exception(
            "No trigger payload provided. Please provide JSON payload as argument."
        )
    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    flow = AmazonPHFlow()
    try:
        return flow.kickoff({"crewai_trigger_payload": trigger_payload})
    except Exception as e:
        raise Exception(f"Error running flow with trigger: {e}")


if __name__ == "__main__":
    kickoff()
