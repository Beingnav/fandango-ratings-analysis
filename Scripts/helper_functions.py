"""Shared data loading, normalization, and plotting-style helpers for the
Fandango ratings analysis notebook."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "Data"
SCREENSHOTS_DIR = REPO_ROOT / "Dashboard_Screenshots"

# Categorical palette (fixed, non-cycled order) shared by every chart in the project.
COLORS = {
    "blue": "#2a78d6",
    "orange": "#eb6834",
    "aqua": "#1baf7a",
    "yellow": "#eda100",
    "magenta": "#e87ba4",
    "green": "#008300",
    "violet": "#4a3aa7",
    "red": "#e34948",
}

SURFACE = "#fcfcfb"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRIDLINE = "#e1e0d9"


def set_plot_style():
    """Apply a consistent, minimal look to every chart in the project."""
    sns.set_theme(style="white")
    plt.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRIDLINE,
        "axes.labelcolor": INK_SECONDARY,
        "text.color": INK_PRIMARY,
        "xtick.color": INK_MUTED,
        "ytick.color": INK_MUTED,
        "grid.color": GRIDLINE,
        "axes.grid": True,
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.family": "sans-serif",
        "font.size": 11,
    })


def load_data(data_dir: Path = DATA_DIR):
    """Load the two raw source CSVs."""
    fandango = pd.read_csv(data_dir / "fandango_scrape.csv")
    all_sites = pd.read_csv(data_dir / "all_sites_scores.csv")
    return fandango, all_sites


def normalize_scores(fandango: pd.DataFrame, all_sites: pd.DataFrame):
    """Merge the two datasets and rescale every rating onto Fandango's 0-5 star
    range so platforms become comparable. Returns (combined_df, norm_scores_df).
    """
    combined = fandango.merge(all_sites, on="FILM", how="inner")

    combined["RT_norm"] = combined["RottenTomatoes"] / 20
    combined["RT_user_norm"] = combined["RottenTomatoes_User"] / 20
    combined["Meta_norm"] = combined["Metacritic"] / 20
    combined["Meta_user_norm"] = combined["Metacritic_User"] / 2
    combined["IMDB_norm"] = combined["IMDB"] / 2
    combined["Fandango_STARS_norm"] = combined["STARS"]
    combined["Fandango_RATING_norm"] = combined["RATING"]

    norm_scores = combined[[
        "FILM",
        "Fandango_STARS_norm",
        "Fandango_RATING_norm",
        "RT_norm",
        "RT_user_norm",
        "Meta_norm",
        "Meta_user_norm",
        "IMDB_norm",
    ]]
    return combined, norm_scores


def save_dashboard_figure(fig, filename: str, screenshots_dir: Path = SCREENSHOTS_DIR):
    """Save a figure into Dashboard_Screenshots/ at a consistent size/DPI."""
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(screenshots_dir / filename, dpi=150, facecolor=SURFACE, bbox_inches="tight")
