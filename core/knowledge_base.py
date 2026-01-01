from __future__ import annotations
"""
core.knowledge_base

Simple knowledge base placeholder to store and retrieve key facts.
"""
from typing import Any, Dict


class KnowledgeBase:
    """In-memory knowledge base placeholder."""

    def __init__(self) -> None:
        self._facts: Dict[str, Any] = {}

    def add_fact(self, key: str, value: Any) -> None:
        """Add a fact to the knowledge base."""
        self._facts[key] = value

    def get_fact(self, key: str, default: Any | None = None) -> Any:
        """Retrieve a fact from the knowledge base."""
        return self._facts.get(key, default)
