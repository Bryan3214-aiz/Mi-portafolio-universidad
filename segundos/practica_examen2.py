"""
Práctica para el exámen - Sebastián Mora Rodríguez
"""
import os

# clase


class Cliente:
    def __init__(self, nombre, correo, cel):
        self.nombre = nombre
        self.correo = correo
        self.cel = cel


# archivo de text


def leer_datos():
    datos = []
    if os.path.exists("teatro.txt"):
        archivo = open("teatro.txt", "r")
        contenido = archivo.read()
        cada_cliente = contenido.split("\n")
        cada_cliente.pop()
        for i in cada_cliente:
            sitios = i.split(";")
            nuevo_cliente = Cliente(sitios[0], sitios[1], sitios[2])
            datos.append(nuevo_cliente)
        archivo.close()
    return datos


def guardar_datos(datos):
    archivo = open("teatro.txt", "w")
    for i in datos:
        archivo.write(i.nombre + ";" + i.correo + ";" + i.cel + "\n")
    archivo.close()


# funciones por zona

def zona_popular(popular):
    if len(popular) < 15:
        # solicitar los requisitos
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        cel = input("Teléfono: ")
        nuevo_cliente = Cliente(nombre, correo, cel)
        popular.append(nuevo_cliente)
        print("¡Bienvenido!")
    else:
        print("Popular lleno")
    guardar_datos(popular)


def zona_preferencial(preferencial):
    if len(preferencial) < 15:
        # solicitar los requisitos
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        cel = input("Teléfono: ")
        nuevo_cliente = Cliente(nombre, correo, cel)
        preferencial.append(nuevo_cliente)
        print("¡Bienvenido!")
    else:
        print("Preferencial lleno")
    guardar_datos(preferencial)


def zona_vip(vip):
    if len(vip) < 10:
        # solicitar los requisitos
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        cel = input("Teléfono: ")
        nuevo_cliente = Cliente(nombre, correo, cel)
        vip.append(nuevo_cliente)
        print("\n¡Bienvenido!")
    else:
        print("VIP lleno")
    guardar_datos(vip)

# funciones principales


def ingresar(popular, preferencial, vip):
    # verificar la capacidad del teatro
    if len(popular) + len(preferencial) + len(vip) < 40:
        # verificar la capacidad de cada zona
        print("\n----\n1. Popular\n2. Preferencial\n3. VIP\n----\n")
        zona = int(input("Zona: "))
        if zona == 1:
            zona_popular(popular)
        elif zona == 2:
            zona_preferencial(preferencial)
        elif zona == 3:
            zona_vip(vip)
    else:
        print("El teatro se encuentra lleno")


def retirar():
    pass


def consultar():
    pass


# listas de zonas
popular = []
preferencial = []
vip = []

# menu
espacios = leer_datos()
while True:
    print("\n---Teatro La Carcajada---\n")
    print("1. Ingresar")
    print("2. Retirar")
    print("3. Consultar")
    print("0. Salir")
    opcion = int(input("\nIngrese una opción: "))
    if opcion == 1:
        ingresar(popular, preferencial, vip)
    elif opcion == 2:
        retirar()
    elif opcion == 3:
        consultar()
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción correcta.")
