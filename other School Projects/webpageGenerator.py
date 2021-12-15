import webbrowser
from tkinter import *
import tkinter as tk

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
        # this is the title in the tkinter window
        self.master.title("The Tkinter Web Page Demo")
        # this is a lable telling the user what to do
        self.lbl_fname = tk.Label(self.master, text='Enter in what you want to say on your website: ')
        # these are just locations of where the label will sit
        self.lbl_fname.grid(row=0, column=0, padx = (20,0), pady=(10,0), sticky = N+W)
        # this is where the user will input their message of what they want the website to have inside the body tag
        self.txt_1 = tk.Entry(self.master, text = 'Input body for your webpage!')
        self.txt_1.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky = N+E+W)
        # this is where we put the button to run our openWeb function and to run everything inside and to execute it and show up when the button is pressed
        self.btn_add = tk.Button(self.master, width=12, height=2, text='Create Site', command = lambda: openWeb(self))
        self.btn_add.grid(row=8, column=0, padx=(25,0), pady=(45,10), sticky = W)

# this is the part for the HTML code that will show up when we click the button
# we make a function and put self so it can work and also get the info from above
def openWeb(self):
    # we then make these var's to keep in our html code and layer them the way they need to be set up to run properly
    htmlTop = """
    <html>
        <body>
            <h1>Stay tuned for our amazing summer sale!</h1>
        """ 
    # this will get the text that is typed into the GUI
    htmlMiddle = self.txt_1.get()
    # this is just the closing tags for the html
    htmlBottom = """
        </body> 
    </html> 
    """
    # here we use the webbrowser library to make our index.html file and write it and then we due the file.write method
    # and pass in our vars to make them all as one
    with open("index.html", "w") as file:
        file.write(htmlTop + htmlMiddle + htmlBottom)
    # we then assign index.html file to a var
    url = "index.html"
    # this code calls to open the url and what is inside it when we press the button, it will open default browser and a new tab for the user
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    # this creates the window from the tkinter
    root = tk.Tk()
    # this is our app we are calling our class the app and attached the root
    # basically this is the syntax required by tkinter in order to create the window and pass it to our class
    App = ParentWindow(root)
    # this is to make it so the app doesn't close right away
    root.mainloop()


