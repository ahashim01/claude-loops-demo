"""Text normalization helpers for mention bodies."""
import re

_URL = re.compile(r"https?://\S+")
_MENTION = re.compile(r"@\w+")
_WS = re.compile(r"\s+")


def strip_urls(text: str) -> str:
    return _URL.sub("", text)


def strip_mentions(text: str) -> str:
    return _MENTION.sub("", text)


def collapse_whitespace(text: str) -> str:
    return _WS.sub(" ", text).strip()


def normalize(text, *, drop_urls: bool = True, drop_mentions: bool = True) -> str:
    """Normalize a mention body for analysis."""
    if text is None:
        raise ValueError("text must not be None")
    out = text
    if drop_urls:
        out = strip_urls(out)
    if drop_mentions:
        out = strip_mentions(out)
    return collapse_whitespace(out)
