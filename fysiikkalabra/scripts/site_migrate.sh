#!/bin/sh
# Bring an open branch past work queue 0g PR 3 (the committed fysiikkalabra/site/ is gone from main).
# Run it in the branch's checkout, from anywhere inside it: it merges origin/main, accepts the deletion of
# fysiikkalabra/site/ (the branch's own site/ changes are dropped; CI builds the site, and site/ is not part of the
# content hash, so no rebuild and no new review is needed) and commits. Nothing is pushed.
set -e
cd "$(git rev-parse --show-toplevel)"
git fetch -q origin main
git merge origin/main || true                         # a modify/delete conflict on site/ files is expected
git rm -rq --cached --ignore-unmatch fysiikkalabra/site
if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
  echo "site_migrate: conflicts outside fysiikkalabra/site/ remain; fix them and commit:"; git diff --name-only --diff-filter=U; exit 1
fi
git commit -qm "Merge main: fysiikkalabra/site/ is no longer committed (work queue 0g PR 3)" 2>/dev/null || true
echo "site_migrate: done; tracked site files left: $(git ls-files fysiikkalabra/site | wc -l)"
