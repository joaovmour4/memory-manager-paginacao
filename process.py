import random
import string
from tkinter import *
from memory import Memory

class Process:
    processes = []
    def __init__(self, memory, frame):
        while True:    
            tempID = random.choice(string.ascii_uppercase)
            if tempID not in Process.processes:
                break
        self.id = tempID
        self.size = random.randint(1, 5)
        self.posInit = Memory.verifyMemory(memory, self.size)
        self.time = random.randint(1, 3)
        if self.posInit is not None:    
            self.insertDict(memory)
        Process.processes.append(tempID)
        self.label = Label(frame, text=self.__str__(), borderwidth=1, relief='solid')

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
        self.label.grid_remove()
        Process.processes.remove(self.id)

    def __str__(self) -> str:
        r = f'ID: {self.id}, Tamanho: {self.size}'
        return r