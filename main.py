from data import * 
player_data = data_r()
batsmen = player_data["batsmen"]
bowlers = player_data["bowlers"]
allrounders = player_data["allrounders"]
keepers = player_data["keepers"]
roster = [batsmen, bowlers, allrounders, keepers]

def next_player(): #generator function
    for i in roster:
        gen = iter(i)
        for j in gen:
            pic = j[1]
            uselist  = j.copy()
            uselist.pop(1)
            actlist = []
            temp = []
            for i in range(len(uselist)-1):
                if i % 2 != 0:
                    temp.append(uselist[i])
                    actlist.append(temp.copy())
                    temp.clear()
                else:
                    temp += [uselist[i]]
            yield pic, actlist
        
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






