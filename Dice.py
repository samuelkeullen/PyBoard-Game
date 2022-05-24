import random
class Dice:
    def __init__(self, numFaces, arrayNum):
        self.numFaces = numFaces;
        self.arrayNum = arrayNum;

    def setDice(self):
        self.numFaces = 6;
        self.arrayNum = [1,2,3,4,5,6];

    def rollDice(self):
        return random.choice(self.arrayNum)