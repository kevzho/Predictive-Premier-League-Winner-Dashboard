#fetches data remotely

import os
import pandas as pd
import requests

from datetime import datetime

#our data directory (place `data` next to this script)
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
# ensure the data directory exists so writing won't raise FileNotFoundError
os.makedirs(DATA_DIR, exist_ok=True)

''' For future use, possibly, if we were to scrape multiple seasons
def season_codes_candidates():
    # returns candidate season like '2526' for 2025-2026 
    now = datetime.utcnow() 
    year = now.year
    month = now.month
    
    if month >= 7: # season starts in Jul
        start = year % 100
        end = (year + 1) % 100
    else:
        start = (year - 1) % 100
        end = year % 100

'''
#gets the csv from football-data.co.uk for given season and league
def download_fdc_csv(season_code = "2526", league = "E0"):
    url = f"https://www.football-data.co.uk/mmz4281/{season_code}/{league}.csv"
    out = os.path.join(DATA_DIR, f"{league}_{season_code}.csv")
    
    print("Downloading: ", url)
    # set timeout to 10 seconds
    r = requests.get(url, timeout = 10)

    #If status code is not 200, print error (meaning that it was unsuccessful)
    if r.status_code != 200:
        print("Error: ", r.status_code)
        return 
    
    #exporting to output file
    with open(out, "wb") as f:
        f.write(r.content)
    
    print("Saved to: ", out)

download_fdc_csv("2526", "E0") #downloading 25-26 premier league data
