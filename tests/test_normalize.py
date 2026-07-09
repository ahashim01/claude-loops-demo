from src.normalize import strip_urls, normalize


def test_strip_urls():
    assert strip_urls("see https://x.co/abc now") == "see  now"


def test_normalize_default():
    out = normalize("hey @user check https://x.co/1   thanks")
    assert "http" not in out
    assert "@user" not in out
    assert "  " not in out
