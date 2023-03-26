from tkinter import *

class Memory:
    def __init__(self, frame):
        self.dict = {}
        self.insertMemory(20)
        self.frame = frame


    @staticmethod
    def verifyMemory(memory, size):
        aux = 0
        for elemento in memory.keys():
            if memory[elemento] != ' ':
                aux = 0
            else:
                aux += 1
                if aux == size:
                    return elemento - (size - 1)

    def printMemory(self):
        lbls = []
        row = 1
        column = 0
        if len(lbls) == 0:
            for elemento in self.dict.keys():
                Label(self.frame, text=str(elemento), borderwidth=1, background='blue', fg='white').grid(row=row, column=column,
                                                                                     padx=(10,0), pady=3, sticky=W)
                lbl = Label(self.frame, text=f'{self.dict[elemento]}',
                            width=5, height=1, borderwidth=1, relief='solid')
                lbls.append(lbl)
                lbl.grid(row=row, column=column+1, pady=2, padx=(0,40))
                column += 2
                if column >= 10:
                    column = 0
                    row += 1
        else:
            for elemento in self.dict.keys():
                lbls[elemento].grid_remove()
                lbls[elemento]['text'] = f'{self.dict[elemento]}'
                lbl.grid(row=row, column=column+1, pady=2, padx=10)
                column += 2
                if column >= 10:
                    column = 0
                    row += 1

    def insertMemory(self, qtElement):
        for i in range(0, qtElement):
            self.dict[i] = ' '
