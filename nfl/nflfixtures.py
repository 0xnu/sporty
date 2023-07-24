import requests
import json

def nfl_schedule():
    response = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
    data = response.json()

    ret = ''
    for event in data['events']:
        status = event['status']['type']['name']
        if status == 'STATUS_SCHEDULED':
            home_team = event['competitions'][0]['competitors'][0]['team']['displayName']
            away_team = event['competitions'][0]['competitors'][1]['team']['displayName']
            date = event['date']

            ret += f"\n  {home_team} [Home] - [Away] {away_team}\n"
            ret += f"  Game Date: {date}\n"

    return ret

nfl_sched = nfl_schedule()
#print(nfl_sched)
