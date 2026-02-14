![Alt text describing the image](img/pl.png)
# PLForecast - Premier League Prediction Dashboard (v1)

A Monte Carlo simulation engine that predicts Premier League outcomes with interactive visualizations. Currently tracking the 2025-26 season with 20,000 simulations per run.

## Features

- **Title Probability** - Real-time chances for each team to win the league
- **Top 4 (UCL) Probability** - Champions League qualification odds
- **Relegation Battle** - Drop zone probabilities with full distribution
- **Expected Points Table** - Projected final standings with confidence intervals
- **Position Distribution Heatmap** - Probability of finishing in each league position
- **Team Deep Dive** - Detailed breakdown for any selected team
- **Smart Caching** - 24-hour cache with instant reload and force refresh

## Current Predictions (as of Feb 2026)

| Team | Title % | Top 4 % | Relegation % | Exp Points |
|------|---------|---------|--------------|------------|
| Arsenal | 83.7% | 99.9% | 0.0% | 77.5 |
| Man City | 9.2% | 95.6% | 0.0% | 70.0 |
| Aston Villa | 6.6% | 92.4% | 0.0% | 69.3 |
| *... full table in dashboard* | | | | |

## Tech Stack

- **Frontend**: Streamlit + Plotly
- **Backend**: Python (pandas, numpy)
- **Simulation**: Monte Carlo (20k runs)
- **Rating System**: ELO-based with home advantage
- **Caching**: JSON-based with metadata validation
- **Data Sources**: [football-data.co.uk](https://www.football-data.co.uk/englandm.php), BBC Sport

### Project Structure:
    ./
    ├── cache/   #auto generated cache
    │   ├── elo_ratings_2526.csv
    │   ├── latest_simulations.json
    ├── data/
    │   ├── bbc_raw.html
    │   ├── EO_2526_raw.json   #json file
    │   ├── E0_2526.csv
    │   ├── elo_ratings_2526.csv    #elo ratings
    │   ├── power_rankings_2526.csv   #elo ratings sorted
    │   ├── remaining_fixtures2526.csv   #remaining fixtures in 25-26 season
    │   ├── simulation_results_2526.csv   #results from monte-carlo simulation
    │   └── summary_table2526.csv
    ├── viz/
    │   ├── match-level-eda.ipynb
    │   ├── table-level-eda.ipynb
    │   ├── mle.py   #.py file copy of match-level-eda.ipynb to import draw-rate variable
    │   ├── power-rankings-viz.ipynb
    │   ├── betting-odds-analysis.ipynb   #currently empty, will revisit in v2
    │   └── README.md   #readme for more details about data EDA and visualization
    ├── src/
    │   ├── config.py
    │   ├── elo.py #generate elo's
    │   ├── elo_run.py #generates elo's
    │   ├── fetch_data.py   #gets data from website
    │   ├── cache_utils.py   #caches data
    │   ├── pipeline.py.   #define simulation pipeline (parameters, etc.)
    │   ├── simulation.py   #contains details about running the monte-carlo simulations (main logic here)
    │   ├── table.py    #defines function for updating our simulated league table
    │   ├── remaining_fixtures.py       #loads remaining fixtures
    │   ├── load_data.py    #loading season data from `EO_2526.csv`, power rankings, and current league table
    │   └── README.md   #readme for more details about `src`
    ├── app.py   #Main Streamlit Dashboard
    ├── run.py    #Entry point for simulations
    ├── cache_manager.py   #saving, loading, & managing cacheing of results
    ├── data_processor.py   #processes simulation results data for streamlit + plotly visualization
    ├── LICENSE
    ├── requirements.txt
    └── README.md

## Descriptions:
- All analysis notebooks are located in  `notebook-viz/`.
- Logic and data-fetching will be located in `src/`.

## How It Works

### 1. **ELO Rating System**
- Each team starts with a base ELO rating of 1500
- Ratings update after every match based on result and margin
- Home advantage factor built into calculations

### 2. **Monte Carlo Simulation**
- Takes current ELO ratings and remaining fixtures
- Simulates each match 20,000 times using probability distributions
- Updates league table after each simulated match
- Records final positions across all simulations

### 3. **Probability Calculations**
- **Title %**: Times team finishes 1st / total simulations
- **Top 4 %**: Times team finishes 1st-4th / total simulations
- **Relegation %**: Times team finishes 18th-20th / total simulations
- **Expected Points**: Average points across all simulations

### 4. **Caching Strategy**
- Results cached for 24 hours (configurable)
- Cache invalidated when new match data arrives
- Manual override with "Force Refresh" button

### Local Installation

```bash
# Clone repository
git clone https://github.com/yourusername/PLForecast.git
cd PLForecast

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py
```
## Future Enhancements in v2:
- Live data fetching via API (football-data.org)
- Automated nightly simulation runs
- Poisson model as alternative to ELO
- Betting odds integration with value detection
- Historical accuracy tracking
- Head-to-head match predictor
- Export functionality (PDF/CSV)
- Mobile-responsive design

---

### **NOTICE**:

This project uses football data for educational and demonstration purposes.

Important Disclaimers:
- This project is not affiliated with, endorsed by, or connected to the Premier League
- Club names, logos, and trademarks are property of their respective owners
- Predictions are based on statistical models and should not be used for betting
- Past performance DOES NOT guarantee future results!!

## Contact me:
Kevin Zhou - kevinz09302009@gmail.com

# Star this repo if you find it useful!
Last updated: February 2026