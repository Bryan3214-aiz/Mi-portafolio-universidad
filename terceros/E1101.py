# En esta versión se incluye POO
# Por cada carro vamos a almacenar tres datos
import os

# Definición de la clase
class Carro:
     # Constructor con 3 parámetros
     def __init__(self, placa, color, marca, entrada, salida):
          self.placa = placa
          self.color = color
          self.marca = marca
          self.entrada = entrada
          self.salida = salida

     # Método para marcar ingreso
     def ingresar(self, horaentrada):
          self.entrada = horaentrada

     # Método para marcar la salida
     def retirar(self, horasalida):
          self.salida = horasalida

     # Método para mostrar datos del carro
     def informe(self):
          print("El vehículo placa " + self.placa + " entro a las " + self.horaentrada + " y salió a las " + self.horasalida)

def LeerDatos():
     valores = []
     if os.path.exists("datos.txt"):
          
          archivo = open("datos.txt", "r")
          contenido = archivo.read()
          cadacarro = contenido.split("\n")
          cadacarro.pop()
          for i in cadacarro:
               partes = i.split(";")
               nuevocarro = Carro(partes[0], partes[1], partes[2], partes[3], partes[4])
               valores.append(nuevocarro)
          archivo.close()
     return valores


def GuardarDatos(datos):
     # Guardo todos los valores de la lista
     archivo = open("datos.txt", "w")
     # Recorrido de todo la lista
     for i in datos:
        archivo.write(i.placa + ";" + i.color + ";" + i.marca + ";" + i.entrada + ";" + i.salida + "\n")
     archivo.close()

def Ingresar(lista):
     # Verificar que hay espacio
     if len(lista) < 12:
          control = 0
          # Solicitar la placa, el color y la marca
          placa = input("Ingrese su placa: ")
          color = input("Ingrese el color: ")
          marca = input("Ingrese la marca: ")
          entrada = input("Ingrese la hora de entrada: ")
          salida = input("Ingrese la hora de entrada: ")
          # Verifica que no existan duplicadas
          for i in lista:
               if i.placa == placa:
                    print("Atención: Placa repetida, puede ser un fraude")
                    control = 1
          # Si no hay duplicadas, la agrega
          if control == 0:
               nuevocarro = Carro(placa, color, marca, entrada, salida)
               lista.append(nuevocarro)
               print("Carro agregado correctamente...")
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
              if lista[i].placa == placa:
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
    # Mostrar la información completa
    for i in lista:
        print("Placa:", i.placa, ", color:", i.color, ", marca:", i.marca, "Hora de entrada: ", i.entrada, "Hora de salida: ", i.salida)

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
