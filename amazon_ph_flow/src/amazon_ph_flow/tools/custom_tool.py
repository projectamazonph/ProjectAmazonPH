"""
Amazon PH Custom Tools for CrewAI Agents

Provides specialized tools for Amazon Philippines market analysis,
including tools for e-commerce research, consumer behavior analysis,
and market intelligence gathering.
"""

from typing import Type

from pydantic import BaseModel, Field

from crewai.tools import BaseTool


class AmazonMarketSearchInput(BaseModel):
    """Input schema for AmazonMarketSearchTool."""

    query: str = Field(
        ..., description="Search query for Amazon PH market intelligence."
    )
    market: str = Field(
        default="Philippines",
        description="Target market (default: Philippines).",
    )


class AmazonMarketSearchTool(BaseTool):
    """Tool for searching Amazon Philippines market intelligence."""

    name: str = "Amazon Market Intelligence Search"
    description: str = (
        "Search for current Amazon Philippines market data, competitor "
        "intelligence, consumer trends, and e-commerce statistics. "
        "Use this tool to gather background market research data."
    )
    args_schema: Type[BaseModel] = AmazonMarketSearchInput

    def _run(self, query: str, market: str = "Philippines") -> str:
        """Execute market search. For now returns a guidance message."""
        return (
            f"Search query for {market}: '{query}'\n"
            f"Use SerperDevTool or ScrapeWebsiteTool for actual web search. "
            f"This tool prepares the structured query for those tools."
        )


class ConsumerInsightInput(BaseModel):
    """Input schema for ConsumerInsightTool."""

    segment: str = Field(
        ..., description="Consumer segment to analyze (e.g., 'urban millennials')."
    )
    market: str = Field(
        default="Philippines",
        description="Target market for consumer insight analysis.",
    )


class ConsumerInsightTool(BaseTool):
    """Tool for analyzing Filipino consumer behavior patterns."""

    name: str = "Filipino Consumer Insight Tool"
    description: str = (
        "Analyze Filipino online consumer behavior, purchasing patterns, "
        "payment preferences, and cultural factors affecting e-commerce "
        "adoption. Use alongside web search for current data."
    )
    args_schema: Type[BaseModel] = ConsumerInsightInput

    def _run(self, segment: str, market: str = "Philippines") -> str:
        return (
            f"Consumer insight analysis for {market}: {segment} segment.\n"
            f"Combine this analysis with actual web search results via "
            f"SerperDevTool for current market data."
        )


class LocalizationGuideInput(BaseModel):
    """Input schema for LocalizationGuideTool."""

    content_type: str = Field(
        ...,
        description="Type of content to localize (e.g., 'product page', 'email', 'social post').",
    )
    target_market: str = Field(
        default="Philippines",
        description="Target market for localization.",
    )


class LocalizationGuideTool(BaseTool):
    """Tool for providing Philippine market localization guidance."""

    name: str = "PH Market Localization Guide"
    description: str = (
        "Get culturally-informed guidance for localizing content, "
        "UI/UX, and marketing for the Philippine market. Covers "
        "Taglish integration, cultural references, trust signals, "
        "and visual design preferences specific to Filipino users."
    )
    args_schema: Type[BaseModel] = LocalizationGuideInput

    def _run(self, content_type: str, target_market: str = "Philippines") -> str:
        return (
            f"Localization guide for {target_market}: {content_type}.\n"
            f"Consider Taglish language integration, mobile-first design, "
            f"trust signals (GCash/Maya badges, return policies), "
            f"and culturally-relevant imagery. Combine with web research."
        )
