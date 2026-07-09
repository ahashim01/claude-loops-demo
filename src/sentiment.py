"""Sentiment scoring for social mentions (toy, deterministic)."""

POSITIVE = {"love", "great", "excellent", "good", "happy", "amazing", "ممتاز", "رائع"}
NEGATIVE = {"hate", "bad", "terrible", "awful", "angry", "poor", "سيء"}


def score(text: str) -> float:
    """Return a sentiment score in [-1, 1] for the given text."""
    if not text:
        return 0.0
    words = text.lower().split()
    pos = sum(1 for w in words if w in POSITIVE)
    neg = sum(1 for w in words if w in NEGATIVE)
    total = pos + neg
    if total == 0:
        return 0.0
    return (pos - neg) / total


def label(text: str) -> str:
    """Classify text as positive / negative / neutral."""
    s = score(text)
    if s > 0.2:
        return "positive"
    if s < -0.2:
        return "negative"
    return "neutral"
