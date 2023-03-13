def inserir(processo, lista):
    for i in range(len(lista)):
        if type(lista[i]) == int:
            if lista[i] == processo[0]:
                    lista.insert(i, processo)
                    break
                    lista.insert(0, processo)
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
        


memory = [i for i in range(0, 100)]

process = [i for i in range(10, 14)]

inserir(process, memory)

process = [i for i in range(14, 20)]

inserir(process, memory)

process = [i for i in range(0, 10)]

inserir(process, memory)


print(memory)

print(verificar_espaco(8, memory))
