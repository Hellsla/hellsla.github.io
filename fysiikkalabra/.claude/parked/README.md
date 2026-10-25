# Parked agents and commands

These produce nothing that reaches the site yet: `build.py` renders no news page, `tips/` and `newsletter/`
are empty, and no glossary page exists. They are parked here, out of Claude Code's agent and command
discovery, until the lesson pipeline is stable and the site has a place for their output.

To bring one back: move it to `.claude/agents/` or `.claude/commands/`, then add the build step that
renders its output (a news page and an "Ajankohtaista" box on the tagged lesson for `news-agent`;
a glossary page for `glossary-curator`), and re-enable the scheduled task in `SCHEDULED-TASKS.md`.
