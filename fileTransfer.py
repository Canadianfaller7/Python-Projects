import shutil
import os
import webbrowser
from tkinter import *
import tkinter as tk
# source = '/Users/spencermerrill/Desktop/Folder A/'

# destination = '/Users/spencermerrill/Desktop/Folder B/'

# files = os.listdir(source)

# for i in files:
#     shutil.move(source+i, destination)

# sourceCopy = '/Users/spencermerrill/Desktop/Folder C/'

# destinationCopy = '/Users/spencermerrill/Desktop/Folder D/'

# filesCopy = os.listdir(sourceCopy)

# for i in filesCopy:
#     shutil.copy(sourceCopy+i, destinationCopy)


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
        self.master.title("The Tkinter File Transfer Demo")
        # this is a lable telling the user what to do
        self.lbl_webBody = tk.Label(self.master, text='Please select the folers that have the files you would like to transfer: ')
        # these are just locations of where the label will sit
        self.lbl_webBody.grid(row=0, column=0, padx = (20,20), pady=(10,0), sticky = N+W)

        # this is where we put the button to run our openWeb function and to run everything inside and to execute it and show up when the button is pressed
        self.btn_add = tk.Button(self.master, width=8, height=2, text='Folder C', command = lambda: (self))
        self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky = W)









if __name__ == '__main__':
    # this creates the window from the tkinter
    root = tk.Tk()
    # this is our app we are calling our class the app and attached the root
    # basically this is the syntax required by tkinter in order to create the window and pass it to our class
    App = ParentWindow(root)
    # this is to make it so the app doesn't close right away
    root.mainloop()


