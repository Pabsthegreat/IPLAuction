from data import * 
player_data = data_r()
batsmen = player_data["batsmen"]
bowlers = player_data["bowlers"]
allrounders = player_data["allrounders"]
keepers = player_data["keepers"]
roster = [batsmen, bowlers, allrounders, keepers]
print(roster)

def next_player(): #generator function
    for i in roster:
        gen = iter(i)
        for j in gen:
            yield j

def bid(team, current, inc): #bid
    current += inc
    return team , current

def teamlists(team):#returns team list, number of players, total value of team
    team1 = team_data(team)
    disp_team = []
    val = 0
    for i in team1:
        disp_team += [i[0:7]]
        val += i[-1]
    return disp_team, len(disp_team), val






