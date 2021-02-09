import sys,os
import tkinter as tk
from tkinter import filedialog



class Application(tk.Frame):
    def __init__(self, master=None):
        #Init widget frame with set width and height
        tk.Frame.__init__(self, master, bd=100)
        #self.grid_propagate(0)  #Propagate to allow custom frame size

        self.grid()
        self.createWidgets()

    def select_skin(self):
        #Find skins
        folders = {} #skin folder name : fp
        for root,dirs,files in os.walk(self.skin_dir):
            for skin_fold in dirs:
                folders[skin_fold] = os.path.join(root,skin_fold)
        #Create dropdown menu with available skins

        # self.skin_mb = tk.Menubutton(self, text="Select skin to make funny", relief=tk.RAISED)
        # self.skin_mb.grid(row=4,column=0)

        # self.skin_mb.menu = tk.Menu(self.skin_mb, tearoff=0)
        # self.skin_mb['menu'] = self.skin_mb.menu

        # #temp: add avail skins
        # self.skin1 = tk.IntVar()
        # self.skin_mb.menu.add_checkbutton(label='skin1',variable=self.skin1)

        # #add all skins as option
        # for skin in folders.keys():
        #     new_var = tk.IntVar()
        #     self.skin_mb.menu.add_checkbutton(label=skin,variable=new_var)

        self.skin_list = tk.Listbox(self)




    def get_dir(self):
        self.directory = os.path.abspath(filedialog.askdirectory())
        self.skin_dir = self.directory
        #If main osu! folder was entered, direct to Skins folder
        if os.path.basename(self.directory) == "osu!":
            self.skin_dir = os.path.join(self.directory, "Skins")
        
        #Verify correct input
        if not os.path.exists(self.skin_dir) or os.path.basename(self.skin_dir) != "Skins":
            #Update title label
            self.titleLabel = tk.Label(self, text="Invalid folder directory. Please input the correct\ngame installation folder containing Skins.", padx=10,pady=10)
            self.titleLabel.grid(row=0,column=0)
            return

        #Omit all from the grid after row 1
        for wi in self.grid_slaves():
                wi.grid_forget()

        #Draw result widget
        self.resultLabel = tk.Label(self,text=f"osu! Skins directory: {self.skin_dir}")
        self.resultLabel.grid(row=3,column=0)

        self.select_skin()
        

    def createWidgets(self):
        #Instructions label
        self.titleLabel = tk.Label(self, text="Please browse to osu! game folder directory", padx=10,pady=10)
        self.titleLabel.grid(row=0,column=0)

        #File input
        self.browseButton = tk.Button(self, text="Browse", command=self.get_dir)
        self.browseButton.grid(row=2,column=0)

        #Quit app
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)  #Init new button widget
        self.quitButton.grid(sticky=tk.SE)  #Populate grid with button
    



app = Application()
app.master.title('osu! funny skin generator')
app.mainloop()
