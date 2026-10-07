---
description: "When a question is allowed vs forbidden. Read before AskUserQuestion or a clarifying question."
---

# Ask gate

Blocked means all three failed: the request does not say, the code does not pick, and no sensible default exists. Claude Code's own rule for `AskUserQuestion` is that sentence. If you can name a default, you are not blocked.

Ask only if every line is also true:

1. Cheap undo is false — a wrong call here is hard to reverse.
2. You already searched the request, the repo, git, and public docs.
3. Neighbor code does not already pick a pattern.
4. No safe default exists.
5. The user is the only person who knows.

If any line is false, look or assume. "When in doubt, ask" is the other school. Doubt after a bounded look is an assumption.

## Cheap undo

Assume, do not ask:

| Choice | Why it is cheap |
| --- | --- |
| File path, folder, helper name | Rename or move later |
| Match existing library | Repo already pays the cost |
| Test added next to neighbors | Delete the file |
| Extra log line / flag default off | Revert the diff |
| Plan contents in plan mode | User rejects the plan |
| Implementation approach when one sibling exists | Copy the sibling |

Ask, after the look:

| Choice | Why it is theirs |
| --- | --- |
| Prod migrate, delete, force-push | Data or history loss |
| Email customers / spend money | External side effect |
| Secret value missing from env | Only they have it |
| Product audience the repo never states | Two real products |
| Brand / copy / UX with no existing screen | Taste |
| Scope they never named | They asked for a typo, not a rewrite |

## Do not ask

| Topic | Do this |
| --- | --- |
| File location | Grep / Glob |
| How a function works | Read it |
| Which library | package manifest + imports |
| Test or lint command | package.json, Makefile, CI |
| Node / Python / package manager | lockfile (`pnpm-lock.yaml` wins over a question) |
| Public API shape | vendor docs |
| New helper name | match the folder |
| Whether to read a file | read it |
| "Is this the right file?" | If Grep hit it and the test sits next to it, it is |
| Plan OK in plan mode | Exit plan for approval |
| Paste this log / file | Read the terminal or workspace |
| Dark/light, spacing, copy on an existing screen | Match the screen |

## Permission theater

| Stall | Action |
| --- | --- |
| Want me to check the repo? | Check the repo |
| Should I search the web? | Search only for third-party APIs |
| Can I run the tests? | Run the relevant tests |
| Should I add a test? | Add one if this layer already has tests |
| Do you want me to proceed? | They already gave the task |
| Which of these three plans? | Pick the one that matches the repo, put the others in one rejected line |

## Greenfield

Empty or tiny repo, no sibling pattern:

1. Still do not ask stack questions the lockfile or scaffold already answered.
2. If the user named the outcome and not the stack, pick the smallest common default and assume.
3. Ask once only for a product fork (who it is for, paid vs free, destroy vs keep data).

## Question shape

One question. The tool allows up to four. This skill allows one. Two only if they are independent and both user-owned. Never a second round.

Recommended option first. End that label with `(Recommended)`. Header at most 12 characters. 2–4 options. Do not list "Other". The UI adds it.

Do not ask "is the plan OK?", "should I proceed?", or anything that mentions "the plan". Approval is `ExitPlanMode`.

Empty result (skill and command context can auto-submit blank, issue 29674): no answer. Take Recommended and say so in one sentence. Do not ask again.

```
Looked: <tools and paths>
Blocked on: <why only the user knows>
Recommended: <option + why>
Other: <option>
```

Two axes (who + where) go in one turn. Do not ask axis 1, wait, then axis 2.
