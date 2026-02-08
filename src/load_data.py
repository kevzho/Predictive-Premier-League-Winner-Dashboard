#translate raw data into interpretable format for analysis

import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")

REQUIRED_COLS = [
    "Date",
    "HomeTeam",
    "AwayTeam",
    "FTHG",
    "FTAG"
]

def load_season_df(season_code="2526", league="E0"):
    path = os.path.join(DATA_DIR, f"{league}_{season_code}.csv")
    df = pd.read_csv(path)

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = df[REQUIRED_COLS].copy()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

    return df

def split_played_future(df):
    played = df.dropna(subset=["FTHG", "FTAG"])
    future = df[df["FTHG"].isna() & df["FTAG"].isna()] #checking for rows with null full time hg and ag (indicating non-played status)
    return played, future
