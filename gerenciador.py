from processo import Processo

def inserir(processo, lista):
    for i in range(len(lista)):
        if type(lista[i]) == int:
            if lista[i] == processo[0]:
                    lista.insert(i, processo)
                    break
    for endereco in processo:
        lista.remove(endereco)

def verificar_espaco(size, array):
    sizeAux = 0
    for i in array:
        if type(i) != list:
            sizeAux += 1
        else:
            sizeAux = 0
        if sizeAux == size:
            return i - (size-1)
    return False

def arrPrint(array):
    column=0
    for element in array:
        if type(element) == int:
            print(element, end='\t')
            column+=1
        else:
            print('[', end='')
            for listElement in element:
                print(listElement, end='\t')
                column+=1
                if column > 7:
                    print('\n', end='')
                    column=0
            print(']', end='')
        if column > 7:
            print('\n', end='')
            column=0
        


memory = ['-' for i in range(0, 64)]
arrProcess = []


arrProcess.append(Processo.insertList(arrProcess))
arrProcess.append(Processo.insertList(arrProcess))


column = 0

for adrMemory in range(len(memory)):
    for process in arrProcess:
        if process.locInit == adrMemory:
            for i in range(process.locInit, process.locInit + process.size):
                memory[i] = process.id
    print(memory[adrMemory], end='\t')
    column+=1
    if column == 8:
        column=0
        print()

print(arrProcess[0].locInit, arrProcess[0].size)
    

# print(verificar_espaco(8, memory))
