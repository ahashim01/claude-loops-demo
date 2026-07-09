import pytest
from src.normalize import strip_mentions, normalize


def test_strip_mentions():
    assert strip_mentions("hi @user and @two") == "hi  and "


def test_normalize_none_raises():
    with pytest.raises(ValueError):
        normalize(None)


def test_normalize_flags_off():
    out = normalize("keep @user and https://x.co/1", drop_urls=False, drop_mentions=False)
    assert "@user" in out
    assert "http" in out
