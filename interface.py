from tkinter import *
from main import *
from data import write_data
from PIL import Image, ImageTk
from tkinter import ttk

#class of buttons to allow for generalizing button behaviours and allows to call functions related to buttons without renaming each time.
class Buttons(object):
    def __init__(self, name, x, y, pic = "pics\\public\\ipl.jpeg", wallet = 100):
        self.name = name
        self.pic = pic
        self.wallet = wallet
        self.x = x
        self.y = y

    def display(self): #displaying required data
        label1 = Label(root, text = self.name.upper()).place(x = self.x + 25, y = self.y+80)
        label2 = Label(root, text = "Wallet: "+str(self.wallet)+" cr").place(x = self.x , y = self.y+100)
        b = Button(root, image = self.pic, command = self.bid_deets)  #calls the desired function when clicked #should a command always be there?
        b.place(x = self.x , y = self.y, bordermode="inside") #can i give params in the command function, will it instatnly execute?

    def bid_deets(self):
        global bid_price,base_price,bid_team, wallet_bidteam
        bid_team = self.name
        self.wallet = team_wallet(self.name)
        print(self.wallet)
        label2 = Label(root, text = "Wallet: "+str(self.wallet)+" cr").place(x = self.x , y = self.y+100)
        if bid_price == 0:
            bid_price = int(base_price)
        else:
            bid_price += 0.05
            bid_price = round(bid_price,2) #limit decimal points to 2 digits after decimal point
            
        #label that show current bidded price   
        bid_label = Label(root, text="Current Bid is : " + str(bid_price) + ".cr", width=25). place(x = 30, y = 170)

        #image of the team currently with the highest bid
        c_img = req_pic("pics\\teampics\\"+self.name+".jpeg",30,30)
        current_label = Label(root, image=c_img)
        current_label. place(x = 210, y = 170)
        current_label.image = c_img


teams_list = ["rr","rcb","gt","csk","srh","lsg","kxip","kkr","dc","mi"]
teams_list.sort() #alphabetical order

#initializing window
root = Tk()
root.geometry("600x600")
#setting title of window
root.wm_title("IPL AUCTION")

#bid and base price of current player
bid_price = 0
base_price = 0.25
bid_team = ""
player = ""
wallet_bidteam = 100
#setting window icon
t_img = ImageTk.PhotoImage(file="pics\\public\\ipl.jpeg")
root.iconphoto(True,t_img)

def content(pic, players_list = []):
    #player_list format:{type, pic, name, age, country, spec, exp, matches, runs, wickets, catches, stumpings, base}
    global bid_price, base_price, player

    if players_list != []:
        base_price = players_list[-1][-1]
        bid_price = 0
        player = players_list[0][1]
        #resettig the values for new player
        Label(root, text="Current Bid is : 0.cr", width=25). place(x = 30, y = 170)
        d_img = req_pic("pics\\public\\auction.jpeg",30,30)
        d = Label(root, image=d_img)
        d.place(x = 210, y = 170)
        d.image = d_img

    #content area
    if len(players_list) == 0:
        welc = Label(root, text="WELCOME TO IPL AUCTION", width=25). place(x = 175, y = 55)
        c_img = req_pic(pic,145,145)
        c = Label(root, image=c_img)
        c.place(x = 0, y = 0)
        c.image = c_img
        #The problem is that the Tkinter/Tk interface doesn’t handle references to Image objects properly; 
        # the Tk widget will hold a reference to the internal object, but Tkinter does not. 
        # When Python’s garbage collector discards the Tkinter object, Tkinter tells Tk to release the image. 
        # But since the image is in use by a widget, Tk doesn’t destroy it. Not completely. It just blanks the image, making it completely transparent…
        # The solution is to make sure to keep a reference to the Tkinter object, for example by attaching it to a widget attribute: 
        
    else:
        tree = ttk.Treeview(root,column = ('c1','c2'), height=6, show = '') #tree with column headings
        tree.column('#1',anchor = CENTER)
        tree.column('#2',anchor = CENTER)

        for i in players_list:
            tree.insert("", END, values = i)
        tree.place(x = 175, y = 0)

        c_img = req_pic(pic,145,145)
        c = Label(root, image = c_img)
        c.place(x = 0, y = 0)
        c.image = c_img

#fn that calls the fns that displays the player details on screen
m = next_player()
def get_next():
    pic, player_list = next(m)
    content(pic, player_list)

def sell(): #writes data onto team database and then calls get_next() which gets the next player onto the screen
    write_data(bid_team, player, bid_price)
    get_next()

#starting face
content('pics\\public\\auction.jpeg')

#label that show current bidded price   
bid_label = Label(root, text="Current Bid is", width=25). place(x = 30, y = 170)

#image of the team currently with the highest bid
current_label = Label(root, text="Current", width=15). place(x = 230, y = 170)

#sell button
sell_Button = Button(root, text= "sold", width=10, command=sell)
sell_Button.place(x = 335, y = 170)

#intro label
intro = Label(root, text="Click a Team to place bid or increase bid for that team").place(x = 50, y = 220)

#next button
next_button = Button(root, text="Next Player ->",width=15, command=get_next). place(x = 450, y = 170)

#getting the team buttons
y = 100
x = 50 
for i in teams_list:
    photo = req_pic("pics\\teampics\\"+i+".jpeg",75,75)
    
    if teams_list.index(i) % 5 == 0: #to get 5 buttons per row the += values are to get right spacing between the icons
        x = 50
        y += 150
    else: 
        x += 100

    t = Buttons(i, x, y, photo)
    t.display()

root.mainloop()