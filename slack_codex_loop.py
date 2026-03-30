"""Slack loop integration for the workshop SearchAgent.

Run locally:
    source venv/bin/activate
    python slack_codex_loop.py

Required env vars:
    SLACK_BOT_TOKEN
    SLACK_APP_TOKEN
Optional env vars:
    SLACK_DEFAULT_HOST ("xai" or "groq", defaults to "xai")
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from Agents.websearchagent import SearchAgent

load_dotenv()


def _build_agent() -> SearchAgent:
    host = os.getenv("SLACK_DEFAULT_HOST", "xai").strip().lower() or "xai"
    if host not in {"xai", "groq"}:
        host = "xai"
    return SearchAgent(delay=0, host=host)


app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.event("app_mention")
def handle_app_mention(event, say):
    text = (event.get("text") or "").strip()
    cleaned_query = " ".join(
        part for part in text.split() if not part.startswith("<@")
    ).strip()

    if not cleaned_query:
        say("Please mention me with a question, for example: `@agent latest AI news`. ")
        return

    say(f"Working on: `{cleaned_query}`")

    try:
        agent = _build_agent()
        result = agent.call(cleaned_query)
        last_output = result.memory.steps[-1].model_output if result.memory.steps else "No output generated."
        say(last_output[:3000])
    except Exception as exc:  # noqa: BLE001
        say(f"I hit an error while running the agent: `{exc}`")


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
