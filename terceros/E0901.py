import os

def LeerDatos():
     if os.path.exists("datos.txt"):
          archivo = open("datos.txt", "r")
          contenido = archivo.read()
          valores = contenido.split("\n")
          archivo.close()
          valores.pop()
          return valores
     else:
          return []

def GuardarDatos(datos):
     # Guardo todos los valores de la lista
     archivo = open("datos.txt", "w")
     for i in datos:
        archivo.write(i + "\n")
     archivo.close()

def Ingresar(lista):
     # Verificar que hay espacio
     if len(lista) < 12:
          control = 0
          # Solicitar la placa
          placa = input("Ingrese su placa: ")
          # Verifica que no existan duplicadas
          for i in lista:
               if i == placa:
                    print("Atención: Placa repetida, puede ser un fraude")
                    control = 1
          # Si no hay duplicadas, la agrega
          if control == 0:
               lista.append(placa)
               print("Placa agregada correctamente")
     else:
          print("El parqueo está lleno")
     GuardarDatos(lista)
     return lista

def Retirar(lista):
     # Verificar que no esté vacío
     if len(lista) > 0:
          posicion = -1
          placa = input("Ingrese la placa: ")
          # Buscar posición de la placa, si existe
          for i in range(len(lista)):
              if lista[i] == placa:
                  posicion = i
          # Si la placa existe la elimino
          if posicion >= 0:
              lista.pop(posicion)
              print("Vehículo retirado exitosamente")
          else:
               print("La placa no está dentro del parqueo")
     else:
          print("No existen vehículos en el parqueo")
     GuardarDatos(lista)
     return lista

def Reporte(lista):
    # Mostrar la cantidad de espacios disponibles
    print("Quedan", str(12 - len(lista)), "espacios disponibles")
    # Mostrar las placas existentes
    for i in lista:
        print(i)

# Comienza el programa
# Definición de la lista
espacios = []
opcion = 1
# Menú
espacios = LeerDatos()
while opcion != 0:
     opcion = int(input("1. Ingresar\n2. Retirar\n3. Reporte\n0. Salir\n"))
     if opcion == 1:
        # Llamado a la función INGRESAR, la cual envía la lista y la recibe
        espacios = Ingresar(espacios)
     elif opcion == 2:
        # Llamado a la función RETIRAR, la cual envía la lista y la recibe
        espacios = Retirar(espacios)
     elif opcion == 3:
         # Llamado a la función REPORTE, la cual envía lista
         Reporte(espacios)


