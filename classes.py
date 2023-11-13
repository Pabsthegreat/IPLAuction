from tkinter import *
from PIL import Image, ImageTk

#class of buttons to allow for generalizing button behaviours and allows to call functions related to buttons without renaming each time.
class Buttons(object):
    def __init__(self, name, pic, wallet, r, c):
        self.name = name
        self.pic = pic
        self.wallet = wallet
        self.r = r
        self.c = c
    def display(self): #displaying required data
        label1 = Label(root, text = self.name.upper()).grid(row = self.r, column = self.c)
        label2 = Label(root, text = "Wallet: "+str(self.wallet)+" cr").grid(row = self.r+1, column = self.c)
        b = Button(root, image = self.pic, command = self.team)  #calls the desired function when clicked #should a command always be there?
        b.grid(row = self.r-1, column = self.c, columnspan = 3, pady = 7, padx = 5)#pady=5, padx= 5

    def team(self):
        print("hi")

teams_list = ["rr","rcb","gt","csk","srh","lsg","kxip","kkr","dc","mi"]
teams_list.sort()
#initializing window
root = Tk()
root.geometry("600x600")
#setting title of window
root.wm_title("IPL AUCTION")
#setting window icon
t_img = ImageTk.PhotoImage(file="C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\public\\ipl.jpeg")
root.iconphoto(True,t_img)
#content area
c_img0 = Image.open("C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\public\\auction.jpeg")
c_img1 = c_img0.resize((150,150))
c_img = ImageTk.PhotoImage(c_img1)
content = Label(root, image=c_img)
content.grid(row=1, column=0, columnspan=6, rowspan=3, padx=5, pady=10)#padx=5, pady=10)

#getting the team buttons
r = 4 #row
c = 0 #column
for i in teams_list:
    image1 = Image.open("C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\teampics\\"+i+".jpeg")
    image2 = image1.resize((75, 75))
    photo = ImageTk.PhotoImage(image2)
    if teams_list.index(i) % 5 == 0: #to get 5 buttons per row the += values are to get right spacing between the icons
        c = 0
        r += 3
    else: 
        c += 4

    t = Buttons(i, photo, 100, r, c)
    t.display()
    # label = Label(root, text = i.upper()) #getting the title of each team.
    # label.grid(row=r, column=c, columnspan=3, padx=5, pady=2)

#calling the main loop of tkinter
root.mainloop()


# Label(root, text = 'Position image on button', font =('calibri', 10)).pack(side = TOP, padx = 5, pady = 5)
# image1 = Image.open("C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\teampics\\71-z0jdRfvL._AC_UF1000,1000_QL80_.jpg")
# image2 = image1.resize((50, 50))
# photo = ImageTk.PhotoImage(image2)
# Position image on button
# Button(root, image = photo, command=one.display).pack(side = BOTTOM, pady = 5)


# #Create a photoimage object of the image in the path
# image1 = Image.open("C:\\Users\\adars\\OneDrive\\Documents\\GitHub\\IPLAuction\\pics\\teampics\\71-z0jdRfvL._AC_UF1000,1000_QL80_.jpg")
# test = ImageTk.PhotoImage(image1)
# label1 = Label(image=test)
# label1.image = test
# # Position image
# label1.place(x =10, y=10)

