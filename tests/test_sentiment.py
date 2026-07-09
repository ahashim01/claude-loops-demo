from src.sentiment import score, label


def test_score_positive():
    assert score("I love this, it is great and amazing") > 0


def test_score_negative():
    assert score("this is bad and terrible") < 0


def test_score_neutral_and_empty():
    assert score("") == 0.0
    assert score("a plain factual sentence") == 0.0


def test_label():
    assert label("love great amazing") == "positive"
    assert label("bad terrible awful") == "negative"
    assert label("") == "neutral"
