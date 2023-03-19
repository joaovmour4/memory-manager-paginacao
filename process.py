import random
import string
from tkinter import *
from memory import Memory

class Process:
    def __init__(self, memory):
        self.id = random.choice(string.ascii_uppercase)
        self.size = random.randint(1, 5)
        self.posInit = Memory.verifyMemory(memory, self.size)
        self.time = random.randint(1, 3)
        self.insertDict(memory)

    def insertDict(self, memoryDict):
        if type(self.posInit) == int:
            for i in memoryDict.keys():
                if i == self.posInit:
                    for x in range(self.posInit, self.posInit + self.size):
                        memoryDict[x] = self.id
        else:
            # msg = Message(self.root)
            # msg.showinfo(title='teste', message=f'O processo {self.id} não foi alocado por falta de memória!')
            print(f'O processo {self.id} não foi alocado por falta de memória!')

    def removeDict(self, memoryDict):
        for i in memoryDict.keys():
            if i == self.posInit:
                for x in range(self.posInit, self.posInit + self.size):
                    memoryDict[x] = '-'

    def __str__(self) -> str:
        r = f'ID: {self.id}, Tamanho: {self.size}'
        return r