# Methodology

## Question

Does Fandango display inflated star ratings compared to its own underlying data and
to other movie rating platforms — a pattern that would benefit Fandango, since it also
sells movie tickets?

## Data

See [`Data_Dictionary.md`](Data_Dictionary.md) for full column definitions. Both source
files were collected by FiveThirtyEight on August 24, 2015 and are used as-is, with no
re-scraping.

## Steps

1. **Load** `fandango_scrape.csv` and `all_sites_scores.csv` (`Scripts/helper_functions.py::load_data`).
2. **Filter to reviewed films.** 69 of 504 Fandango titles have zero votes; these are
   dropped before comparing `STARS` (displayed) against `RATING` (true), leaving 435
   films.
3. **Quantify the display gap.** `STARS_DIFF = STARS - RATING`, rounded to 2 decimals,
   computed per film.
4. **Merge platforms.** `fandango_scrape.csv` and `all_sites_scores.csv` are joined on
   `FILM` with an **inner** merge, keeping only the 145 films present in both — this is
   the only fair basis for a cross-platform comparison.
5. **Normalize every rating to a 0–5 scale** (`Scripts/helper_functions.py::normalize_scores`),
   since Rotten Tomatoes and Metacritic report out of 100, Metacritic's user score and
   IMDb report out of 10, and Fandango already reports out of 5:
   - `/ 20` for scores out of 100 (`RottenTomatoes`, `RottenTomatoes_User`, `Metacritic`)
   - `/ 2` for scores out of 10 (`Metacritic_User`, `IMDB`)
   - Fandango's `STARS` and `RATING` are left unchanged
6. **Compare distributions** with KDE plots, a correlation matrix, and mean ratings per
   platform, and check whether Fandango's regression line against Rotten Tomatoes
   critics sits above the "perfect agreement" diagonal.

All code is in [`../Notebook/Fandango_Ratings_Analysis.ipynb`](../Notebook/Fandango_Ratings_Analysis.ipynb),
built on reusable functions in [`../Scripts/helper_functions.py`](../Scripts/helper_functions.py).

## Caveats

- **Single snapshot, single year.** All data is from August 2015; findings describe
  Fandango's behavior at that point in time, not necessarily today.
- **Displayed-vs-true gap is small in aggregate but consistent.** The mean gap between
  `STARS` and `RATING` is about +0.21 stars — small per film, but it is a one-directional
  rounding-up bias, not noise.
- **RT critics vs. Metacritic critics correlate almost perfectly (0.96)**, which is a
  useful sanity check: independent critic scores agree with each other far more than
  either agrees with Fandango.
- **Zero-vote films are excluded** from the STARS-vs-RATING comparison since `RATING`
  is undefined without votes; this does not affect the cross-platform comparison, which
  uses the inner-merged 145-film set regardless of vote count.
