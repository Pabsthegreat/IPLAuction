from data import * 
from PIL import Image, ImageTk
import os
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
            # Normalize image path from CSV so it works on all OSes
            pic = j[1].replace("\\", "/")
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
def teamlists(team):#returns team list, number of players, total value of team
    team1 = team_data(team)
    disp_team = []
    val = 0
    for i in team1:
        disp_team += [i[0:7]]
        val += i[-1]
    return disp_team, len(disp_team), val

def req_pic(path, width, height):#try req_label
    req_img0 = Image.open(path)
    req_img1 = req_img0.resize((width, height))
    req_img = ImageTk.PhotoImage(req_img1)
    return req_img




