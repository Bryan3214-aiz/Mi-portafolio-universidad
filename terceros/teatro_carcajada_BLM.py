#Teatro la carcajada - Programado por Bryan Leiva Mejia
import os

#Se define la clase
class clientes_teatro:
    def __init__(self,nombre,correo,telefono,zona): #Atributos que se solicitaran a cada nuevo cliente que se registre.
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.zona = zona

#Funciones para leer los archivos planos que se hayan creado.
def leer_datos_popular():
    datos_popular = []
    if os.path.exists("zona_popular.txt"):
        archivo = open("zona_popular.txt", "r")
        contenido = archivo.read()
        clientes = contenido.split("\n")
        clientes.pop()
        for i in clientes:
            usuarios = i.split(";")
            nuevo_usuario = clientes_teatro(usuarios[0],usuarios[1],usuarios[2],usuarios[3])
            datos_popular.append(nuevo_usuario)
        archivo.close()
    return datos_popular

def leer_datos_preferencial():
    datos_preferencial = []
    if os.path.exists("zona_preferencial.txt"):
        archivo = open("zona_preferencial.txt", "r")
        contenido = archivo.read()
        clientes = contenido.split("\n")
        clientes.pop()
        for i in clientes:
            usuarios = i.split(";")
            nuevo_usuario = clientes_teatro(usuarios[0],usuarios[1],usuarios[2],usuarios[3])
            datos_preferencial.append(nuevo_usuario)
        archivo.close()
    return datos_preferencial

def leer_datos_VIP():
    datos_VIP = []
    if os.path.exists("zona_VIP.txt"):
        archivo = open("zona_VIP.txt", "r")
        contenido = archivo.read()
        clientes = contenido.split("\n")
        clientes.pop()
        for i in clientes:
            datos = i.split(";")
            nuevo_usuario = clientes_teatro(datos[0],datos[1],datos[2],datos[3])
            datos_VIP.append(nuevo_usuario)
        archivo.close()
    return datos_VIP

#Funciones para crear los archivos planos.
def guardar_datos_popular(zona_popular):
    archivo = open("zona_popular.txt", "w")
    for i in zona_popular:
        archivo.write(i.nombre + ";" + i.correo + ";" + i.telefono + ";" + i.zona + "\n")
    archivo.close()

def guardar_datos_preferencial(zona_preferencial):
    archivo = open("zona_preferencial.txt", "w")
    for i in zona_preferencial:
        archivo.write(i.nombre + ";" + i.correo + ";" + i.telefono + ";" + i.zona + "\n")
    archivo.close()

def guardar_datos_VIP(zona_VIP):
    archivo = open("zona_VIP.txt", "w")
    for i in zona_VIP:
        archivo.write(i.nombre + ";" + i.correo + ";" + i.telefono + ";" + i.zona + "\n")
    archivo.close()

def ingresar(zona_popular,zona_preferencial,zona_VIP):
    try:
        zona_elegida = input("\nEscriba la zona en la que desea ubicarse:\n1. Zona popular\n2. Zona preferencial\n3. Zona VIP\nOpcion elegida: ")
        opcion = zona_elegida.capitalize()
        if opcion == "Zona popular":
            if len(zona_popular) < 15:
                control = 0
                nombre = input("\nIngrese su nombre: ")
                correo = input("Ingrese su correo electronico: ")
                telefono = input("Ingrese su numero de telefono: ")
                zona = opcion
                for i in zona_popular:
                    if i.telefono == telefono:
                        print("\nEl usuario ya se encuentra registrado.")
                        control = 1
                if control == 0:
                    nuevo_cliente_teatro = clientes_teatro(nombre,correo,telefono,zona)
                    zona_popular.append(nuevo_cliente_teatro)
                    print("\nUsuario ingresado correctamente")
            else:
                print("\nLa zona seleccionada ha alcanzado su limite de capacidad")
            guardar_datos_popular(zona_popular)

        elif opcion == "Zona preferencial":
            if len(zona_popular) < 15:
                control = 0
                nombre = input("\nIngrese su nombre: ")
                correo = input("Ingrese su correo electronico: ")
                telefono = input("Ingrese su numero de telefono: ")
                zona = opcion
                for i in zona_popular:
                    if i.telefono == telefono:
                        print("\nEl usuario ya se encuentra registrado.")
                        control = 1
                if control == 0:
                    nuevo_cliente_teatro = clientes_teatro(nombre,correo,telefono,zona)
                    zona_preferencial.append(nuevo_cliente_teatro)
                    print("\nUsuario ingresado correctamente")
            else:
                print("\nLa zona seleccionada ha alcanzado su limte de capacidad")
            guardar_datos_preferencial(zona_preferencial)
        elif opcion == "Zona vip":
            if len(zona_VIP) < 15:
                control = 0
                nombre = input("\nIngrese su nombre: ")
                correo = input("Ingrese su correo electronico: ")
                telefono = input("Ingrese su numero de telefono: ")
                zona = opcion
                for i in zona_popular:
                    if i.telefono == telefono:
                        print("\nEl usuario ya se encuentra registrado.")
                        control = 1
                if control == 0:
                    nuevo_cliente_teatro = clientes_teatro(nombre,correo,telefono,zona)
                    zona_VIP.append(nuevo_cliente_teatro)
                    print("\nUsuario ingresado correctamente")
            else:
                print("\nLa zona seleccionada ha alcanzado su limte de capacidad")
            guardar_datos_VIP(zona_VIP)
    finally:
        print("\nLo sentimos la zona que ingreso no existe")

def retirar(zona_popular,zona_preferencial,zona_VIP):
    try:
        zona_elegida = input("Escriba la zona en la que estaba ubicado: ")
        opcion = zona_elegida.capitalize()
        if opcion == "Zona popular":
            if (len(zona_popular)) > 0:
                cliente = -1 
                telefono = input("Ingrese el numero de telefono que registro: ")
                for i in range(len(zona_popular)):
                    if zona_popular[i].telefono == telefono:
                        cliente = i
                else:
                    print("\nNo existe ningún usuario registrado con ese numero.")
                if cliente >= 0:
                    zona_popular.pop(cliente)
                    print("\nUsuario retirado con exito")
                guardar_datos_popular(zona_popular)
            else:
                print("No han ingresado usuario a esta zona")
        elif opcion == "Zona preferencial":
            if (len(zona_preferencial)) > 0:
                cliente = -1 
                telefono = input("Ingrese el numero de telefono que registro: ")
                for i in range(len(zona_preferencial)):
                    if zona_preferencial[i].telefono == telefono:
                        cliente = i
                else:
                    print("\nNo existe ningún usuario registrado con ese numero.")

                if cliente >= 0:
                    zona_preferencial.pop(cliente)
                    print("\nUsuario retirado con exito.")
                guardar_datos_preferencial(zona_preferencial)
            else:
                print("\nNo han ingresado usuario a esta zona.")
        elif opcion == "Zona vip":
            if (len(zona_VIP)) > 0:
                cliente = -1 
                telefono = input("Ingrese el numero de telefono que registro: ")
                for i in range(len(zona_VIP)):
                    if zona_VIP[i].telefono == telefono:
                        cliente = i
                else:
                    print("\nNo existe ningún usuario registrado con ese numero.")

                if cliente >= 0:
                    zona_VIP.pop(cliente)
                    print("\nUsuario retirado con exito")
                guardar_datos_VIP(zona_VIP)
            else:
                print("\nNo han ingresado usuario a esta zona.")
    except:
        print("\nLo sentimos la zona ingresada no existe.")

def consultar(zona_popular,zona_preferencial,zona_VIP):
    #Verifica la capacidad restante en cada zona
    print("\n---ASIENTOS DISPONIBLES POR ZONA---")
    print(f"Zona popular = {str(15 - len(zona_popular))} espacios libres\nZona preferencial = {str(15 - len(zona_preferencial))} espacios libres\nZona VIP = {str(10 - len(zona_VIP))} espacios libres")
    mostrar = input("\n¿Qué desea hacer?\n1. Ver porcentaje de asientos ocupados por zona.\n2. Ver información general de todos los usuarios.\nOpción elegida: ")
    if mostrar == 1:
        porcentaje_popular = (len(zona_popular) * 100) // 15
        porcentaje_preferencial = (len(zona_preferencial) * 100) // 15
        porcentaje_VIP = (len(zona_VIP) * 100) // 10        
        print(f"\nPorcentaje ocupado zona popular: {porcentaje_popular}%")
        print(f"Porcentaje ocupado zona preferencial: {porcentaje_preferencial}%")
        print(f"Porcentaje ocupado zona VIP: {porcentaje_VIP}%")
        print(f"Porcentaje general del teatro: {porcentaje_popular+porcentaje_preferencial+porcentaje_VIP}%")
    elif mostrar == 2: #Si existe al menos un dato ingresado en cada una de las zonas se muestra en consola ese valor.
        if len(zona_popular) > 0:
            print("\n---ZONA POPULAR---")
            for i in zona_popular:
                print(f"Nombre: {i.nombre} | Correo: {i.correo} | Telefono: {i.telefono} | Zona: {i.zona}")
        else:
            print("\nNo hay usuarios registrados en la zona popular.")
        if len(zona_preferencial) > 0:
            print("\n---ZONA PREFERENCIAL---")
            for i in zona_preferencial:
                print(f"Nombre: {i.nombre} | Correo: {i.correo} | Telefono: {i.telefono} | Zona: {i.zona}")
        else:
            print("\nNo hay usuarios registrados en la zona preferencial.")
        if len(zona_VIP) > 0:
            print("\n---ZONA VIP---")
            for i in zona_VIP:
                print(f"Nombre: {i.nombre} | Correo: {i.correo} | Telefono: {i.telefono} | Zona: {i.zona}")
        else:
            print("\nNo hay usuarios registrados en la zona VIP.")
#Lista por cada zona del teatro.
zona_popular = []
zona_preferencial = []
zona_VIP = []
opcion = 1
#Menu principal
zona_popular = leer_datos_popular()
zona_preferencial = leer_datos_preferencial()
zona_VIP = leer_datos_VIP()
while opcion != 4:
    try:
        opcion = int(input("\nBienvenido al teatro la carcajada, elija una opción del menu:\n1. Ingresar\n2. Retirar\n3. Consultar\n4. Salir\nOpción elegida: "))
        if opcion == 1:
            ingresar(zona_popular,zona_preferencial,zona_VIP)
        elif opcion == 2:
            retirar(zona_popular,zona_preferencial,zona_VIP)
        elif opcion == 3:
            consultar(zona_popular,zona_preferencial,zona_VIP)
        elif opcion == 4:
            print("\nGracias por visitar el Teatro La carcajada :)\n")
    except:
        print("\nERROR, el valor ingresado es incorrecto.")