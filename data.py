import csv
def data_r():
    with open("player_data.csv", "rb") as player_data:
        read = csv.reader(player_data)
        player_datal = {}
        player_datal["batsmen"] = []
        player_datal["bowlers"] = []
        player_datal["allrounders"] = []
        player_datal["keepers"] = []
        for i in read:
            if i[0] == "batsman":
                player_datal["batsmen"] = player_datal["batsmen"].append(i)
            elif i[0] == "bowler":
                player_datal["bowlers"] = player_datal["bowlers"].append(i)
            elif i[0] == "allrounder":
                player_datal["allrounders"] = player_datal["allrounders"].append(i)
            elif i[0] == "keeper":
                player_datal["kepers"] = player_datal["keepers"].append(i)

        return player_datal
#decorator and yeild can be used

def write_data(teams):
    with open("team_data.csv","w") as teams:
        cols = ["Team, playerlist"]
        teamwriter = csv.writer(teams, lineterminator="\n")
        teamwriter.writerow
        teamwriter.writerows(teams)
        return "records updated"

def team_data(team):
    with open("team_data.csv","r", newline="\n") as team:
        t_read = csv.reader(team_data)
        req_team = []
        for i in t_read:
            if i[0] == team:
                req_team.append(i[1:])
        return req_team
    
