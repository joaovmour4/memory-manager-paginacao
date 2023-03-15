from process import Process
from memory import Memory

memory = Memory()
process = []

for i in range(0, 7):
    process.append(Process(memory.dict))

memory.printMemory()

