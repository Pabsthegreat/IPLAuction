import csv
def data_r():
    with open("data\\playerdata\\player_data.csv", "r") as player_data:
        read = csv.reader(player_data)
        player_datal = {}
        player_datal["batsmen"] = []
        player_datal["bowlers"] = []
        player_datal["allrounders"] = []
        player_datal["keepers"] = []
        for i in read:
            if i[0] == "batsman":
                player_datal["batsmen"].append(i)
            elif i[0] == "bowler":
                player_datal["bowlers"].append(i)
            elif i[0] == "allrounder":
                player_datal["allrounders"].append(i)
            elif i[0] == "keeper":
                player_datal["keepers"].append(i)
        return player_datal

def write_data(team,player, price):
    with open("data\\auction_files\\team_data.csv","a") as teams:
        teamwriter = csv.writer(teams, lineterminator="\n")
        sold_player = [team] + [player] + [price]
        teamwriter.writerow(sold_player)
        return "records updated"

def team_data(team):
    with open("data\\auction_files\\team_data.csv","r", newline="\n") as team1:
        t_read = csv.reader(team1)
        req_team = []
        for i in t_read:
            if i[0] == team:
                req_team.append(i[1:])
        return req_team

def team_wallet(team):
    wallet = 0
    team1 = open("data\\auction_files\\team_data.csv","r", newline="\n")
    t_read = csv.reader(team1)
    wallet = 100
    for i in t_read:
        if i[0] == team:
            wallet -= float(i[-1])
    print(wallet)
    return round(wallet,2)
