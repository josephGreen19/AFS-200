
import random
class Die:

    def __init__(self, sides=6):
        self.numOfSides= sides
        self.currentSideUp= 1

    def roll(self):
        self.currentSideUp = random.randint(1,self.numOfSides)
        return self.currentSideUp

    def getNumOfSide(self):
        return self.numOfSides

    def getCurrentSideUp(self):
        return self.currentSideUp

    def setNumOfSide(self,sides):
        self.numOfSides = sides

    def setCurrentSideUp(self,sideUp):
        self.currentSideUp = sideUp

    def showDieFace(self):
        print(f"({self.currentSideUp})")
