import csv
print("Enter all names, all runs, all wickets etc...")
print("Enter Q to quit the loop once all of that particular data has been entered.")
l = ["type", "pic", "name", "age", "country", "spec", "exp", "matches", "runs", "wickets", "catches", "stumpings", "base", "bid"]
sub = []
for i in l:
    j = []
    while True:
        q = input("Enter"+" "+i+" :")
        if q.lower() == "q":
            break
        else:
            j.append(q)
    sub.append(j)
main = {}
for i in range(len(sub[0])):
    name = sub[2][i]
    main[name] = [] #making a dict with key as each player name and initializing a empty list to write easily into csv file.

for i in main:
    for j in range(len(l)):
        name_index = sub[2].index(i)  #the index of a player's detail in each category in the sublist will be the same.
        main[i].append(sub[j][name_index]) #adding each detail from sub list into the player's list in the main dict.

with open("player_data.csv","a") as f:
    player_w = csv.writer(f, lineterminator="\n")
    for i in main:
        player_w.writerow(main[i]) #writing each player onto the player_data csv file.
