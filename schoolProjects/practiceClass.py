""" Here we made a basic Enemy class to have a min attack strength
full health and min blocking """
class Enemy:
    attackStrength = 10
    health = 100
    block = 5
# this inherits the attributes above and then adds some of its own to fit
# more of what a dragon can do
class Dragon(Enemy):
    attackStrength = 15
    wingSpan = '50ft'
    wingAttack = 15
    fireAttack = 20
# this inherits the Enemy attributes as well but also can regenerate its health and has archery skills
class Skeleton(Enemy):
    healthRegenration = True
    archerySkill = 60

# we make a dragon object
dragon = Dragon()
# we then print some of the attributes the dragon object has
print(dragon.attackStrength)
# create a skeleton object
skeleton1 = Skeleton()
# we then print some of the attributes the skeleton object has
print(skeleton1.archerySkill)

class Hero:
    attack = 15
    health = 100
    block = 7

    def senario(self):
        msg = "\nThe Hero attacks the dragon and does {} damage!\nThe dragon then uses it's fire attack,\nbut the hero blocks it and\nhis health still stays at {}".format(self.attack, self.health)
        return msg
        
if __name__ == '__main__':
    thor = Hero()
    print(thor.senario())
    print(thor.health)

# This is the parent class that sets the main attribues and lets you create a new user
class User:
    name = None
    email = None
    password = None

    def createUser(self):
        enterName = input("Please enter in your new user name:\n")
        enterEmail = input("Please put in your email:\n")
        enterPassword = input("Please enter in a new password:\n")

# this is a child class inheriting the attributes of the parent but with new info from the new user created
class User1(User):
    name = 'cracken23'
    email = 'cracken23@gmail.com'
    password = '1234567a'
    followers = '100'
    videos = '250'

    def getLogInInfo(self):
        enterName = input("\nPlease enter in your user name:\n ")
        enterEmail = input("Please put in your email:\n ")
        enterPassword = input("Please enter in your password:\n ")
        if (enterEmail == self.email and enterPassword == self.password):
            print("Welcome back {}!".format(enterName))
        else:
            print("Either the email or passowrd was entered in wrong.")

# this is another child inheriting from the parent, but this one also has a method giving some info about jack frost.
class User2(User):
    name = 'Jackfrost24'
    email = 'winteriscoming@yahoo.com'
    combination = 'winterwonderland'
    secretPower = 'winter storms'
    weakness = 'Sun light'

    def winter(self):
        enterName = input("\nPlease enter in your user name:\n ")
        enterEmail = input("Please put in your email:\n ")
        enterCombination = input("Please enter in your password:\n ")
        if (enterEmail == self.email and enterCombination == self.combination):
            print("Welcome back {}!".format(enterName))
        else:
            print("Either the email or passowrd was entered in wrong.")

    def aboutJack(self):
        msg = "\nJack frost is a powerful man.\nHe is able to use his secret power to creat {}.\nHowever, his biggest weakness is {}.\n"\
            .format(self.secretPower, self.weakness)
        return msg

if __name__ == '__main__':
    spencer = User1()
    spencer.getLogInInfo()

    jack = User2()

    jack.winter()
    print(jack.aboutJack())

