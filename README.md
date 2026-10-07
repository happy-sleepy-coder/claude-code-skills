# Claude Code skills

Skills for Claude Code. Copy a skill folder into `.claude/skills/` in a project, or into `~/.claude/skills/` to use it everywhere.

This repo has a [CLAUDE.md](CLAUDE.md). In this repo, Claude Code should use `plain-docs` for every project doc, and `self-reasoning` before asking the user a question.

## Skills

| Skill | What it does |
| --- | --- |
| [java-debug](skills/java-debug) | Debug a red Maven or Gradle build, a failing test, or a JVM stack trace. Reproduce, fix the cause, re-run the same command. |
| [plain-docs](skills/plain-docs) | Write or rewrite docs and technical design documents (TDD) in short plain English from real findings. |
| [self-reasoning](skills/self-reasoning) | Look first, ask last. Search the repo, git, docs, and public sources before asking the user. A PreToolUse hook denies `AskUserQuestion` without an evidence line. |

## Install

```bash
git clone https://github.com/ajarhserus/claude-code-skills.git
mkdir -p ~/.claude/skills
cp -R claude-code-skills/skills/java-debug ~/.claude/skills/java-debug
cp -R claude-code-skills/skills/plain-docs ~/.claude/skills/plain-docs
cp -R claude-code-skills/skills/self-reasoning ~/.claude/skills/self-reasoning
```

One project only:

```bash
mkdir -p .claude/skills
cp -R skills/java-debug .claude/skills/java-debug
cp -R skills/plain-docs .claude/skills/plain-docs
cp -R skills/self-reasoning .claude/skills/self-reasoning
```

Already installed? Copy the folder again after a pull. Claude Code reads skills at session start.

Then ask for a README, runbook, ADR, TDD, `/plain-docs`, `/self-reasoning`, or `/java-debug`.

`self-reasoning` only arms its hook after the skill is invoked. To deny bare questions every session, add the settings block in [skills/self-reasoning/references/hooks.md](skills/self-reasoning/references/hooks.md).

To force a skill in another repo, copy the matching block in [CLAUDE.md](CLAUDE.md) into that repo's `CLAUDE.md`.
