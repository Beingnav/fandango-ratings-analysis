# Contributing

Thanks for your interest in improving this project. It's a small, self-contained data
analysis, so contributions are kept lightweight.

## Getting set up

```bash
git clone https://github.com/Beingnav/fandango-ratings-analysis.git
cd fandango-ratings-analysis
pip install -r requirements.txt
jupyter notebook Notebook/Fandango_Ratings_Analysis.ipynb
```

## Ways to contribute

- **Fix a bug or improve a chart** — open a pull request directly.
- **Extend the analysis** (new platform, newer dataset, additional visualization) —
  open an issue first describing what you'd like to add, so it can be discussed before
  you invest time in it.
- **Improve documentation** — typo fixes and clarity improvements to `README.md` or
  anything in `Documentation/` are always welcome.

## Guidelines

- Keep new analysis code inside the notebook, and put anything reused across multiple
  cells (loading, normalizing, styling) into [`Scripts/helper_functions.py`](Scripts/helper_functions.py)
  instead of duplicating it.
- If you add or change a chart, regenerate its PNG in `Dashboard_Screenshots/` and make
  sure the notebook still runs top to bottom without errors:
  ```bash
  jupyter nbconvert --to notebook --execute --inplace Notebook/Fandango_Ratings_Analysis.ipynb
  ```
- If you add or rename a data column, update [`Documentation/Data_Dictionary.md`](Documentation/Data_Dictionary.md)
  to match.
- Keep pull requests focused — one change per PR is easier to review than several
  unrelated ones bundled together.

## Reporting issues

Open a GitHub issue with a clear description of the problem (or idea) and, if it's a
bug, the steps to reproduce it.
