def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:  
            return x
    return None
    
lista = [4, 7, 12, 47, 61]
valor = int(input('Digite o valor que está procurando: '))
pesquisar = pesquise(lista, valor)

print('A posição do número pesquisado é:', pesquisar)