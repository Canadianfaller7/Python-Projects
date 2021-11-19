#create variable with an integar and request input
numInput = int(input('Gimme a number: '))
#create a function with argument that takes the input number and creates a result and prints string
def celsiusToFarenheit(numInput):
    result = (numInput * 9/5) + 32
    print(str(numInput), 'degrees celsius converted to farenheit equals', str(result))
#print adds space
print(" ")
#call funtion with argument in it
celsiusToFarenheit(numInput)

