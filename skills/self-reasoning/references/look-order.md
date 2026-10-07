---
description: "Search order before asking. Read when you do not know where a fact lives."
---

# Look order

Smallest tool first. Stop when you have the fact.

## 1. Request

Current message, last few turns, @-paths. If they named a file, start there.

## 2. Exact strings

Grep the error, symbol, route, flag, unique phrase.
Glob likely folders (`**/*auth*`, `**/*billing*`).

Two hits in different packages: pick the package the user is already in (`pwd`, open file, @-mention). Say so. Do not ask which package.

## 3. Neighbors

Implementation, test beside it, type or proto it imports. House style lives in siblings more than in README.

## 4. House files

`CLAUDE.md`, `.claude/`, ADRs, `docs/`, `.env.example`, CI, Makefile, package manifest, lockfile. Lockfile is the package manager. Do not ask npm vs pnpm vs yarn.

## 5. Git

`git log -S` and `git blame` for why it is this way. The commit message often beats asking the person next to you.

## 6. Web, third-party only

Vendor docs for an external API, CLI flag, or library error. Not for how this repo names things.

## Commands

Do not ask "how do I run tests / lint / dev / migrate":

1. `package.json` scripts, Makefile, `justfile`, `Taskfile`, `tox.ini`, `pyproject.toml`
2. `.github/workflows` or other CI
3. README only if those are empty

Then run the narrowest matching command.

## Stop

- One pattern: copy it.
- Two patterns: same-package wins. Write both candidates, keep the one a file supports, discard the other in one line. Do not ask.
- Nothing after a bounded look: assume the smallest change that compiles (additive, flag off, no delete).

On a red test or type error: one failure line, then retry. Do not ask if the failure is real.

Bounded look = one Grep or Glob + one neighbor or house file. Then decide.
