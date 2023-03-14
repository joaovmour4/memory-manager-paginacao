import random, string

class Process:
    def __int__(self):
        self.id = random.choice(string.ascii_letters)
        self.size = random.randint(1, 5)
        self.posInit = None
