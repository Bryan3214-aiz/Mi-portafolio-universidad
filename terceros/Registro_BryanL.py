import os 

class usuario:
    def __init__(self, nombre, correo, contrasena):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

def registrarse(Vdatos_usuario):
    if len(Vdatos_usuario) < 1:
        print("\n---INGRESA TUS DATOS PERSONALES---")
        nombre = input("Nombre: ")
        correo = input("Correo electronico: ")
        contrasena = input("Contraseña: ")
        nuevo_usuario = usuario(nombre,correo,contrasena)
        Vdatos_usuario.append(nuevo_usuario)
    else:
        print("\nYa se encuentra un usuario registrado")

def editar_informacion(Vdatos_usuario):
    if len(Vdatos_usuario) < 1:
        editar = int(input("\n¿Qué deseas hacer?\n1. Editar información\n2. Borrar información\nOpcion elegida: "))
        if editar == 1:
            editar_datos = int(input("\n¿Qué deseas hacer?\n1. Editar nombre\n2. Editar correo\n3. Editar contraseña\nOpcion elegida: "))
            if editar_datos == 1:
                nombre = input("Nombre: ")
                for i in range(len(Vdatos_usuario)):
                    if Vdatos_usuario[i].nombre == nombre:
                        Vdatos_usuario.append

            elif editar_datos == 2:
                None
            elif editar_datos == 3:
                None
            
        elif editar == 2:
            None
    else:
        print("\nNo hay usuarios registrados.")

#lista 
Vdatos_usuario = []
#funcion para leer los documentos que se hayan creado y recopilar la informacion si se comprueba su existencia.

#Menu principal
menu = 1
while menu != 4:
    menu = int(input("\nBienvenido a UH digital, de acuerdo con las siguientes opciones eliga una.\n1. Registrarse\n2. Editar información\n3. Ver información\n4. Salir\nOpción elegida: "))
    if menu == 1:
        registrarse(Vdatos_usuario)
    elif menu == 2:
        editar_informacion(Vdatos_usuario)
    elif menu == 3:
        ver_informacion(Vdatos_usuario)
    else:
        print("\nHasta la proxima, esperamos que haya sido de tu agrado el entorno estudiantil UH :)\n")
