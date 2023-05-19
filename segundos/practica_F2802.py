#programa de numeros.

numeros = 1
cantidad = 0

while cantidad <= 100:
    if numeros % 2 == 0 and numeros % 5 == 0 and numeros % 10:
        cantidad += 1 
        print (numeros)
    numeros += 1