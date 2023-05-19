from cryptography.fernet import Fernet
from pathlib import Path
import os 

def generador_claves():
    archivo = r'key.key'
    objeto_archivo = Path(archivo)
    if not objeto_archivo.is_file():
        clave = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(clave)
def cargar_clave():
    return open("key.key", "rb").read()

def encriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo,"rb") as file:
        datos = file.read()
        datos_encriptados = f.encrypt(datos)
        with open(archivo, "rb") as file:
            file.write(datos_encriptados)

def Leer_datos():
    if os.path.exists("Datos_usuario.txt"): #Utilizando funciones con el modulo del sistema operativo se comprueba si existen documentos con la extension que esta entre parentesis.
        archivo = open("Datos_usuario.txt", "r") 
        contenido = archivo.read()
        datos_encontrados = contenido.split("\n")
        archivo.close()
        datos_encontrados.pop()
        return datos_encontrados
    else:
        return [] #Si no existe ningún documento se retorna una lista vacía
    
def Guardar_datos():
    archivo = open("Datos_usuario.txt", "w") #Se crea un archivo en el cual se van escribir todos los datos ingresados por el usuario.
    for i in Vdatos_usuario:
        archivo.write(i + "\n")
    archivo.close()

def registrarse(): #Registra al nuevo usuario.
    nombre = input("\nNombre usuario: ")
    Vdatos_usuario.append(nombre)
    print("\nUsuario registrado correctamente\n")
    contrasena = input("Contraseña: ")
    Vdatos_usuario.append(contrasena)
    print("\nContraseña registrada correctamente")

def editar_informacion(): #Modifica los datos ya registrados.
    eleccion = int(input("\n¿Qué desea editar?\n1. Usuario\n2. Contraseña\n3. Cambiar ambos datos\n4. Borrar información\n5. Volver al menu principal\nOpcion elegida: ")) 
    if eleccion == 1:
        nombre = input("\nNombre usuario: ")
        if nombre in Vdatos_usuario:
            print("\nEl nombre ingresado ya esta registrado.")
        else:
            Vdatos_usuario[0] = nombre
            print("\nNuevo nombre registrado correctamente")
    elif eleccion == 2:
        contrasena = input("\nContraseña: ")
        if contrasena in Vdatos_usuario:
            print("\nLa contraseña ingresada ya esta registrada.")
        else:
            Vdatos_usuario[1] = contrasena
            print("\nLa nueva contraseña fue registrada correctamente")
    elif eleccion == 3:
        nombre = input("\nNombre usuario: ")
        if nombre in Vdatos_usuario:
            print("\nEl nombre ingresado ya esta registrado.\n")
        else:
            Vdatos_usuario[0] = nombre
            print("\nNuevo nombre registrado correctamente\n")
        contrasena = input("Contraseña: ")
        if contrasena in Vdatos_usuario:
            print("\nLa contraseña ingresada ya esta registrada.")
        else:
            Vdatos_usuario[1] = contrasena
            print("\nLa nueva contraseña fue registrada correctamente")
    elif eleccion == 4:
        nombre = input("\nNombre usuario: ")
        if nombre in Vdatos_usuario:
            Vdatos_usuario.remove(nombre)
            print("\nEl nombre ingresado fue eliminado correctamente\n")
        else:
            print("\nEl nombre ingresado no esta registrado.\n")
        contrasena = input("Contraseña: ")
        if contrasena in Vdatos_usuario:
            Vdatos_usuario.remove(contrasena)
            print("\nLa contraseña ingresada fue eliminada correctamente")
        else:
            print("\nLa contraseña ingresada no esta registrada.")
    
def ver_informacion(): #Se verifica si existen datos y si es así se muestran en pantalla.
    if len(Vdatos_usuario) > 0: #Verifica si existen datos registrados en la lista.
            print(f"\nNombre de usuario: {Vdatos_usuario[0]}\nContraseña: {Vdatos_usuario[1]}")
    else:
        print("\nNo se han registrado datos todavia.")

#lista
Vdatos_usuario = []
#funciones para leer los documentos con extension txt.
archivo = "Archivo.txt"
clave = cargar_clave()
#Menu principal
menu = 1
while menu != 5:
    menu = int(input("\nBienvenido a UH digital, de acuerdo con las siguientes opciones eliga una.\n1. Registrarse\n2. Editar información\n3. Ver información\n4. Encriptar datos\n5. Salir\nOpción elegida: "))
    if menu == 1:
        registrarse()
    elif menu == 2:
        editar_informacion()
    elif menu == 3:
        ver_informacion()
    elif menu == 4:
        encriptar(Vdatos_usuario,cargar_clave)
    else:
        print("\nHasta la proxima, esperamos que haya sido de tu agrado el entorno estudiantil UH :)\n")

Guardar_datos()