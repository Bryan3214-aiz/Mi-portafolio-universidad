
def mostrar_letras ():
    nombre_letra = list(nombre)
    for nombre_letra in nombre:
        print (nombre_letra)

def mostrar_tamaño ():
    tamaño = len(nombre)
    print ("El tamaño es:",tamaño)

def ciclo_libre():
    cantidad_ingresadas= int(input("Ingrese cuantas veces desea mostrar su nombre: "))
    cantidad_repeticiones = 0
    while cantidad_repeticiones < cantidad_ingresadas:
        print(nombre)
        cantidad_repeticiones = cantidad_repeticiones + 1


nombre = input("Ingrese su nombre completo: ")

opcion = 1
while opcion != 0:
     opcion = int(input("1. Mostrar letra\n2. Mostrar el tamaño\n3. Ciclo libre\n0. Salir: "))
     if opcion == 1:
          mostrar_letras()
     elif opcion == 2:
          mostrar_tamaño()
     elif opcion == 3:
          ciclo_libre()
     else:
          print("Gracias por usar el programa.")