"""Aggregation over scored mentions."""
from collections import defaultdict


def count_by_label(labels):
    """Count occurrences of each label."""
    counts = defaultdict(int)
    for lab in labels:
        counts[lab] += 1
    return dict(counts)


def average_score(scores):
    """Mean of the given scores, or 0.0 when empty."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def top_channel(mentions):
    """Return the channel with the most mentions, or None when empty."""
    counts = defaultdict(int)
    for m in mentions:
        counts[m.get("channel", "unknown")] += 1
    if not counts:
        return None
    return max(counts, key=counts.get)


def summary(mentions):
    """Build a small summary dict for a list of mention dicts."""
    labels = [m["label"] for m in mentions if "label" in m]
    scores = [m["score"] for m in mentions if "score" in m]
    return {
        "total": len(mentions),
        "by_label": count_by_label(labels),
        "avg_score": round(average_score(scores), 3),
        "top_channel": top_channel(mentions),
    }
