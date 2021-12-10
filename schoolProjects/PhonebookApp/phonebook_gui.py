from tkinter import *
import tkinter as tk

# be sure to import our other modules so we can have access to them
import phonebook_main
import phonebook_func

# remember we have to have self added because it is the key in order for us to access all of the class objects
def load_gui(self):

    """ all these are making our labels by using the tkinter class for a label (tk.Label) which is the syntax to access
    it and bring it to reality or instantiate you then give it a class name which will be (lbl_fname) and
    our rows and columns and what the labels are going to say and where they are going to be put
    by using the grid geometry manager. """
    self.lbl_fname = tk.Label(self.master, text='First Name: ')
    self.lbl_fname.grid(row=0, column=0, padx = (27,0), pady=(10,0), sticky = N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name: ')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky = N+W)
    self.lbl_phone = tk.Label(self.master, text='Phone Number: ')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky = N+W)
    self.lbl_email = tk.Label(self.master, text='Email Address: ')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky = N+W)
    self.lbl_user = tk.Label(self.master, text='User: ')
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky = N+W)
    
    # all of these are going to be the stuff entered and how much room they take up on the columns and we use
    # the rowspan and columnspan to make it so they spread out a litter bigger and take up an exta row/rows and column/columns
    self.txt_fname = tk.Entry(self.master, text = '')
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
    self.txt_lname = tk.Entry(self.master, text = '')
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
    self.txt_phone = tk.Entry(self.master, text = '')
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
    self.txt_email = tk.Entry(self.master, text = '')
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)

    """ this is going to be our box that holds our phonebook list and will create the scroll bar to scroll up and down.
    We also define the tikinter list box here and give it a name of lstList1 and attaching our class to it. Withe the
    (lstList1.bind) we are binding to our list box an event. We are saying this is what they call a listener and so we
    are saying in tikinter to create an event listern to listen for something that is going to occure, which in this case
    is for a user click or select on an object within our list, and if that happens to then call our function which we do by
    creating a Labmda anonymous function (lambda event:) which means we don't need to name the particular function and we can
    just say what we want the function to do which will access our phonebook_func file and we have a function in there defined as
    onSelect. So if the user goes to select it is going to call select. So user selects on an object from the list, it will call the function on select
    and in order to access that function and have it actually do the things it needs to do we need to pass in the self so its like the key to access
    everything that is in the class and the is going to be something that needs to be when we are associating it with the event listener """
    self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect (self,event))
    self.scrollbar.config(command=self.lstList1.yview)
    self.scrollbar.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky = N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky = N+E+S+W)

    # these are going to be all of the buttons that we will put in and will connect our functions to them to make them work
    # this also designs where the buttons will be located
    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command= lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky = W)
    self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command= lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8, column=1, padx=(15,0), pady=(45,10), sticky = W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command= lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8, column=2, padx=(15,0), pady=(45,10), sticky = W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command= lambda: phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8, column=4, padx=(15,0), pady=(45,10), sticky = W)

    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)

if __name__ == '__main__':
    pass

    
