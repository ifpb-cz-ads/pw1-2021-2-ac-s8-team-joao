def listaString(listString):
    converterString = list(listString)
    contador = 0
    minimo = 5
    maximo = 10
    veracidade = False
    
    while contador < len(converterString):
        contador = contador + 1
    
    if(contador >= minimo and contador <= maximo):
        veracidade = True
        print(veracidade)
    else:
        print(veracidade)
        
stringLista = input('Digite a palavra: ')

listaString(stringLista)