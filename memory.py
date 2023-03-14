class Memory:
    def __int__(self):
        self.memory = {}
        for i in range(0, 20):
            self.memory[i] = '-'

    def verifyMemory(self, size):
        aux = 0
        for elemento in self.memory.keys():
            if self.memory[elemento] != '-':
                aux = 0
            else:
                aux += 1
                if aux == size:
                    return elemento - (size - 1)