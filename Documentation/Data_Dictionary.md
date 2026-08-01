# Data Dictionary

Two source files live in [`../Data/`](../Data). Both were originally collected by
FiveThirtyEight for [*Be Suspicious Of Online Movie Ratings, Especially Fandango's*](http://fivethirtyeight.com/features/fandango-movies-ratings/)
(Walt Hickey, 2015) and pulled from Fandango on **August 24, 2015**.

## `fandango_scrape.csv`

Every film Fandango showed on its site at the time of the pull, regardless of vote count.

| Column | Type | Description |
|---|---|---|
| `FILM` | string | Movie title, including release year, e.g. `"Fifty Shades of Grey (2015)"` |
| `STARS` | float | Star rating **displayed** on Fandango.com (rounded to the nearest half star) |
| `RATING` | float | The true average rating pulled from the page's HTML, before display rounding |
| `VOTES` | int | Number of user reviews on Fandango at the time of the pull |

**Rows:** 504 | **Rows with ≥ 1 vote:** 435

## `all_sites_scores.csv`

Every film that has a Rotten Tomatoes rating, an RT user rating, a Metacritic score, a
Metacritic user score, an IMDb score, **and** at least 30 fan reviews on Fandango.

| Column | Type | Description |
|---|---|---|
| `FILM` | string | Movie title, including release year |
| `RottenTomatoes` | int (0–100) | Rotten Tomatoes Tomatometer (critics) score |
| `RottenTomatoes_User` | int (0–100) | Rotten Tomatoes audience (user) score |
| `Metacritic` | int (0–100) | Metacritic critic score |
| `Metacritic_User` | float (0–10) | Metacritic user score |
| `IMDB` | float (0–10) | IMDb user score |
| `Metacritic_user_vote_count` | int | Number of user votes behind the Metacritic user score |
| `IMDB_user_vote_count` | int | Number of user votes behind the IMDb score |

**Rows:** 146

## Derived / normalized columns

Created in the notebook (see [`Methodology.md`](Methodology.md)) so every platform is
comparable on Fandango's 0–5 star scale:

| Column | Formula | Range |
|---|---|---|
| `RT_norm` | `RottenTomatoes / 20` | 0–5 |
| `RT_user_norm` | `RottenTomatoes_User / 20` | 0–5 |
| `Meta_norm` | `Metacritic / 20` | 0–5 |
| `Meta_user_norm` | `Metacritic_User / 2` | 0–5 |
| `IMDB_norm` | `IMDB / 2` | 0–5 |
| `Fandango_STARS_norm` | `STARS` (already 0–5) | 0–5 |
| `Fandango_RATING_norm` | `RATING` (already 0–5) | 0–5 |
| `STARS_DIFF` | `STARS - RATING` | can be negative |

`combined_df` is the inner merge of both files on `FILM` (**145 rows** — one title in
`all_sites_scores.csv` has no matching entry in `fandango_scrape.csv`).
