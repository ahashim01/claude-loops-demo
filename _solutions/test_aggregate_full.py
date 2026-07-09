from src.aggregate import top_channel, summary


def test_top_channel():
    assert top_channel([{"channel": "x"}, {"channel": "x"}, {"channel": "y"}]) == "x"


def test_top_channel_empty():
    assert top_channel([]) is None


def test_summary():
    mentions = [
        {"label": "positive", "score": 1.0, "channel": "x"},
        {"label": "negative", "score": -1.0, "channel": "y"},
    ]
    s = summary(mentions)
    assert s["total"] == 2
    assert s["by_label"] == {"positive": 1, "negative": 1}
    assert s["avg_score"] == 0.0
    assert s["top_channel"] in {"x", "y"}
