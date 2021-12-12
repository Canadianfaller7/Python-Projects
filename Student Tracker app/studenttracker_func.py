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

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

# import our other files as well
import studenttracker_main
import studenttracker_gui

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

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect('db_studenttracker.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_studenttracker.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student (col_fname,col_lname,col_fullname,col_phone,col_email, col_course) VALUES (?,?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com', 'JavaScript'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_student""")
    count = cur.fetchone()[0] # because our data that will be returned will be returned as tuples, we need to extract them and this is how we do it  
    return cur,count

def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0] # because our data that will be returned will be returned as tuples, we need to extract them and this is how we do it
    value = varList.get(select) # this will take the extracted index's from the tuple from the code above and returns its value so we don't just get numbers
    conn = sqlite3.connect('db_studenttracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email, col_course FROM tbl_student WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # this returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistent with the database
    var_fname = var_fname.strip() # this will remove any blank spaces before and after the users entry
    var_lname = var_lname.strip() # this will ensure that the first character in each word is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname)) # combine our normalized names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not "@" or not "." in var_email:#will use this soon
        print("Incorrect email fromat!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): # enforce the user to provide both names
        conn = sqlite3.connect('db_studenttracker.db')
        with conn:
            cursor = conn.cursor()
            # check the database for existance of the fullname, if so we will alert user and disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student WHERE col_fullname = '{}'""".format(var_fullname)) #, (var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: # if this is 0 then there is no existance of the fullname and we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_student (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
                onClear(self) # call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database. Please choos a different name.".format(var_fullname))
                onClear(self) # call the function to clear all of the textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missint Text Error", "Please ensure that there is data in all foru fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # listbob's selected value
    conn = sqlite3.connect('db_studenttracker.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure this is not the last record in the database... cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information assiciated with, ({}) \nwill be permenantly deleted from the database. \
                                            \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_studenttracker.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox.
                    # onRefresh(self) ## update the listbox of the changes
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and connot be deleted at this time. \
                                                \n\nPlease add another record first before you can delete ({})".format(var_select,var_select))

    conn.close()

def onDeleted(self):
    # clear the text in thes textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    #   onRefresh(self) # update the listbox of the changes

    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onRefresh(self):
    # populate the listbox, coinciding with the database
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('db_studenttracker.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()

if __name__ == '__main__':
    pass
    
