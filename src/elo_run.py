from elo import compute_table_state, save_elo, save_elo_csv
import pandas as pd
import os

df = pd.read_csv("data/E0_2526.csv")

ratings, table = compute_table_state(df) #defaulted to k=20, home_adv=80, base_rating=1500

elo_df = pd.DataFrame(list(ratings.items()), columns=["Team", "EloRating"])

#sort values by elo (descending) to get current league table order, or even just power rankings
power_rankings_df = elo_df.sort_values("EloRating", ascending=False).reset_index(drop=True)
power_rankings_df["Rank "] = power_rankings_df.index + 1

os.makedirs("data", exist_ok=True)

elo_df.to_csv("data/elo_ratings_2526.csv", index=False)
power_rankings_df.to_csv("data/power_rankings_2526.csv", index=False)
save_elo(ratings, season_code="2526")

print(f"Elo ratings saved to /data folder.")