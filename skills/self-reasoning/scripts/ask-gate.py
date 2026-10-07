#!/usr/bin/env python3
"""PreToolUse gate for AskUserQuestion. The model cannot skip this."""

import json
import re
import sys

STALL = re.compile(
    r"which file|which folder|which package|npm or pnpm|pnpm or npm|"
    r"should i proceed|do you want me to|want me to proceed|is the plan|"
    r"does this plan|is this the right file|can i run the tests|should i add a test|"
    r"paste the (log|file|stack)|how do i run",
    re.I,
)


def deny(reason):
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    sys.stdout.write("\n")


def main():
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        deny("AskUserQuestion blocked: hook could not read the tool input. Look or assume.")
        return

    tool_input = payload.get("tool_input") or payload.get("toolInput") or {}
    questions = tool_input.get("questions") or []
    if isinstance(questions, dict):
        questions = [questions]

    texts = []
    for q in questions:
        if isinstance(q, str):
            texts.append(q)
            continue
        if not isinstance(q, dict):
            continue
        texts.append(str(q.get("question") or ""))
        for opt in q.get("options") or []:
            if isinstance(opt, dict):
                texts.append(str(opt.get("label") or ""))
                texts.append(str(opt.get("description") or ""))
            else:
                texts.append(str(opt))
    blob = "\n".join(texts)

    if len(questions) > 1:
        deny(
            "AskUserQuestion blocked: one question max. "
            "Look, or write Assumption: <choice> because <file>. Do not ask again."
        )
        return

    if STALL.search(blob):
        deny(
            "AskUserQuestion blocked: this is a look-or-assume stall "
            "(file, package manager, proceed, plan approval, paste). Do not ask in prose either."
        )
        return

    if "Looked:" not in blob or "Recommended:" not in blob:
        deny(
            "AskUserQuestion blocked: missing Looked: and Recommended:. "
            "Search the repo first. If you can name a default, assume it. "
            "Ask only when the user is the only one who knows, with the evidence line in the question."
        )
        return


if __name__ == "__main__":
    main()
