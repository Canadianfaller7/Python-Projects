myAnimalList = ['kiara', 'kovue', 'rue', 'joey', 'ginger', 'toothless', 'maggie', 'annie']
myAnimalList.sort()
print(myAnimalList)

name = input("What is your name? : ")
print("Hello " + name +"! lets find out how long you have been alive for in months and years!")

age = int(input("How old are you now? : "))
print("You are ", age, " years old")

year = age * 1
months = age * 12
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print("You have been alive for", year, "years, or", months, "months, or", days, "days, or", minutes, "minutes, or", seconds, "seconds.")
