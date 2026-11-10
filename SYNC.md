# GitHub sync and continuation

Intended remote: `https://github.com/Sumitmishra-09/prep.git`.

## Repository connection

`origin` is configured for the user-supplied repository above. On 2026-11-10, the initial filesystem/network restrictions were lifted, GitHub access succeeded, and the remote advertised no existing refs before the first push. Ordinary session syncing can now use Git. Always verify each push; permission to sync does not prove a push succeeded.

To inspect synchronization:

```powershell
git status --short --branch
git remote -v
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Local and remote commit hashes should match after a successful push, with a clean working tree. A local commit alone is not a GitHub backup. If a push is rejected, preserve both histories and inspect the divergence; do not force push or hard reset.

## Continue on another laptop

After the first successful push:

```powershell
git clone https://github.com/Sumitmishra-09/prep.git
cd prep
```

Open Claude Code or Codex in that folder and say:

> Read the instructor instructions and progress/state.json. Resume the guided lesson in chat. Explain missing concepts and help me reason through one question at a time.

The repository files carry the learning state; chat history is not required. Python is needed only for the validation helper, and Java/Maven/database tools are needed only when starting their corresponding labs.

The visual teaching skills travel with the repository in `.agents/skills/`, with Claude entry points in `.claude/skills/`. Both agent instruction files route to the canonical skills even if automatic discovery differs by client. See [skill sources and setup](research/SKILLS.md); there is no separate global installation step for these bundled skills.

## Routine session sync

Before starting, inspect `git status`. With a clean working tree and an established upstream, use `git pull --ff-only`. If another laptop has created divergent commits, fetch and inspect before merging; do not discard either session's progress. Avoid simultaneous study sessions on multiple laptops.

At session end, the instructor updates state and tracker, runs validation, reviews the diff, stages only intended files, commits, and runs `git push`. Report failures and leave an actionable checkpoint. There is no autonomous background sync or reminder service.

Keep credentials, customer/employer data, and private documents out of Git. The `private/` folder is ignored for optional local material; it will not sync to the other laptop.
