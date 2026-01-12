#fetches data remotely

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

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

def get_prem_table(season = "2526"):
    """Get Premier League table from Google search results"""
    #bbc prem table
    url = "https://www.bbc.com/sport/football/premier-league/table"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print(f"Fetching from BBC Sport: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        #debug
        print(f"Status code: {response.status_code}")
        
        #save raw html for debugging
        '''
        debug_file = os.path.join(DATA_DIR, "bbc_raw.html")
        with open(debug_file, 'w', encoding='utf-8') as f:
            f.write(response.text[:5000])  # Save first 5000 chars
        print(f"Raw HTML saved to: {debug_file}")
        '''

        #try to parse with pandas first
        try:
            # Try lxml first (faster)
            tables = pd.read_html(response.text, flavor='lxml')
        except:
            #html5lib falback (download both if needed)
            try:
                tables = pd.read_html(response.text, flavor='html5lib')
            except Exception as e:
                print(f"Failed to parse with lxml/html5lib: {e}")
                #try to parse without either
                tables = pd.read_html(response.text)
        
        # print(f"Found {len(tables)} tables.")
        
        if tables:
            #debug code to check for shape and columns to make sure
            #it's the right table

            '''
            for i, table in enumerate(tables):
                print(f"\nTable {i} shape: {table.shape}")
                print(f"Table {i} columns: {table.columns.tolist()}")
                print(f"First few rows:\n{table.head(3)}")
                print("-" * 50)
            '''
            
            df = tables[0] if len(tables[0]) > 5 else tables[1]
            df = df.copy()
            
            #no multi-index columns
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = ['_'.join(col).strip() for col in df.columns]
            df.columns = [str(col).strip() for col in df.columns]
            
            #export
            out = os.path.join(DATA_DIR, f"{season}-prem-table-bbc.csv")
            df.to_csv(out, index=False)
            print(f"✓ Saved to: {out}")
            print(f"Final shape: {df.shape}")
            
            return df
        
        else:
            print("No tables found")
            return None

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return None

download_fdc_csv("2526", "E0") #downloading 25-26 premier league data
get_prem_table("2526") #getting premier league table data