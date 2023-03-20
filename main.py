from process import Process
from memory import Memory
from time import sleep
from tkinter import *
import threading

condition = False

def start():
    global condition
    if not condition:
        condition = True
        thread = threading.Thread(target=execute, args=(process, memory))
        thread.start()

def stop():
    global condition
    condition = False

def execute(process, memory):
    while condition:
        memory.printMemory()
        printProcess()
        for proc in process:
            proc.time -= 1
            if proc.time == 0:
                process.remove(proc)
                proc.removeDict(memory.dict)
        sleep(2)

def addProcess(process, memory):
    proc1 = Process(memory.dict, frame)
    if proc1.posInit:
        process.append(proc1)

def printProcess():
    for i in range(len(process)):
        process[i].label.grid(column=10, row=i+1, sticky=W, padx=5, pady=3)

root = Tk()
root.title('Gerenciador de memória')
root.option_readfile("optionDB.txt")
root.geometry('805x150')
root.resizable(False,False)
frame = Frame(root)
memory = Memory(frame)
process = []
processWidgets = []

memory.printMemory()
printProcess()

Label(frame, text='Memória:').grid(column=0, row=0, padx=0, pady=0, columnspan=10)
Label(frame, text='Processos:').grid(column=10, row=0, padx=0, pady=0)


Button(frame, text='Executar', command=start).grid(column=10, row=10, sticky=W, padx=5, pady=2)  
Button(frame, text='Pause', command=stop).grid(column=11, row=10, sticky=W, padx=5, pady=2)
Button(frame, text='Add processo', command=lambda:addProcess(process, memory)).grid(column=12, row=10,
                                                                                    sticky=W, padx=5, pady=2)

frame.grid()
root.mainloop()