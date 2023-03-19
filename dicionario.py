from process import Process
from memory import Memory
from time import sleep
from tkinter import *
import os

def execute(root, process, memory):
    process.append(Process(memory.dict))
    memory.printMemory(root)
    for proc in process:
        proc.time -= 1
        if proc.time == 0:
            proc.removeDict(memory.dict)
            process.remove(proc)

def printProcess():
    for i in range(len(process)):
        Label(root, text=f'{process[i]}', borderwidth=1, relief='solid').grid(column=10, row=i+1, sticky=W, padx=5, pady=3)

root = Tk()
memory = Memory()
process = []


for i in range(0, 7):
    process.append(Process(memory.dict))

Label(root, text='Memória:').grid(column=0, row=0, padx=0, pady=0, columnspan=10)

memory.printMemory(root)

Button(root, text='Executar', command=lambda:[execute(root, process, memory),printProcess()]).grid(column=10, row=10, sticky=W, padx=5, pady=5)  

root.mainloop()