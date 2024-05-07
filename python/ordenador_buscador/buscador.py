class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return False
    
    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1 

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return False
    
    def busca_binaria_recursiva(self, lista, x, min=0, max=None):
        if max == None:
            max = len(lista) - 1

        if max < min:
            return False
        else:
            meio = (min + max) // 2

        if lista[meio] > x:
            return self.busca_binaria_recursiva(lista, x, min, meio-1)
        elif lista[meio] < x:
            return self.busca_binaria_recursiva(lista, x, meio+1, max)
        else:
            return meio
