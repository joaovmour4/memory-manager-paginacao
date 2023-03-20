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
        proc = Process(memory.dict)
        if proc.posInit:
            process.append(proc)
        memory.printMemory()
        printProcess()
        for proc in process:
            proc.time -= 1
            if proc.time == 0:
                process.remove(proc)
                proc.removeDict(memory.dict)
        sleep(1)

def printProcess():
    for i in processWidgets:
        if i['text'] not in process:
            i.grid_remove()
            processWidgets.remove(i)
    for i in range(len(process)):
        lblProcess = Label(frame, text=f'{process[i]}', borderwidth=1, relief='solid')
        processWidgets.append(lblProcess)
        lblProcess.grid(column=10, row=i+1, sticky=W, padx=5, pady=3)

root = Tk()
root.option_readfile("optionDB.txt")
frame = Frame(root)
memory = Memory(frame)
process = []
processWidgets = []


for i in range(0, 7):
    process.append(Process(memory.dict))

Label(frame, text='Memória:').grid(column=0, row=0, padx=0, pady=0, columnspan=10)


Button(frame, text='Executar', command=start).grid(column=10, row=10, sticky=W, padx=5, pady=2)  
Button(frame, text='Pause', command=stop).grid(column=11, row=10, sticky=W, padx=5, pady=2)

frame.grid()

# thread = threading.Thread(target=execute, args=(process, memory))
# thread.start()
# thread.run()

root.mainloop()