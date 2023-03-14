from process import Process
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

for i in range(0, 20):
    memory[i] = '-'

p1 = Process()
p1.size = 3
p1.id = 'A'
p1.posInit = verifyMemory(memory, p1.size)

for i in memory.keys():
    if i == p1.posInit:
        for x in range(p1.posInit, p1.posInit+p1.size):
            memory[x] = p1.id

p2 = Process()
p2.size = 5
p2.id = 'B'
p2.posInit = verifyMemory(memory, p2.size)

for i in memory.keys():
    if i == p2.posInit:
        for x in range(p2.posInit, p2.posInit+p2.size):
            memory[x] = p2.id

aux = 0
for elemento in memory.keys():
    print(f'{elemento}\t {memory[elemento]}', end='\t\t\t')
    aux+=1
    if aux == 5:
        print()
        aux = 0

# print(verifyMemory(memory, 4))

