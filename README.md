# Ivar Soares Urdalen

My personal website where I write about topics related to finance and data engineering.

## Prerequisites

- [Quarto](https://quarto.org/docs/download/) (latest version)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Setup

```bash
uv sync
```

## Development

Preview the site locally:

```bash
uv run quarto preview
```

## Publishing

The site is deployed to GitHub Pages via a GitHub Actions workflow that triggers on every push to `main`. The workflow builds the site and publishes it to the `gh-pages` branch.

R code outputs are cached locally using Quarto's [freeze](https://quarto.org/docs/projects/code-execution.html#freeze) feature. This means CI doesn't need to re-execute Python code — it uses the pre-computed results from the `_freeze/` directory.

**When you change `.qmd` files that contain Python code**, render locally and commit the frozen outputs:

```bash
./render.sh
git commit -m "your message"
git push
```

For changes to plain markdown `.qmd` files (no Python code), just commit and push — CI handles the rendering.

## Quarto Extensions

Extensions used in the project:

- https://github.com/quarto-ext/fontawesome
