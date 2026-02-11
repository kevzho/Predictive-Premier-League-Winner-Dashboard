![Alt text describing the image](img/pl.png)
# PLForecast - Premier League Prediction Dashboard (WIP)

- Predicts the probability that each Premier League team will win the league
- Updates live using match results / standings
- Visualizes model outputs (e.g., probabilities, rankings, expected points)
- Uses machine learning or Monte-Carlo simulation
- Runs locally or deploys via Streamlit Cloud

### Sources: 
1. https://www.football-data.co.uk/englandm.php
2. https://www.bbc.com/sport/football/premier-league/table


### Data that was collected:
#### From each match:
- Home team, Away team
- Score
- xG (Expected Goals)
- Possession, shots, cards
- Match date
- (Optional, will maybe include) Betting odds

#### From each team: 
- Current standings
- Form (Last 5 wins)
- SPI Standings (If we can access)


### Schema:
    ./
    ├── data/
    │   ├── bbc_raw.html
    │   ├── EO_2526_raw.json                 #json file
    │   ├── E0_2526.csv
    │   ├── results_25-26.csv
    │   ├── power_rankings_2526.csv
    │   ├── elo_ratings_2526.csv
    │   └── summary_table2526.csv
    ├── notebook-viz/
    │   ├── match-level-eda.ipynb
    │   ├── table-level-eda.ipynb
    │   ├── power-rankings-viz.ipynb
    │   ├── betting-odds-analysis.ipynb
    │   └── README.md                       #readme for data EDA and visualization
    ├── output/
    ├── src/
    │   ├── config.py
    │   ├── elo.py                          #generate elo's
    │   ├── elo_run.py                      #generates elo's
    │   ├── fetch_data.py
    │   ├── cache_utils.py                  #caches data
    │   ├── pipeline.py                     #define simulation pipeline (parameters, etc.)
    │   ├── simulation.py                   #contains details about running the monte-carlo simulations (main logic here)
    │   ├── table.py                        #defines function for updating our simulated league table
    │   └── load_data.py
    ├── app.py
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── run.py                              #main entry point

#### Descriptions:
- All analysis notebooks are located in  `notebook-viz/`.
- Logic and data-fetching will be located in `src/`.

---

### **NOTICE**:

This project uses football data for educational and demonstration purposes.

Important Disclaimers:
- This project is not affiliated with, endorsed by, or connected to the Premier League
- Club names, logos, and trademarks are property of their respective owners
- Predictions are based on statistical models and should not be used for betting
