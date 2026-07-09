"""Parse raw mention payloads into normalized records."""
from .normalize import normalize
from .sentiment import score, label


class Mention:
    """A single normalized mention."""

    def __init__(self, id, text, channel):
        self.id = id
        self.text = text
        self.channel = channel

    def to_dict(self):
        clean = normalize(self.text)
        return {
            "id": self.id,
            "channel": self.channel,
            "text": clean,
            "score": round(score(clean), 3),
            "label": label(clean),
        }


def parse(payload: dict) -> Mention:
    """Parse a raw payload dict into a Mention."""
    if "id" not in payload:
        raise KeyError("payload missing 'id'")
    return Mention(
        id=payload["id"],
        text=payload.get("text", ""),
        channel=payload.get("channel", "unknown"),
    )


def parse_many(payloads):
    """Parse a list of raw payloads into Mentions."""
    return [parse(p) for p in payloads]
