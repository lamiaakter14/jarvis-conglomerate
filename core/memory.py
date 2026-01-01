from __future__ import annotations
"""
core.memory

Simple memory component placeholder for storing past analyses.
"""
from typing import Any, Dict, List


class Memory:
    """Stores past analyses and can retrieve them for context."""

    def __init__(self) -> None:
        self.past_analyses: List[Dict[str, Any]] = []

    def store_analysis(self, problem: str, result: Dict[str, Any]) -> None:
        """Save an analysis result with its problem statement."""
        self.past_analyses.append({"problem": problem, "result": result})

    def last(self) -> Dict[str, Any] | None:
        """Return the last stored analysis, if any."""
        return self.past_analyses[-1] if self.past_analyses else None
