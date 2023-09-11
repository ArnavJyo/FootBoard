import requests
import json
import pandas as pd

Mancity_uri = 'http://api.football-data.org/v4/teams/65'
headers = { 'X-Auth-Token': '7b4b24acaa1c42a19a95a189f9b52c0f' }

try:
    response = requests.get(Mancity_uri, headers=headers)
    print(response.status_code)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    print(data)
    # premier_league_teams_standings_df = pd.json_normalize(data['standings'][0]['table'])
    # premier_league_teams_standings_df.columns = premier_league_teams_standings_df.columns.str.replace('team.', 'team_')

    # premier_league_teams_standings_df.to_csv('premier_league_teams_standings.csv')
    # df = pd.read_csv("premier_league_teams.csv")
    # df = df.fillna(0)
    # df.to_csv('premier_league_teams.csv')
    # df = pd.read_csv("premier_league_teams_standings.csv")
    # df = df.fillna(0)
    # df.to_csv('premier_league_teams_standings.csv')
    pass

    

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
