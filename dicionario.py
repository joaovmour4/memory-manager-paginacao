from process import Process
from memory import Memory
import random, string

def verifyMemory(memory, size):
    aux = 0
    for elemento in memory.keys():
        if memory[elemento] != '-':
            aux = 0
        else:
            aux += 1
            if aux == size:
                return elemento - (size-1)


memory = {}
memoryTest = Memory()
memoryTest.insertMemory()

for i in range(0, 20):
    memory[i] = '-'

p1 = Process()
p1.size = 3
p1.id = 'A'
p1.posInit = verifyMemory(memory, p1.size)

p1.insertDict(memory)

p2 = Process()
p2.size = 5
p2.id = 'B'
p2.posInit = verifyMemory(memory, p2.size)

p2.insertDict(memory)

aux = 0
for elemento in memory.keys():
    print(f'{elemento}\t {memory[elemento]}', end='\t\t\t')
    aux+=1
    if aux == 5:
        print()
        aux = 0

print('\n\n')

# memoryTest.printMemory()
print(memoryTest.dict)
# print(verifyMemory(memory, 4))

