#Programa realizado por Bryan Leiva.

#Numeros primos
numero = int(input("Ingresa un numero: "))
x = 1
y = 0
#Ciclo para averiguar si el numero ingresado es primo
while x <= numero:
    if numero % x == 0 and numero // numero == 1: #Si la division es exacta y es igual a 0 es primo
        y += 1
    #Se aumenta la variable de control tantas veces como se repita el ciclo y asi evitar un bucle infinito.
    x += 1 
if y == 2: 
    print(f"\nEl numero {numero} es primo.\n")
else:
    print(f"\nEl numero {numero} no es primo.\n")