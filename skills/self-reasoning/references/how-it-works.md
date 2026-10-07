---
description: "What self-reasoning is, from public agent practice and papers. Read before asking, or when two approaches both look valid."
---

# How self-reasoning works

This skill is the look-first school. It is not an interview skill.

Public practice splits in two:

| School | What it does | When it fits |
| --- | --- | --- |
| Interview-first | Explore, then `AskUserQuestion` in rounds (feature-interview, grill-me, "when in doubt, ask") | User said interview me, spec workshop, or grill-me |
| Look-first (this skill) | Resolve from request, code, or a sensible default. Ask only if still blocked on something only the user knows | Implement, fix, debug, plan, ship |

Claude Code's own tool boundary matches look-first: use `AskUserQuestion` only when blocked on a decision you cannot resolve from the request, the code, or sensible defaults. Do not use it to ask if the plan is ready. That is `ExitPlanMode`.

Blocking questions are a known harness failure. Some coding CLIs dropped blocking ask tools because the model locks the turn waiting. If a call returns empty (seen in skill and command context, Claude Code issue 29674), treat it as no answer and take Recommended.

## Three moves that are actually "self-reasoning"

Do these in your head. Do not paste the scratch pad unless you assume or ask.

**1. Two candidates, then keep the one the files support.**

Self-consistency (Wang et al., ICLR 2023) samples many reasoning paths and keeps the answer they agree on. In a coding session, do not sample a crowd. Write two candidates:

- A: copy the sibling in this package
- B: the other approach you were about to ask about

Keep A if a file, test, lockfile, or ADR supports it. Discard B in one line. Ask only if A and B are both user-owned and neither is reversible.

**2. The tool is the evaluator. The user is not.**

Reflexion (Shinn et al., 2023) stores a short verbal note from task feedback and retries. Feedback here is the compiler, the test, Grep, the log. On failure, write one line (`Failed: assertion X in foo.test.ts`) and change the code. Do not ask "does this look right?" when a command can answer.

**3. Three private checks.**

From agent thinking-tool skills. Run them silently.

| Check | When | Fail means |
| --- | --- | --- |
| Collected | After the bounded look, before edit | You have not read the neighbor or the house file. Look again. |
| Adherence | Before the edit | The edit adds a feature they did not ask for. Cut it. |
| Done | Before you say finished | Tests for this layer did not run, or the original error is still the hypothesis. Run or reopen. |

A check that fails is not a question for the user.

## Verify the claim, then speak

Hallucination survey (Tonmoy et al., arXiv:2401.01313) and Anthropic's reduce-hallucinations guide agree on the coding move. The user is not the checker.

Chain-of-Verification: draft the answer, write the check, answer the check without rereading the draft, keep only what agrees.

Anthropic: a claim needs a quote. No quote, retract it. "Not in the repo" is allowed. Inventing a path is not.

For this skill, one check, not a second full generation:

```
Claim: orders handler is apps/api/src/orders/create.ts
Check: Grep POST /orders
Quote: create.ts:41 router.post("/orders"
Keep: yes
```

No quote: drop the claim. Look once more, or say it is not in the tree and assume the smallest reversible place. Do not ask "is this the right file?"

Ask the user only when the evidence is missing and the fact is theirs (MixAlign's exception, not the default). A secret, a product fork, a destructive go-ahead. Not a path, a flag, or a test command.

## Failure class, not a score

Langflow discussion 12111: a single "hallucination rate" is too broad. Name the miss, then fix that miss. Do not ask the user which class it is.

| Class | In this skill | Fix |
| --- | --- | --- |
| Unsupported claim | Named a file, flag, or command with no quote | Retract. Grep or Read. |
| Retrieval miss | The fact is in the tree and you did not search | Look. Do not abstain yet. |
| Abstention miss | Not in the tree, and you invented a path anyway | Say it is not there. Assume the smallest reversible place. |
| Citation mismatch | You cited a file, and the line does not say what you claimed | Drop the claim. Read the line again. |

Do not import the rest of that thread. Three sampled runs, Langfuse judges, and KL drift are production evals. This skill gets one quote from a tool it already called. Verify paths, commands, and code that will run. Skip the check on chatty status lines.

## What not to import

- Interview loops that ask 5–10 rounds before code. Those skills say so. This one does not.
- "When in doubt, ask." Doubt after a bounded look is an assumption.
- Multi-sample self-consistency inside the turn. Two candidates is the budget.
- Mental-model theatre (inversion, second-order) before a local bugfix. Use it only for a hard-to-undo product fork, and still prefer the repo pattern.
