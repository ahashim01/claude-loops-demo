"""ANTI-EXAMPLE: "coverage theater".

This is what a naive `loop until 90% coverage` tends to produce: it *executes*
the code (so the coverage number shoots up) but asserts nothing about
correctness. Every one of these tests would still pass if the functions
returned complete garbage. DO NOT ship tests like this — a fake test is worse
than no test, because it gives false confidence right before a refactor.
"""
from src.api import MentionsService
from src.parser import parse_many
from src.aggregate import summary, top_channel


def test_touches_everything():
    svc = MentionsService()
    svc.ingest([{"id": 1, "text": "anything", "channel": "c"}])
    svc.report()
    svc.reset()
    parse_many([{"id": 2}])
    summary([])
    top_channel([])
    assert True  # <-- asserts nothing about correctness
