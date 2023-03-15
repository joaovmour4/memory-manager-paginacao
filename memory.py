class Memory:
    def __init__(self):
        self.dict = {}
        self.insertMemory()


    @staticmethod
    def verifyMemory(memory, size):
        aux = 0
        for elemento in memory.keys():
            if memory[elemento] != '-':
                aux = 0
            else:
                aux += 1
                if aux == size:
                    return elemento - (size - 1)

    def printMemory(self):
        aux = 0
        for elemento in self.dict.keys():
            print(f'{elemento}\t {self.dict[elemento]}', end='\t\t\t')
            aux += 1
            if aux == 5:
                print()
                aux = 0

    def insertMemory(self):
        for i in range(0, 20):
            self.dict[i] = '-'
