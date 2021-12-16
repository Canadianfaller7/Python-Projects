import shutil
import os
import webbrowser
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import fileTranferFunc
import fileTransfer
# this is a lable telling the user what to do
def loadGui(self):      

    # Label widget 
    self.lbl_fSource = tk.Label(self.master, text='Select source folder: ')
    # these are just locations of where the label will sit
    self.lbl_fSource.grid(row=0, column=0, padx = (10,20), pady=(20,20), sticky = N+W)
    self.lbl_fDestination = tk.Label(self.master, text='Select desitnation folder: ')
    self.lbl_fDestination.grid(row=1, column=0, padx = (10,20), pady=(10,10), sticky = N+W)
    self.lbl_fMove = tk.Label(self.master, text='Click here to move/copy files: ')
    self.lbl_fMove.grid(row=2, column=0, padx = (10,20), pady=(10,10), sticky = N+W)

    # Entry widget
    self.txt_fSource = tk.Entry(self.master, text = '')
    self.txt_fSource.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
     self.txt_fDestination = tk.Entry(self.master, text = '')
    self.txt_fDestination.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
    
    
    # Button widgets

    # this is where we put the button to run our openWeb function and to run everything inside and to execute it and show up when the button is pressed
    self.btn_add = tk.Button(self.master, width=10, height=2, text='Source', command = lambda: fileTranferFunc.pickSource(self))
    self.btn_add.grid(row=0, column=1, padx=(10,10), pady=(5,20), sticky = W)
     # this is where we put the button to run our openWeb function and to run everything inside and to execute it and show up when the button is pressed
    self.btn_add = tk.Button(self.master, width=10, height=2, text='Destination', command = lambda: fileTranferFunc.pickDestination(self))
    self.btn_add.grid(row=1, column=1, padx=(10,10), pady=(5,10), sticky = W)
     # this is where we put the button to run our openWeb function and to run everything inside and to execute it and show up when the button is pressed
    self.btn_add = tk.Button(self.master, width=10, height=2, text='Move/Copy', command = lambda: fileTranferFunc.moveFiles(self))
    self.btn_add.grid(row=2, column=1, padx=(10,10), pady=(10,5), sticky = W)


if __name__ == '__main__':
    pass