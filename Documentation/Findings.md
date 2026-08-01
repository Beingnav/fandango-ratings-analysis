# Findings

Full methodology: [`Methodology.md`](Methodology.md). Column definitions: [`Data_Dictionary.md`](Data_Dictionary.md).
Charts referenced below are in [`../Dashboard_Screenshots/`](../Dashboard_Screenshots).

## 1. Fandango rounds its displayed rating up

Across the 435 reviewed films, the displayed `STARS` value is **0.21 stars higher on
average** than the true underlying `RATING`. The gap is one-directional — displayed
ratings are pushed up, never down — and is visible in the KDE comparison
([`02_KDE_Comparison.png`](../Dashboard_Screenshots/02_KDE_Comparison.png)): the
"Displayed Stars" curve sits shifted to the right of "True Rating."

The largest single-film gap is *Turbo Kid (2015)*, displayed at 5.0 stars against a
true rating of 4.0 — though with only 2 votes, that one film isn't representative on
its own.

## 2. The displayed-star distribution skews high

[`01_Ratings_Distribution.png`](../Dashboard_Screenshots/01_Ratings_Distribution.png)
shows 87.8% of reviewed films (382 of 435) display 3.5 stars or higher, and the
distribution is heavily left-skewed — only 8 films display below 3.0 stars. A platform
with no bias would be expected to show a wider, more centered spread.

## 3. Fandango rates higher than every other platform

Averaged across the 145 films present on all platforms
([`06_Final_Insights.png`](../Dashboard_Screenshots/06_Final_Insights.png)):

| Platform | Mean rating (0–5) |
|---|---|
| **Fandango (displayed stars)** | **4.09** |
| Fandango (true rating) | 3.84 |
| IMDb | 3.36 |
| Metacritic (users) | 3.25 |
| Rotten Tomatoes (users) | 3.18 |
| Rotten Tomatoes (critics) | 3.03 |
| Metacritic (critics) | 2.93 |

Fandango's displayed stars average **1.15 points higher** than Metacritic critics —
the platform with no ticket-sales incentive and the most independent editorial voice
in the dataset.

## 4. Fandango barely tracks Rotten Tomatoes critics

The regression in [`05_Regression.png`](../Dashboard_Screenshots/05_Regression.png)
compares Fandango's displayed stars to RT's normalized critic score. The fitted line
sits well above the "perfect agreement" diagonal across the *entire* range — even
films RT critics rated near 0 still show 3.5–4 stars on Fandango. The correlation
between the two is just **0.29**
([`03_Correlation.png`](../Dashboard_Screenshots/03_Correlation.png)), the weakest
pairing in the whole matrix. By contrast, RT critics and Metacritic critics — two
independent critic sources — correlate at **0.96**.

## 5. Independent sources agree with each other; Fandango is the outlier

The correlation matrix makes the pattern explicit: every non-Fandango platform
correlates with every other non-Fandango platform at 0.68 or higher. Fandango's two
columns are the only ones that drop as low as 0.17–0.33 against another platform
(both against Metacritic critics). Fandango's own `STARS` and `RATING` correlate with
each other at 0.96, confirming the display gap is a consistent rounding-up rule, not
a data quality issue.

## 6. Worst-reviewed films still display high on Fandango

Films with the lowest Rotten Tomatoes critic scores — e.g. *Paul Blart: Mall Cop 2*
(RT critics: 0.25/5) and *Taken 3* (RT critics: 0.45/5, Fandango: 4.5/5) — still
display 3–4.5 stars on Fandango, the same pattern FiveThirtyEight's original 2015
analysis found.

## Bottom line

The 2015 snapshot supports FiveThirtyEight's original conclusion: Fandango's displayed
ratings were **inflated relative to Fandango's own underlying data and relative to
every other rating platform in the dataset**, in a direction that would be expected to
increase ticket sales. This is a single time-period snapshot (Aug. 2015) and does not
speak to Fandango's current rating practices.
