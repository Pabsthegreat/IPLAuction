from tkinter import *
from main import *
from data import write_data
from PIL import Image, ImageTk
from tkinter import ttk
#class of buttons to allow for generalizing button behaviours and allows to call functions related to buttons without renaming each time.
class Buttons(object):
    def __init__(self, name, pic, wallet, x, y):
        self.name = name
        self.pic = pic
        self.wallet = wallet
        self.x = x
        self.y = y
    def display(self): #displaying required data
        label1 = Label(root, text = self.name.upper()).place(x = self.x + 25, y = self.y+80)
        label2 = Label(root, text = "Wallet: "+str(self.wallet)+" cr").place(x = self.x , y = self.y+100)
        b = Button(root, image = self.pic, command = self.team)  #calls the desired function when clicked #should a command always be there?
        b.place(x = self.x , y = self.y, bordermode="inside")

    def team(self):
        print("hi")

teams_list = ["rr","rcb","gt","csk","srh","lsg","kxip","kkr","dc","mi"]
teams_list.sort() #alphabetical order

#initializing window
root = Tk()
root.geometry("600x600")

#setting title of window
root.wm_title("IPL AUCTION")

#setting window icon
t_img = ImageTk.PhotoImage(file="C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\public\\ipl.jpeg")
root.iconphoto(True,t_img)
def content(pic, players_list = []):
    print(pic)
    #player_list format:{type, pic, name, age, country, spec, exp, matches, runs, wickets, catches, stumpings, base, bid}
    #content area
    if len(players_list) == 0:
        c_img0 = Image.open(pic)
        c_img1 = c_img0.resize((145,145))
        c_img = ImageTk.PhotoImage(c_img1)
        Label(root, image=c_img).place(x = 0, y = 0)
        welc = Label(root, text="WELCOME TO IPL AUCTION", width=25). place(x = 175, y = 55)
    else:
        c_img0 = Image.open(pic)
        c_img1 = c_img0.resize((145,145))
        c_img = ImageTk.PhotoImage(c_img1)
        Label(root, image=c_img).place(x = 0, y = 0)
       
        tree = ttk.Treeview(root,column = ('c1','c2'), height=6) #tree with column headings
        
        tree.column('#1',anchor = CENTER)
        tree.column('#2',anchor = CENTER)
        for i in players_list:
            tree.insert("", END, values = i)
        tree.place(x = 175, y = 0)

m = next_player()
def get_next():
    pic, player_list = next(m)
    print(pic)
    content(pic, player_list)

content('C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\public\\auction.jpeg')
    
bid_label = Label(root, text="Current Bid is", width=25). place(x = 30, y = 170)
current_label = Label(root, text="Current", width=15). place(x = 230, y = 170)
sell_Button = Button(root, text="Sold",width=10). place(x = 335, y = 170)
intro = Label(root, text="Click a Team to place bid or increase bid for that team").place(x = 50, y = 220)
next_button = Button(root, text="Next Player ->",width=15, command=get_next). place(x = 450, y = 170)
#getting the team buttons
y = 100
x = 50 
for i in teams_list:
    image1 = Image.open("C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\teampics\\"+i+".jpeg")
    image2 = image1.resize((75, 75))
    photo = ImageTk.PhotoImage(image2)
    
    if teams_list.index(i) % 5 == 0: #to get 5 buttons per row the += values are to get right spacing between the icons
        x = 50
        y += 150
    else: 
        x += 100

    t = Buttons(i, photo, 100, x, y)
    t.display()
#bid
# cur_bid, cur_team = bid(cur_bid, )

# cur_player = []
# #next button
# x = next_player()
# print(x)
# cur_player = x
# #sell player
# write_data(cur_team, cur_player, cur_bid)

root.mainloop()