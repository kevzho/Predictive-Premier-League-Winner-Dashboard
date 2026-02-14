"""
Fixtures module for Premier League 2025-26 season.
Complete fixture list from Feb 18 - May 24, 2026.
"""

import pandas as pd
from pathlib import Path
import os

def get_all_fixtures():
    """Complete Premier League fixtures from Feb 18 - May 24, 2026 with actual kickoff times"""
    
    fixtures = [
        # ========================================
        # FEBRUARY 2026
        # ========================================
        
        # Wednesday, 18 February 2026
        ['Wolves', 'Arsenal', '2026-02-18', '15:00', 'EST'],
        
        # Saturday, 21 February 2026
        ['Aston Villa', 'Leeds', '2026-02-21', '10:00', 'EST'],
        ['Brentford', 'Brighton', '2026-02-21', '10:00', 'EST'],
        ['Chelsea', 'Burnley', '2026-02-21', '10:00', 'EST'],
        ['West Ham', 'AFC Bournemouth', '2026-02-21', '12:30', 'EST'],
        ['Man City', 'Newcastle', '2026-02-21', '15:00', 'EST'],
        
        # Sunday, 22 February 2026
        ['C Palace', 'Wolves', '2026-02-22', '09:00', 'EST'],
        ['Nottm Forest', 'Liverpool', '2026-02-22', '09:00', 'EST'],
        ['Sunderland', 'Fulham', '2026-02-22', '09:00', 'EST'],
        ['Spurs', 'Arsenal', '2026-02-22', '11:30', 'EST'],
        
        # Monday, 23 February 2026
        ['Everton', 'Man United', '2026-02-23', '15:00', 'EST'],
        
        # Friday, 27 February 2026
        ['Wolves', 'Aston Villa', '2026-02-27', '15:00', 'EST'],
        
        # Saturday, 28 February 2026
        ['AFC Bournemouth', 'Sunderland', '2026-02-28', '07:30', 'EST'],
        ['Burnley', 'Brentford', '2026-02-28', '10:00', 'EST'],
        ['Liverpool', 'West Ham', '2026-02-28', '10:00', 'EST'],
        ['Newcastle', 'Everton', '2026-02-28', '10:00', 'EST'],
        ['Leeds', 'Man City', '2026-02-28', '12:30', 'EST'],
        
        # ========================================
        # MARCH 2026
        # ========================================
        
        # Sunday, 1 March 2026
        ['Brighton', 'Nottm Forest', '2026-03-01', '09:00', 'EST'],
        ['Fulham', 'Spurs', '2026-03-01', '09:00', 'EST'],
        ['Man United', 'C Palace', '2026-03-01', '09:00', 'EST'],
        ['Arsenal', 'Chelsea', '2026-03-01', '11:30', 'EST'],
        
        # Tuesday, 3 March 2026
        ['AFC Bournemouth', 'Brentford', '2026-03-03', '14:30', 'EST'],
        ['Everton', 'Burnley', '2026-03-03', '14:30', 'EST'],
        ['Leeds', 'Sunderland', '2026-03-03', '14:30', 'EST'],
        ['Wolves', 'Liverpool', '2026-03-03', '15:15', 'EST'],
        
        # Wednesday, 4 March 2026
        ['Aston Villa', 'Chelsea', '2026-03-04', '14:30', 'EST'],
        ['Brighton', 'Arsenal', '2026-03-04', '14:30', 'EST'],
        ['Fulham', 'West Ham', '2026-03-04', '14:30', 'EST'],
        ['Man City', 'Nottm Forest', '2026-03-04', '14:30', 'EST'],
        ['Newcastle', 'Man United', '2026-03-04', '15:15', 'EST'],
        
        # Thursday, 5 March 2026
        ['Spurs', 'C Palace', '2026-03-05', '15:00', 'EST'],
        
        # Saturday, 14 March 2026
        ['West Ham', 'Man City', '2026-03-14', '08:30', 'EDT'],
        ['Burnley', 'AFC Bournemouth', '2026-03-14', '11:00', 'EDT'],
        ['C Palace', 'Leeds', '2026-03-14', '11:00', 'EDT'],
        ['Nottm Forest', 'Fulham', '2026-03-14', '11:00', 'EDT'],
        ['Sunderland', 'Brighton', '2026-03-14', '11:00', 'EDT'],
        ['Chelsea', 'Newcastle', '2026-03-14', '13:30', 'EDT'],
        
        # Sunday, 15 March 2026
        ['Arsenal', 'Everton', '2026-03-15', '10:00', 'EDT'],
        ['Man United', 'Aston Villa', '2026-03-15', '10:00', 'EDT'],
        ['Liverpool', 'Spurs', '2026-03-15', '12:30', 'EDT'],
        
        # Monday, 16 March 2026
        ['Brentford', 'Wolves', '2026-03-16', '16:00', 'EDT'],
        
        # Friday, 20 March 2026
        ['AFC Bournemouth', 'Man United', '2026-03-20', '16:00', 'EDT'],
        
        # Saturday, 21 March 2026
        ['Brighton', 'Liverpool', '2026-03-21', '08:30', 'EDT'],
        ['Fulham', 'Burnley', '2026-03-21', '11:00', 'EDT'],
        ['Everton', 'Chelsea', '2026-03-21', '13:30', 'EDT'],
        ['Leeds', 'Brentford', '2026-03-21', '16:00', 'EDT'],
        
        # Sunday, 22 March 2026
        ['Newcastle', 'Sunderland', '2026-03-22', '08:00', 'EDT'],
        ['Aston Villa', 'West Ham', '2026-03-22', '10:15', 'EDT'],
        ['Spurs', 'Nottm Forest', '2026-03-22', '10:15', 'EDT'],
        
        # ========================================
        # APRIL 2026
        # ========================================
        
        # Saturday, 11 April 2026
        ['Arsenal', 'AFC Bournemouth', '2026-04-11', '10:00', 'EDT'],
        ['Brentford', 'Everton', '2026-04-11', '10:00', 'EDT'],
        ['Burnley', 'Brighton', '2026-04-11', '10:00', 'EDT'],
        ['C Palace', 'Newcastle', '2026-04-11', '10:00', 'EDT'],
        ['Chelsea', 'Man City', '2026-04-11', '10:00', 'EDT'],
        ['Liverpool', 'Fulham', '2026-04-11', '10:00', 'EDT'],
        ['Man United', 'Leeds', '2026-04-11', '10:00', 'EDT'],
        ['Nottm Forest', 'Aston Villa', '2026-04-11', '10:00', 'EDT'],
        ['Sunderland', 'Spurs', '2026-04-11', '10:00', 'EDT'],
        ['West Ham', 'Wolves', '2026-04-11', '10:00', 'EDT'],
        
        # Saturday, 18 April 2026
        ['Aston Villa', 'Sunderland', '2026-04-18', '10:00', 'EDT'],
        ['Brentford', 'Fulham', '2026-04-18', '10:00', 'EDT'],
        ['C Palace', 'West Ham', '2026-04-18', '10:00', 'EDT'],
        ['Chelsea', 'Man United', '2026-04-18', '10:00', 'EDT'],
        ['Everton', 'Liverpool', '2026-04-18', '10:00', 'EDT'],
        ['Leeds', 'Wolves', '2026-04-18', '10:00', 'EDT'],
        ['Man City', 'Arsenal', '2026-04-18', '10:00', 'EDT'],
        ['Newcastle', 'AFC Bournemouth', '2026-04-18', '10:00', 'EDT'],
        ['Nottm Forest', 'Burnley', '2026-04-18', '10:00', 'EDT'],
        ['Spurs', 'Brighton', '2026-04-18', '10:00', 'EDT'],
        
        # Saturday, 25 April 2026
        ['AFC Bournemouth', 'Leeds', '2026-04-25', '10:00', 'EDT'],
        ['Arsenal', 'Newcastle', '2026-04-25', '10:00', 'EDT'],
        ['Brighton', 'Chelsea', '2026-04-25', '10:00', 'EDT'],
        ['Burnley', 'Man City', '2026-04-25', '10:00', 'EDT'],
        ['Fulham', 'Aston Villa', '2026-04-25', '10:00', 'EDT'],
        ['Liverpool', 'C Palace', '2026-04-25', '10:00', 'EDT'],
        ['Man United', 'Brentford', '2026-04-25', '10:00', 'EDT'],
        ['Sunderland', 'Nottm Forest', '2026-04-25', '10:00', 'EDT'],
        ['West Ham', 'Everton', '2026-04-25', '10:00', 'EDT'],
        ['Wolves', 'Spurs', '2026-04-25', '10:00', 'EDT'],
        
        # ========================================
        # MAY 2026
        # ========================================
        
        # Saturday, 2 May 2026
        ['AFC Bournemouth', 'C Palace', '2026-05-02', '10:00', 'EDT'],
        ['Arsenal', 'Fulham', '2026-05-02', '10:00', 'EDT'],
        ['Aston Villa', 'Spurs', '2026-05-02', '10:00', 'EDT'],
        ['Brentford', 'West Ham', '2026-05-02', '10:00', 'EDT'],
        ['Chelsea', 'Nottm Forest', '2026-05-02', '10:00', 'EDT'],
        ['Everton', 'Man City', '2026-05-02', '10:00', 'EDT'],
        ['Leeds', 'Burnley', '2026-05-02', '10:00', 'EDT'],
        ['Man United', 'Liverpool', '2026-05-02', '10:00', 'EDT'],
        ['Newcastle', 'Brighton', '2026-05-02', '10:00', 'EDT'],
        ['Wolves', 'Sunderland', '2026-05-02', '10:00', 'EDT'],
        
        # Saturday, 9 May 2026
        ['Brighton', 'Wolves', '2026-05-09', '10:00', 'EDT'],
        ['Burnley', 'Aston Villa', '2026-05-09', '10:00', 'EDT'],
        ['C Palace', 'Everton', '2026-05-09', '10:00', 'EDT'],
        ['Fulham', 'AFC Bournemouth', '2026-05-09', '10:00', 'EDT'],
        ['Liverpool', 'Chelsea', '2026-05-09', '10:00', 'EDT'],
        ['Man City', 'Brentford', '2026-05-09', '10:00', 'EDT'],
        ['Nottm Forest', 'Newcastle', '2026-05-09', '10:00', 'EDT'],
        ['Spurs', 'Leeds', '2026-05-09', '10:00', 'EDT'],
        ['Sunderland', 'Man United', '2026-05-09', '10:00', 'EDT'],
        ['West Ham', 'Arsenal', '2026-05-09', '10:00', 'EDT'],
        
        # Sunday, 17 May 2026
        ['AFC Bournemouth', 'Man City', '2026-05-17', '10:00', 'EDT'],
        ['Arsenal', 'Burnley', '2026-05-17', '10:00', 'EDT'],
        ['Aston Villa', 'Liverpool', '2026-05-17', '10:00', 'EDT'],
        ['Brentford', 'C Palace', '2026-05-17', '10:00', 'EDT'],
        ['Chelsea', 'Spurs', '2026-05-17', '10:00', 'EDT'],
        ['Everton', 'Sunderland', '2026-05-17', '10:00', 'EDT'],
        ['Leeds', 'Brighton', '2026-05-17', '10:00', 'EDT'],
        ['Man United', 'Nottm Forest', '2026-05-17', '10:00', 'EDT'],
        ['Newcastle', 'West Ham', '2026-05-17', '10:00', 'EDT'],
        ['Wolves', 'Fulham', '2026-05-17', '10:00', 'EDT'],
        
        # Sunday, 24 May 2026 - FINAL DAY
        ['Brighton', 'Man United', '2026-05-24', '11:00', 'EDT'],
        ['Burnley', 'Wolves', '2026-05-24', '11:00', 'EDT'],
        ['C Palace', 'Arsenal', '2026-05-24', '11:00', 'EDT'],
        ['Fulham', 'Newcastle', '2026-05-24', '11:00', 'EDT'],
        ['Liverpool', 'Brentford', '2026-05-24', '11:00', 'EDT'],
        ['Man City', 'Aston Villa', '2026-05-24', '11:00', 'EDT'],
        ['Nottm Forest', 'AFC Bournemouth', '2026-05-24', '11:00', 'EDT'],
        ['Spurs', 'Everton', '2026-05-24', '11:00', 'EDT'],
        ['Sunderland', 'Chelsea', '2026-05-24', '11:00', 'EDT'],
        ['West Ham', 'Leeds', '2026-05-24', '11:00', 'EDT'],
    ]
    
    # Create DataFrame
    df = pd.DataFrame(fixtures, columns=['HomeTeam', 'AwayTeam', 'Date', 'Time', 'Timezone'])
    
    # Standardize team names (mapping to your desired format)
    team_name_map = {
        'Spurs': 'Tottenham',
        'Man United': 'Man United',  # Already in correct format
        'Man City': 'Man City',      # Already in correct format
        'Wolves': 'Wolves',
        'AFC Bournemouth': 'Bournemouth',
        'Leeds': 'Leeds',
        'Brighton': 'Brighton',
        'Newcastle': 'Newcastle',
        'West Ham': 'West Ham',
        'Aston Villa': 'Aston Villa',
        'Nottm Forest': "Nott'm Forest",
        'Sunderland': 'Sunderland',
        'Burnley': 'Burnley',
        'Brentford': 'Brentford',
        'Fulham': 'Fulham',
        'Everton': 'Everton',
        'Liverpool': 'Liverpool',
        'Arsenal': 'Arsenal',
        'Chelsea': 'Chelsea',
        'C Palace': 'Crystal Palace',
    }
    
    df['HomeTeam'] = df['HomeTeam'].replace(team_name_map)
    df['AwayTeam'] = df['AwayTeam'].replace(team_name_map)
    
    # Create datetime column and sort
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df.sort_values('DateTime').reset_index(drop=True)
    
    # Your pipeline likely only needs HomeTeam, AwayTeam, Date
    # So return just those columns
    return df[['HomeTeam', 'AwayTeam', 'Date']]


def save_fixtures_to_csv(season="2526"):
    """Save fixtures to CSV for caching"""
    df = get_all_fixtures()
    
    # Create data directory if it doesn't exist
    Path("data").mkdir(exist_ok=True)
    
    # Save to CSV
    csv_path = f"data/remaining_fixtures{season}.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Saved {len(df)} fixtures to {csv_path}")
    
    return df


def get_fixtures_by_date_range(start_date=None, end_date=None):
    """Get fixtures within a specific date range"""
    df = get_all_fixtures()
    
    if start_date:
        df = df[df['Date'] >= start_date]
    if end_date:
        df = df[df['Date'] <= end_date]
    
    return df


def get_next_n_fixtures(n=10):
    """Get next N fixtures from today"""
    df = get_all_fixtures()
    
    # Convert to datetime for comparison
    df['DateObj'] = pd.to_datetime(df['Date'])
    today = pd.Timestamp.now().normalize()
    
    # Filter for future fixtures
    df = df[df['DateObj'] >= today]
    df = df.sort_values('DateObj')
    df = df.drop('DateObj', axis=1)
    
    return df.head(n)

if __name__ == "__main__":
    save_fixtures_to_csv()  # Save fixtures to CSV on module import