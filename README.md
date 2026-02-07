# Dashboard Creation

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
  project-root/
├─ data/ # Raw and processed data
│ ├─ bbc_raw.html
│ ├─ E0_2526.csv
│ ├─ results_25-26.csv
│ └─ summary_table2526.csv
├─ notebooks/ # Analysis and EDA notebooks
│ ├─ match-level-eda.ipynb
│ ├─ table-level-eda.ipynb
│ └─ betting-odds-analysis.ipynb
├─ output/ # Generated outputs (plots, tables, predictions)
├─ app.py # Main application or runner script
├─ elo.py # ELO rating calculations
├─ fetch_data.py # Data scraping/parsing utilities
├─ simulate.py # Simulation scripts
├─ LICENSE
├─ README.md
└─ requirements.txt

    .
    ├── build                   # Compiled files (alternatively `dist`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── test                    # Automated tests (alternatively `spec` or `tests`)
    ├── tools                   # Tools and utilities
    ├── LICENSE
    └── README.md

#### Descriptions:
- All analysis notebooks are located in the `notebooks/` subfolder.
