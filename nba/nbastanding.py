import requests
import json
import datetime

class NBAStanding:

    def __init__(self):
        self.url = 'https://en.global.nba.com/stats2/season/conferencestanding.json'
        self.json_raw = self.get_json_from_url(self.url)

    def get_json_from_url(self, url):
        return json.loads(requests.get(url).content)

    def prepare_conf(self,conf):
        res = ""
        res += conf["conf-name"] +"\n"
        for team in conf["teams"]:
            if int(team[0]) < 10:
                res += "0{}|{} : W{}/L{}\n".format(team[0],team[1],team[2],team[3])
            else:
                res += "{}|{} : W{}/L{}\n".format(team[0],team[1],team[2],team[3])

        return res

    def process_conference(self,conf):
        result = dict()
        result["conf-name"] = conf["conference"]
        result["teams"] = []
        jteams = conf["teams"]
        for jteam in jteams:
            teamname = jteam["profile"]["abbr"]
            rank = jteam["standings"]["confRank"]
            wins = jteam["standings"]["wins"]
            loss = jteam["standings"]["losses"]
            result["teams"].append(tuple([rank, teamname, wins, loss]))
        result["teams"] = sorted(result["teams"],key=lambda x: x[0])
        return result

    def get_standings(self,conf="ALL"):
        is_error = self.json_raw['error']['isError']
        if is_error != "false":
            return "ERROR"

        conf1 = self.process_conference(self.json_raw["payload"]["standingGroups"][0])
        conf2 = self.process_conference(self.json_raw["payload"]["standingGroups"][1])

        east = conf1 if conf1["conf-name"] == "Eastern" else conf2
        west = conf1 if conf1["conf-name"] == "Western" else conf2

        east = self.prepare_conf(east)
        west = self.prepare_conf(west)

        if conf == "ALL":
            return east +"\n\n\n" + west
        elif conf == "EAST":
            return east
        elif conf == "WEST":
            return west
