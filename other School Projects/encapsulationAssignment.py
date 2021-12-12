""" Here we have a class that is going to use a private and a protected variable
where the protected variable is basically going to use a single '_' and is letting
us know to not use the variable or function outside of the class and the private one
is harder to access than the protected but can still be done with a bit more coding
and the Private uses '__' to make it Private."""
class Protected:
    def __init__(self):
        self.__number = 7
    # when this is called will get the private var that we made above
    def getPrivateNumber(self):
        print(self.__number)
    # this makes it so we can access the Private var and then change it later when called and we pass in an argument
    def changePrivateNumber(self, private):
        self.__number = private

    def __blankStr__(self):
        self.protectedVar = ''
# we set sentence equal to our class
sentence = Protected()
# we then access the method and pass in our string we wanted printed
sentence.protectedVar = 'Hello World!'
# we then print our new string
print(sentence.protectedVar)

# we set obj to equal the class
obj = Protected()
# we then go in and access the getPrivateNumber method to print the number
obj.getPrivateNumber()
# we then call the changePrivateNumber method and put in our arugment to change the Private var
obj.changePrivateNumber(17)
# then we call this method again to get the new answser we passed in above
obj.getPrivateNumber()