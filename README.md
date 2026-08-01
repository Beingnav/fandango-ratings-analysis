![Python](https://img.shields.io/badge/Python-3.x-blue)
![NumPy](https://img.shields.io/badge/NumPy-used-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-used-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-used-red)
![Seaborn](https://img.shields.io/badge/Seaborn-used-blueviolet)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# Fandango Movie Ratings Analysis 🎬

**Does Fandango inflate the star ratings it displays to sell more movie tickets?**

This project reproduces and extends the analysis behind FiveThirtyEight's
[*Be Suspicious Of Online Movie Ratings, Especially Fandango's*](http://fivethirtyeight.com/features/fandango-movies-ratings/)
(2015). It compares Fandango's **displayed** star ratings against Fandango's own
**true** underlying rating, and against Rotten Tomatoes, Metacritic, and IMDb, to check
for a ratings bias.

**Short answer: yes.** In the 2015 dataset, Fandango's displayed stars average higher
than every other platform — including its own true rating. See
[Findings](#key-findings) below, or the full write-up in
[`Documentation/Findings.md`](Documentation/Findings.md).

## Objective

- Compare rating distributions across platforms
- Normalize ratings onto a common 0–5 scale
- Visualize the differences with distributions, correlation, and regression

## Repository Structure

```
Fandango-Ratings-Analysis/
│
├── Data/
│   ├── all_sites_scores.csv
│   └── fandango_scrape.csv
│
├── Notebook/
│   └── Fandango_Ratings_Analysis.ipynb
│
├── Dashboard_Screenshots/
│   ├── 01_Ratings_Distribution.png
│   ├── 02_KDE_Comparison.png
│   ├── 03_Correlation.png
│   ├── 04_Scatter_Plot.png
│   ├── 05_Regression.png
│   └── 06_Final_Insights.png
│
├── Documentation/
│   ├── Project_Report.pdf
│   ├── Findings.md
│   ├── Data_Dictionary.md
│   └── Methodology.md
│
├── Scripts/
│   └── helper_functions.py
│
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
└── README.md
```

## Dashboard

| | |
|---|---|
| ![Ratings Distribution](Dashboard_Screenshots/01_Ratings_Distribution.png) | ![KDE Comparison](Dashboard_Screenshots/02_KDE_Comparison.png) |
| **Distribution of displayed star ratings** — heavily skewed toward 4–5 stars | **Displayed stars vs. true rating** — displayed values shifted higher |
| ![Correlation](Dashboard_Screenshots/03_Correlation.png) | ![Scatter Plot](Dashboard_Screenshots/04_Scatter_Plot.png) |
| **Cross-platform correlation** — Fandango is the outlier | **Rating vs. popularity** — votes vs. true rating |
| ![Regression](Dashboard_Screenshots/05_Regression.png) | ![Final Insights](Dashboard_Screenshots/06_Final_Insights.png) |
| **Fandango vs. RT critics** — far above the agreement line | **Mean rating by platform** — Fandango ranks highest |

## Key Findings

- Fandango's **displayed** stars average **0.21 stars higher** than its own **true**
  rating, across 435 reviewed films.
- **87.8%** of reviewed films display 3.5 stars or higher; almost none display below 3.0.
- Averaged across the 145 films shared by every platform, Fandango's displayed stars
  (**4.09/5**) rank highest of any platform — **1.15 points above Metacritic critics**
  (2.93/5), the most independent source in the dataset.
- Fandango's displayed stars correlate with Rotten Tomatoes critic scores at just
  **0.29** — the weakest pairing in the dataset. Two independent critic sources (RT
  critics vs. Metacritic critics) correlate at **0.96**.
- Films with very low critic scores (e.g. *Taken 3*, RT critics 0.45/5) still display
  high Fandango stars (4.5/5).

Full write-up: [`Documentation/Findings.md`](Documentation/Findings.md) · Methodology:
[`Documentation/Methodology.md`](Documentation/Methodology.md) · Report:
[`Documentation/Project_Report.pdf`](Documentation/Project_Report.pdf)

## Data

- [`Data/fandango_scrape.csv`](Data/fandango_scrape.csv) — Fandango's displayed stars,
  true rating, and vote count for 504 films
- [`Data/all_sites_scores.csv`](Data/all_sites_scores.csv) — Rotten Tomatoes,
  Metacritic, and IMDb scores for 146 films

Column definitions: [`Documentation/Data_Dictionary.md`](Documentation/Data_Dictionary.md)

## Tools & Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## How to Run

1. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/Beingnav/fandango-ratings-analysis.git
   cd fandango-ratings-analysis
   pip install -r requirements.txt
   ```

2. Open the notebook:
   ```bash
   jupyter notebook Notebook/Fandango_Ratings_Analysis.ipynb
   ```

Shared data loading, normalization, and plotting-style logic lives in
[`Scripts/helper_functions.py`](Scripts/helper_functions.py) and is imported directly
by the notebook.

## Contributing

Contributions are welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

## License

Released under the [MIT License](LICENSE).
