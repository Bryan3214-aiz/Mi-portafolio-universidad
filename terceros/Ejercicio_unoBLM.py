#Programa realizado por Bryan Leiva.

def guardar_datos(datos_usuario):
    archivo = open("datos_usuario.txt", "w")
    for i in datos_usuario:
        archivo.write(i + "\n")
    archivo.close()
def Ingresar(datos_usuario):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    for i in range(5):
        datos_usuario.append(nombre)
    for x in range(5):
        datos_usuario.append(apellido)
    guardar_datos(datos_usuario)

datos_usuario = []

Ingresar(datos_usuario)