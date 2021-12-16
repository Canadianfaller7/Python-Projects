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
# Tested OS:  This code was written and tested to work with Windows 10.

import shutil
import os
import webbrowser
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import fileTransfer
import fileTransferGui

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


def pickSource(self):
    source = filedialog.askdirectory()

def pickDestination(self):
    destination = filedialog.askdirectory()

def moveFiles(self):
    files = os.listdir(pickSource)
    for i in files:
        shutil.move(pickSource+i, pickDestination)

if __name__ == "__main__":
    pass