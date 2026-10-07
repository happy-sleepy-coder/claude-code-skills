---
description: "Hook that denies AskUserQuestion unless the call already has evidence. Read when installing, or after a hook denial."
---

# Hooks

The skill text can be skipped. This hook cannot. It runs before `AskUserQuestion` and denies the call.

It arms only after this skill is invoked, and then stays for the session. To arm it on every session, also add the settings block below.

## What it denies

`scripts/ask-gate.py` reads the tool input and denies when:

- more than one question
- the text is a stall (which file, npm or pnpm, should I proceed, is the plan OK, paste the log)
- the question has no `Looked:` line and no `Recommended:` line

A denial is not a cue to ask in prose. Look or assume.

The hook cannot see the repo. A model can fake `Looked:`. The stall list still blocks the usual excuses. A real user-owned question is allowed if it carries the evidence line.

## Skill frontmatter

Already set on this skill. Command path is relative to the skill directory.

```yaml
hooks:
  PreToolUse:
    - matcher: "AskUserQuestion"
      hooks:
        - type: command
          command: "python3 ./scripts/ask-gate.py"
```

## Always on

Put this in the project `.claude/settings.json`, or `~/.claude/settings.json` for every project. Point `command` at the installed script.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/self-reasoning/scripts/ask-gate.py"
          }
        ]
      }
    ]
  }
}
```

Plugin installs use the plugin root instead of `~/.claude/skills`. The script only needs python3 and stdin JSON. No jq.

## After a denial

Do not call the tool again with the same question. Do not print the question in chat. Write `Assumption: ... because ...` and continue. A second denial in the same turn means you are overriding the hook. Stop asking.
