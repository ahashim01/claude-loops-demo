from src.aggregate import count_by_label, average_score


def test_count_by_label():
    assert count_by_label(["positive", "positive", "neutral"]) == {
        "positive": 2,
        "neutral": 1,
    }


def test_average_score():
    assert average_score([1.0, 0.0, -1.0]) == 0.0
    assert average_score([]) == 0.0
