from tkinter import *
from main import *
from data import write_data
root = Tk()
# #creating a label widget
# mylabel1 = Label(root, text= "IPL Auction")
# mylabel2 = Label(root, text= "HI")
# # mylabel1.pack()   #putting on screen
# #columns is relative if there is nothing in columns it will just print the next column with content
# mylabel1.grid(row = 0, column = 0) alt for pack
# mylabel2.grid(row = 1, column = 1)
# root.geometry("400x400")
e = Entry(root, width = 50) #input box
e.pack()
e.insert(0,"Enter your name!")
# buttons
def f1():
    mylabel1 = Label(root, text= e.get()) #gets input from Entry
    mylabel1.pack()
    
button =  Button(root, text="Team 1", command=f1)
button.pack()

class Team_button(name,pic, )
#bid
# cur_bid, cur_team = bid(cur_bid, )

cur_player = []
#next button
x = next_player()
print(x)
cur_player = x
#sell player
write_data(cur_team, cur_player, cur_bid)
root.mainloop()