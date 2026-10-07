---
description: "Good vs bad. Read before asking or when the user said stop asking."
---

# Examples

## "Fix the 500 on POST /orders"

Bad: Which file handles orders? Prisma or SQL?

Good: Grep `POST` + `orders`, read handler + test, patch the nil case, run the existing order tests.

`Assumption: handler is apps/api/src/orders/create.ts; 500 matches the unchecked inventory lookup.`

## "Add rate limiting to the public API"

Bad: Redis or memory? Which library? What limit?

Good when webhooks already limit with Redis: reuse that helper. Say you matched `apps/api/src/webhooks/rateLimit.ts`.

Good when nothing exists:

```
Looked: Grep `rateLimit`, Read `lib/redis.ts`. No public-API limiter.
Recommended: that Redis client at 60/min/IP.
Other: in-memory, single instance only.
```

## "Deploy this"

Bad: Should I deploy? Which env? Want me to read the workflow?

Good: Read `.github/workflows` and the deploy script. One target → that target. Prod vs staging unmarked → one question, staging recommended, prod needs an explicit go-ahead.

## "Don't ask, just do it"

`Action` cannot be `ask`. Repo default. Assumption line. Move.

## Plan mode

Bad: `AskUserQuestion` "Does this plan look good?"
Good: Plan with defaults. Plan approval is the confirm.

## "Which file should this go in?"

You do not ask this. Glob the feature folder. Put it next to the sibling. If two folders fit, the one with tests for that layer wins.

## "Can you confirm this is the auth module?"

You found `src/auth/session.ts` and its test. Do not confirm. Edit it.

## "Paste the CI log"

The log is in the terminal or `gh run view`. Read it.

## Two approaches, no question

Bad: "JWT or sessions?"

Good: sibling `apps/web` already uses session cookies. Candidate B was JWT. Drop B.

`Assumption: session cookies, same as apps/web/src/auth/session.ts.`

## Red test

Bad: "The test failed. Want me to change the assertion?"

Good: read the assertion, fix the code or the wrong expected value, rerun. One line: `Failed: create.test.ts expected 201, got 500. Retrying the nil inventory path.`

## Greenfield "build a CLI"

`package.json` already has `"bin"` and commander. Do not ask framework. Extend the existing CLI.
