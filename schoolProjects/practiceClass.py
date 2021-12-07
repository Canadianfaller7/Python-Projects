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