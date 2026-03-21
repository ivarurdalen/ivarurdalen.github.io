#!/usr/bin/env bash
# Fetch latest CV data, render the site, and stage results for commit
set -e

echo "Fetching CV data from Google Sheets..."
uv run python scripts/fetch_cv_data.py

echo "Clearing freeze cache..."
rm -rf _freeze/cv_ivar

echo "Rendering site..."
uv run quarto render

git add _freeze/ data/
echo "Done. Frozen outputs and data staged. Review with 'git diff --cached' then commit."
