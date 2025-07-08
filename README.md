# Ivar Soares Urdalen

My personal website where I write about topics related to finance and data engineering.

## Development Workflow

This site is developed using [Quarto](https://quarto.org/).
Make sure the [latest version](https://quarto.org/docs/download/) is installed.

To render (build) use the following command in the repo folder.

```bash
quarto render
```

To open the latest rendering open the project in a web browser:

```bash
firefox docs/index.html
```

The rendered site is stored in the `docs` folder.

This site uses the [alternative](https://quarto.org/docs/publishing/github-pages.html#render-to-docs)
to push the `docs` folder to the `main` branch of the GitHub repo.

Push the updated `docs` folder to GitHub to publish it to GitHub Pages.

```bash
git add docs
git commit -m "<message>"
git push
```

## Quarto Extensions

When using Quarto extensions they should be checked into the GitHub repo.

Extensions used in the project:

- https://github.com/quarto-ext/fontawesome
