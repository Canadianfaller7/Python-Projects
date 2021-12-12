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

# these are our other files we will import to have access to
import studenttracker_gui
import studenttracker_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        # define our master frame configuration
        # in order to access objects from the parent window, you need to specify "self." and then the actual tkinter object
        # that we want to make changes to or get data from. its like the address to get to it.
        # so for example, below "self" is simply saying our ParentWindow.master(Frame) so self.master is the ParentWindow(Frame)
        self.master = master
        self.master.minsize(500,350) #(Width, Height)
        self.master.maxsize(2560,1080)

        # this center window method will center our app on the user's screen
        # this line below is accessing our studenttracker_fun file because we imported it
        # then we define an actual function called center_window which allows us to center the app always to a users screen.
        studenttracker_func.center_window(self,500,350)
        # this is going to set the background color
        self.master.title("The Tkinter Student Tracker App")


        self.master.configure(bg="darkgray")
        # this protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on windows OS. We then use our phonebook_func file again because
        # ask_quit will be a function inside that file
        self.master.protocol("WM_DELETE_WINDOW", lambda: studenttracker_func.ask_quit(self))
        arg = self.master
        
        # load in the GUI widgets from a separate module, keeping
        # your code comparmentalized and clutter free
        studenttracker_gui.load_gui(self)

if __name__ == '__main__':
    # this creates the window from the tkinter
    root = tk.Tk()
    # this is our app we are calling our class the app and attached the root
    # basically this is the syntax required by tkinter in order to create the window and pass it to our class
    App = ParentWindow(root)
    # this is to make it so the app doesn't close right away
    root.mainloop()
