import shutil
import os
import webbrowser
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import fileTranferFunc
import fileTransferGui




""" Here is how we can go and create a GUI tkinter app and have it connect with an html file
so when you type in the text into the box and then click create website, it will then add 
what you wrote into the body of the html file and display it on the screen."""

# this is for the tkinter part of things
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        # in order to access objects from the parent window, you need to specify "self." and then the actual tkinter object
        # that we want to make changes to or get data from. its like the address to get to it.
        # so for example, below "self" is simply saying our ParentWindow.master(Frame) so self.master is the ParentWindow(Frame)
        self.master = master
        self.master.minsize(370, 270)
        self.master.maxsize(2560,1080)

        fileTranferFunc.center_window(self,370,270)
        self.master.title("The Tkinter File Transfer Demo")
        arg = self.master
        fileTransferGui.loadGui(self)


if __name__ == '__main__':
    # this creates the window from the tkinter
    root = tk.Tk()
    # this is our app we are calling our class the app and attached the root
    # basically this is the syntax required by tkinter in order to create the window and pass it to our class
    App = ParentWindow(root)
    # this is to make it so the app doesn't close right away
    root.mainloop()


