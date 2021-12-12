# this needs to be imported to make abstract methods or to do abstract classes
from abc import ABC, abstractmethod

# here is our class getting the methods from the ABC class
class Phone(ABC):
    def phonePrice(self, amount):
        print("The total phone amount is: ", amount)

    # this function is telling us to pass in an argument, but we won't be saying
    # what kind of data it will be and this allows our CreditCardPayment class to access this method and pass in its own info
    @abstractmethod
    def payment(self, amount):
        pass
# here we make a card class to get a payment and what form of payment and it has access to the other methods from the Phone class
class CreditCardPayment(Phone):
    # here we will define how to implement a function from its parent phonePrice class
    def payment(self, amount):
        print("We do deeply apologize, however you may not get this phone as your Credit Card limit is only {}.".format(amount))

class DebitCardPayment(Phone):
    def payment(self, amount):
        print("Your card had {} in it and so you were able to purchase your new phone using your Debit Card!".format(amount))

# we set this var to equal our class
obj = CreditCardPayment()
# we then pass in an amount for the method in Phone class 
obj.phonePrice("$1,100")
# we then enter an amount for the method in the card payment class
obj.payment("$1,000")

obj2 = DebitCardPayment()
obj2.phonePrice("$1,100")
obj2.payment("$1,100")

""" Good example of how these abstractionMethods work is from the example in the bootcamp, You may use
this abstractionMethods if you are needing to run different payment options because each payment option 
is going to process differently acocording to how the banks process them and so the abstractionMethod can let us make multiple
classes other than the CreditCardPayment class like shown above"""