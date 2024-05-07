class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)
        for i in range(fim-1):
            posicao_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_minimo]:
                    posicao_minimo = j
            
            lista[i], lista[posicao_minimo] = lista[posicao_minimo], lista[i]

        return lista
    
    def insertion_sort(self, lista):

        for i in range(1, len(lista)):  
            chave = lista[i]
            j = i - 1
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave

        return lista

    def bubble_sort(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        return lista
    
    def merge_sort(self, lista):
        if len(lista) <= 1:
            return lista

        meio = len(lista) // 2

        lado_esquerdo = self.merge_sort(lista[:meio])
        lado_direito = self.merge_sort(lista[meio:])

        return self.merge(lado_esquerdo, lado_direito)
    
    def merge(self, lado_esquerdo, lado_direito):
        if not lado_esquerdo:
            return lado_direito
        
        if not lado_direito:
            return lado_esquerdo
        
        if lado_esquerdo[0] < lado_direito[0]:
            return [lado_esquerdo[0]] + self.merge(lado_esquerdo[1:], lado_direito)
        
        return [lado_direito[0]] + self.merge(lado_esquerdo, lado_direito[1:])
