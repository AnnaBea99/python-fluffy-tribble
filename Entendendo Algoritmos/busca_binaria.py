class BinarySearch():
    
    def pesquisa_binaria(self, lista, item):
        baixo = 0
        alto = len(lista) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = lista[meio]
            if chute == item:
                return meio
            if chute > item:
                alto = meio - 1
            else:
                baixo = meio + 1
        return None 


    def pesquisa_recursiva(self, lista, baixo, alto, item):
        if alto >= baixo:

            meio = (alto + baixo) // 2
            chute = lista[meio]

            if chute == item:
                return meio
            elif chute > item:
                return self.pesquisa_recursiva(lista, baixo, meio -1, item)
            else:
                return self.search_recusiva(lista, meio + 1, alto, item)
        else:
                return None



if __name__ == "__main__":
    bs = BinarySearch()
    minha_lista = [1,3,5,7,9]     

    print (bs.pesquisa_binaria(minha_lista, 3))
    print (bs.pesquisa_binaria(minha_lista, -1))