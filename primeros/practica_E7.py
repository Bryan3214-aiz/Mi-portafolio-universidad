#Programa para numeros pares.

numeros_ingresados = 0
contador_numeros_ingresados = 0

for i in range (0,10):
    numeros_ingresados= int(input("Ingrese 10 numeros: "))
    if numeros_ingresados % 2 == 0: 
        contador_numeros_ingresados = contador_numeros_ingresados + (numeros_ingresados + 1)       
print ("La cantidad de numeros par que se ingresaron es: ",contador_numeros_ingresados)