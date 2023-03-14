import random, string

class Process:
    def __int__(self):
        self.id = random.choice(string.ascii_letters)
        self.size = random.randint(1, 5)
        self.posInit = None

    def insertDict(self, memoryDict):
        for i in memoryDict.keys():
            if i == self.posInit:
                for x in range(self.posInit, self.posInit + self.size):
                    memoryDict[x] = self.id