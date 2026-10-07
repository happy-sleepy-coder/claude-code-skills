---
description: "Ways this skill fails in Claude Code. Read when you are about to ask anyway."
---

# Gotchas

The model will try to ask anyway. These are the usual holes.

| Impulse | What is going on | Do this |
| --- | --- | --- |
| "Quick questions before I start" | Interview habit from other skills | Run the loop. Look first. |
| Three stacked AskUserQuestion cards | Batching to feel thorough | One question or zero |
| "Is this the right file?" | Anxiety after a Grep hit | If the test sits next to it, edit it |
| "Want me to proceed?" | Permission theater | Proceed |
| Asking npm vs pnpm | Did not open the lockfile | Open the lockfile |
| Asking how tests run | Did not open package.json / CI | Open them |
| Asking the user to paste a file | You have Read | Read |
| Asking in a subagent | Subagent cannot see the user well | Assume and return the assumption |
| Plan-mode "look good?" | Wrong tool. Approval is ExitPlanMode | Exit plan |
| Second questionnaire after they answered | Loop not closed | Work with the answer |
| "Which of my three plans?" | You already did the thinking | Two candidates. Ship the repo-shaped one |
| Broad "how do you want this built?" | Skipped neighbor code | Read the sibling feature |
| Asking after "just do it" | Ignored the user | Assume |
| Empty AskUserQuestion result | Tool can auto-submit blank in skill or command context | Treat as no answer. Take Recommended |
| Waiting on the user to confirm a test | User is not the evaluator | Run the test. Reflect on the failure. Retry |
| Copying an interview skill into this one | feature-interview and grill-me are a different school | Do not round-trip questions unless they asked to be interviewed |
| Naming a file you did not open | Draft with no quote | Retract. Grep, then quote the line, or say it is not in the tree |
| Asking the user if your path is right | CoVe check aimed at the user | Answer the check from the file |

If you wrote a question and then noticed it matches this table, delete the question and look or assume.
