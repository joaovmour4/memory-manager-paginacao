from process import Process
from memory import Memory
from time import sleep
from tkinter import *
import os

root = Tk()

memory = Memory()
process = []

for i in range(0, 7):
    process.append(Process(memory.dict))

while True:
    process.append(Process(memory.dict))
    memory.printMemory()
    for proc in process:
        proc.time -= 1
        if proc.time == 0:
            proc.removeDict(memory.dict)
            process.remove(proc)
    sleep(2)
    os.system('cls')

root.mainloop()
