#
# -*- coding: utf-8 -*-
#
# Python Ver:   3.10.1
#
# Author:       Spencer M.
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10 and OS Monterey

import shutil
import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import fileTransfer
import fileTransferGui


# this is the function to center our app on any screen we run it on
def center_window(self, w, h): # pass in the tkinter frame(master) reference aqnd the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth() # this access the primary window and then we use a tkinter method called winfo_screnWidth() which will get the actual users screen width
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))# these take the users screen size and divide by 2 and then subtracts from our mad width and height we set in the main file and it will take those as well and divide them by 2
    y = int((screen_height/2) - (h/2))
    # and that is how we get to this equation and how we can get our app centered on the users screen
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo

""" Here we can use this function with the tkinter framework and use filedialog
.askdirectory to get the user to put in their own directory they have their files
stored in and then we use the tkinter framework to use the entry method and
access the .delete and .insert to remove any text from the text form in the gui
and then enter in the users directory path and add a / to make sure it is complete """
def pickSource(self):
    source = filedialog.askdirectory()
    self.txt_fSource.delete(0, END)
    self.txt_fSource.insert(0, source + '/')

# this is same as above, but here we are having them select a destination directory
# to move or copy the files to
def pickDestination(self):
    destination = filedialog.askdirectory()
    self.txt_fDestination.delete(0, END)
    self.txt_fDestination.insert(0, destination + '/')

# this function takes the paths from above and then turns them into string
# by using the .get() method and so when we use the os framework .listdir and 
# pass in pickSource it and save it into a var and then plug the var into our
# for loop and run it, it will run through all the files in the directory properly
# return them as a string and then copy those files into our destination directory
def moveFiles(self):
    pickSource = self.txt_fSource.get()
    pickDestination = self.txt_fDestination.get()
    files = os.listdir(pickSource)
    for i in files:
        shutil.copy(pickSource+i, pickDestination)

if __name__ == "__main__":
    pass