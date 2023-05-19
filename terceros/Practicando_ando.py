
#CREAR UN TUPLA POR MEDIO DE LA FUNCION ZIP, POR MEDIO DE DOS LISTAS CON LA MISMA LONGITUD.
# nombre = ["Bryan","Leiva","Pedro"]
# edades = [20,21,130]
# combinados = list(zip(nombre,edades))
# print(combinados)
# agregar = int(input("Ingrese el valor que quiere agregar: "))
# edades.append(agregar)
# eliminar = int(input("Ingrese el valor que quiere eliminar: "))
# edades.remove(eliminar)
# print(edades) #LOGRADO

#SUMA DE DOS NUMEROS.
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese un numero: "))
# suma = num1 + num2
# print(f"El resultado es: {suma}") #LOGRADO

#CALCULAR AREA DE UN TRIANGULO.
# base = int(input("Ingrese la base del triangulo: "))
# altura = int(input("Ingrese la altura del triangulo: "))
# calcular_area = (base*altura)//2
# print(f"El area del triangulo es: {calcular_area}") #LOGRADO

# NUMEROS PARES
# for i in range(101):
#     if i % 2 == 0:
#        print(i) #LOGRADO

#CONTADOR DE PALABRAS
# frase = input("Escriba una frase: ")
# contador_palabras = len(frase)
# print(contador_palabras) #LOGRADO

#CREAR NUMERO ALEATORIO Y QUE EL USUARIO ADIVINE.

# import random

# numero_aleatorio = random.randint(1, 10)
# numero_usuario = int(input("Ingrese un numero: "))
# if numero_usuario > numero_aleatorio:
#     print("Muy alto, intentalo de nuevo.")
# elif numero_usuario < numero_aleatorio:
#     print("Muy bajo, intentalo de nuevo.")
# elif numero_usuario == numero_aleatorio:
#     print("Felicidades, has adivinado el numero.")
# print(f"Este era el numero aleatorio: {numero_aleatorio}") #LOGRADO

#CALCULAR LOS VALORES DE X y Y.
# valorX = int(input("Ingrese el valor de x: "))
# if valorX < 0:
#     Y = 3 * valorX + 6
#     print(f"El valor de X = {valorX} y el valor de Y = {Y}")
# elif valorX >= 0:
#     Y = valorX ** 2 + 6
#     print(f"El valor de X = {valorX} y el valor de Y = {Y}")

#CALCULAR EL PRECIO DE UN TERRENO.
# largo = int(input("Ingrese el largo del terreno: ")) #Varibles para almecenar los datos que se van a utilizar para averiguar el precio.
# ancho = int(input("Ingrese el ancho del terreno: "))
# precio_metro2 = int(input("Ingrese el precio por metro cuadrado del terreno: "))

# area_terreno = largo * ancho #Averigua el area total del terreno en metros cuadrados.
# print(f"\nEl area en metros cuadrados del terreno es: {area_terreno}")

# if area_terreno >= 400 and area_terreno < 500: #Valida si el area del terreno es mayor a 400 y menor a 500.
#     precio_neto = largo * ancho * precio_metro2
#     descuento = int(precio_neto * 0.1)
#     precio_total = precio_neto - descuento 
#     print(f"El precio total del terreno aplicando un 10% de descuento es: {precio_total} millones de colones\n")
# elif area_terreno > 500 and area_terreno < 1000:
#     precio_neto = largo * ancho * precio_metro2
#     descuento = int(precio_neto * 0.17)
#     precio_total = precio_neto - descuento
#     print(f"El precio total del terreno aplicando un 17% de descuento es: {precio_total} millones de colones\n")
# elif area_terreno >= 1000:
#     precio_neto = largo * ancho * precio_metro2
#     descuento = int(precio_neto * 0.25)
#     precio_total = precio_neto - descuento
#     print(f"El precio total del terreno aplicando un 25% de descuento es: {precio_total} millones de colones\n")
# else:
#     precio_terreno = largo * ancho * precio_metro2
#     print(f"El precio total del terreno es: {precio_terreno} millones de colones\n") #LOGRADO

lista = []

cantidad = int(input("Ingrese la cantidad: "))
for x in range(cantidad):
    lista.append(x + 10)
print(lista)