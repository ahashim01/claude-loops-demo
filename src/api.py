"""A tiny in-memory service tying parsing + aggregation together.

This is the integration surface for the demo: ingest raw payloads, then
report an aggregated summary across everything ingested.
"""
from .parser import parse_many
from .aggregate import summary

_EMPTY_REPORT = {"total": 0, "by_label": {}, "avg_score": 0.0, "top_channel": None}


class MentionsService:
    """In-memory mentions service."""

    def __init__(self):
        self._mentions = []

    def ingest(self, payloads):
        """Ingest raw payloads; returns the number ingested."""
        records = parse_many(payloads)
        self._mentions.extend(r.to_dict() for r in records)
        return len(records)

    def report(self):
        """Return an aggregated summary of everything ingested."""
        if not self._mentions:
            return dict(_EMPTY_REPORT)
        return summary(self._mentions)

    def reset(self):
        """Clear all ingested mentions."""
        self._mentions = []
