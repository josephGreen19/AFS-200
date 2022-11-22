posNumber=(input("Enter a positive number "))


def onlyEvens(posNumber):
    if (int(posNumber)%2 == 0):
        onlyEvens = [evens for evens in range(int(posNumber)+1)if evens %2 ==0]
        print(onlyEvens)
    elif (int(posNumber)%2 != 0):
        onlyEvens = [evens for evens in range(int(posNumber)+1)if evens %2 ==0]
        print(onlyEvens)

while not (posNumber.isdigit()):
    posNumber = input("Invalid number, please enter valid number.")

onlyEvens(posNumber)















#def onlyEvens(posNumber):
 #   for x in range(0,posNumber+2,2):
  #      print(x)

#if posNumber <0:
 #   print(input("Invalid input. Please enter a positive number:"))
#else:
 #   onlyEvens()
