"""
Notification dispatcher — routes alerts to the right channel.

STATUS: Mid-refactor. email channel is done. slack and webhook are not yet updated.
Do not touch email. Complete slack and webhook to match the same pattern.
"""

from typing import Any


def _send_email(recipient: str, subject: str, body: str) -> dict:
    # DONE: refactored to return structured result
    return {"channel": "email", "recipient": recipient, "status": "queued"}


def _send_slack(channel: str, message: str) -> None:
    # TODO: refactor to return structured result like _send_email
    print(f"[slack] {channel}: {message}")


def _send_webhook(url: str, payload: dict[str, Any]) -> None:
    # TODO: refactor to return structured result like _send_email
    import urllib.request, json
    data = json.dumps(payload).encode()
    urllib.request.urlopen(urllib.request.Request(url, data=data))


def dispatch(channel: str, **kwargs: Any) -> dict:
    if channel == "email":
        return _send_email(
            recipient=kwargs["recipient"],
            subject=kwargs.get("subject", "Notification"),
            body=kwargs["body"],
        )
    elif channel == "slack":
        _send_slack(kwargs["channel_name"], kwargs["message"])
        return {}   # broken — should match email pattern
    elif channel == "webhook":
        _send_webhook(kwargs["url"], kwargs.get("payload", {}))
        return {}   # broken — should match email pattern
    else:
        raise ValueError(f"Unknown channel: {channel}")
