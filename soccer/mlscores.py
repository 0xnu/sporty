import requests
import json

def MLScores():
    response = requests.get("http://site.api.espn.com/apis/site/v2/sports/soccer/usa.1/scoreboard")
    data = response.json()

    ret = ''
    for event in data['events']:
        home_team = event['competitions'][0]['competitors'][0]['team']['displayName']
        home_score = event['competitions'][0]['competitors'][0]['score']
        away_team = event['competitions'][0]['competitors'][1]['team']['displayName']
        away_score = event['competitions'][0]['competitors'][1]['score']
        status = event['status']['type']['description']

        ret += f"\n  {home_team} [Home] - [Away] {away_team} Score: {home_score} - {away_score}\n"
        ret += f"  Game Status: {status}\n"

    return ret

mlscores = MLScores()
#print(mlscores)
