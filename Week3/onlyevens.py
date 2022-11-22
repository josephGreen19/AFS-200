posNumber=int(input("Enter a positive number "))

def onlyEvens():
    for x in range(0,posNumber+2,2):
        print(x)

if posNumber <0:
    print(input("Invalid input. Please enter a positive number:"))
else:
    onlyEvens()
