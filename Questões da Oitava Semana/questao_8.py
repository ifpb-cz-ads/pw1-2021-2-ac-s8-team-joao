def procurarString(s, lista):
    return s in lista


lista = ["Computador",  "Celular", "Tablet", "Televisão"]

print(procurarString("Computador", lista))
print(procurarString("Celular", lista))
print(procurarString("Tablet", lista))
print(procurarString("Televisão", lista))
print(procurarString("Geladeira", lista))