#
# Python 3.10
#
# Author:    Spencer Merrill
#
# Purpose:   Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#            using Tkinter Parent and Child relationships.
#         
# Tested OS: This code was written and tested to work with Windows 10 and 11

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Be sure to import the other modules we made so we can have access to them
import phonebook_gui
import phonebook_func

# frame is the tkinter frame calss that our own class will inherit from("master" is what we will be calling the frame class)
# (when dealing with classes, once you have defined your class, you will then reference it with the "self" word)

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        # in order to access objects from the parent window, you need to specify "self." and then the actual tkinter object
        # that we want to make changes to or get data from. its like the address to get to it.
        # so for example, below "self" is simply saying our ParentWindow.master(Frame) so self.master is the ParentWindow(Frame)
        self.master = master
        self.master.minsize(500,300) # (Height, Width)
        self.master.maxsize(500,300)

        # this center window method will center our app on the user's screen
        # this line below is accessing our phonebook_func file because we imported it
        # then we define an actual function called center_window which allows us to center the app always to a users screen.
        phonebook_func.center_window(self,500,300)
        # this line is going to make the title for our app
        self.master.title("The Tkinter Phonebook Demo")
        # this is going to set the background color
        self.master.configure(bg="#F0F0F0")

        # this protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on windows OS. We then use our phonebook_func file again because
        # ask_quit will be a function inside that file
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, keeping
        # your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)


        

if __name__ == '__main__':
    # this creates the window from the tkinter
    root = tk.Tk()
    # this is our app we are calling our class the app and attached the root
    # basically this is the syntax required by tkinter in order to create the window and pass it to our class
    App = ParentWindow(root)
    # this is to make it so the app doesn't close right away
    root.mainloop()
