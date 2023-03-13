def inserir(processo, lista):
    for endereco in processo:
        lista.remove(endereco)
    for i in range(len(lista)):
        if lista[i] > processo[len(processo)-1]:
            if i != 0:
                lista.insert(i-1, processo)
                break
            else:
                lista.insert(0, processo)


memory = [i for i in range(0, 100)]

process = [i for i in range(10, 14)]

inserir(process, memory)

process = [i for i in range(14, 20)]

# inserir(process, memory)

print(memory)