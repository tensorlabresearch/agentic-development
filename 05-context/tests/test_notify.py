import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.notify import dispatch


def test_email_dispatch_returns_structured_result():
    result = dispatch("email", recipient="a@b.com", body="hello")
    assert result["channel"] == "email"
    assert result["status"] == "queued"

def test_slack_dispatch_returns_structured_result():
    result = dispatch("slack", channel_name="#alerts", message="hello")
    assert result.get("channel") == "slack"
    assert result.get("status") == "queued"

def test_webhook_dispatch_returns_structured_result():
    result = dispatch("webhook", url="http://localhost/hook", payload={"event": "test"})
    assert result.get("channel") == "webhook"
    assert result.get("status") == "queued"
