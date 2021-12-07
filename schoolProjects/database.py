""" Here we are creating a database with python. We import sqlite3(python libraby for sql)
and then we make a var called conn that is set to sqlite3.connect('test1.db') which will
make a database file called test and connect to it so we can then enter stuff into it
then we make a with loop for conn and then we make another var called cur that is equal to
conn.cursor and (the cursor method operates the database when commands are given) then
we do cur.execute and this is what allows us to execute the commands we want to make to our database
so we then create a table if it doesn't exist already and then give it an id of int and make it a
primary key with autoincrement so the (1,1) which means start at 1 and go up 1 each time a new row is made
and then we make a column for the file names that will be printed later and then we do the commit to save the changes
we made in the database and then we close the with loop so there are no leaks"""
import sqlite3

conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test1.db')

# list of files that we want to use in our database
fileList = ('information.docx', 'Hello.txt', 'myImage.ong', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

""" Here we make a for loop saying take the list above and find what file
ends with .txt and then we will do the with conn like before and insert the 
files ending in .txt into our database under col_fileName"""
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (x,))
            print(x)