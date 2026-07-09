from src.api import MentionsService


def test_report_empty():
    svc = MentionsService()
    rep = svc.report()
    assert rep["total"] == 0
    assert rep["top_channel"] is None


def test_ingest_and_report():
    svc = MentionsService()
    n = svc.ingest([
        {"id": 1, "text": "I love it great", "channel": "twitter"},
        {"id": 2, "text": "this is bad terrible", "channel": "twitter"},
        {"id": 3, "text": "a neutral note", "channel": "instagram"},
    ])
    assert n == 3
    rep = svc.report()
    assert rep["total"] == 3
    assert rep["top_channel"] == "twitter"
    assert set(rep["by_label"]) <= {"positive", "negative", "neutral"}


def test_reset():
    svc = MentionsService()
    svc.ingest([{"id": 1, "text": "hi", "channel": "x"}])
    svc.reset()
    assert svc.report()["total"] == 0
