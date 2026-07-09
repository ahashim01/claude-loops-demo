import pytest
from src.parser import Mention, parse, parse_many


def test_parse_builds_mention():
    m = parse({"id": 1, "text": "I love it", "channel": "twitter"})
    assert isinstance(m, Mention)
    assert m.id == 1
    assert m.channel == "twitter"


def test_parse_defaults_channel_and_text():
    m = parse({"id": 2})
    assert m.channel == "unknown"
    assert m.text == ""


def test_parse_missing_id_raises():
    with pytest.raises(KeyError):
        parse({"text": "no id"})


def test_to_dict_normalizes_and_scores():
    m = parse({"id": 3, "text": "check https://x.co/1 @user great", "channel": "ig"})
    d = m.to_dict()
    assert d["id"] == 3
    assert "http" not in d["text"]
    assert d["label"] in {"positive", "neutral", "negative"}


def test_parse_many():
    ms = parse_many([{"id": 1}, {"id": 2}])
    assert len(ms) == 2
