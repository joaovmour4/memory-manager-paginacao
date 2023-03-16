from tkinter import *

class Memory:
    def __init__(self):
        self.dict = {}
        self.insertMemory()


    @staticmethod
    def verifyMemory(memory, size):
        aux = 0
        for elemento in memory.keys():
            if memory[elemento] != '-':
                aux = 0
            else:
                aux += 1
                if aux == size:
                    return elemento - (size - 1)

    def printMemory(self, root):
        frame = Frame(root)
        row = 0
        column = 0
        for elemento in self.dict.keys():
            print(f'{elemento}.\t {self.dict[elemento]}', end='\t\t')
            Label(frame, text=f'{elemento}. {self.dict[elemento]}').grid(row=row, column=column, pady=10, padx=10)
            column += 1
            if column == 5:
                column = 0
                row += 1

    def insertMemory(self):
        for i in range(0, 20):
            self.dict[i] = '-'
