#Programa para el taller mecanico La Mandarina.

#Contadores para las distintas funciones que se realizaran en el programa.
capacidad_taller = 20
Vreparacion_frenos = 0
Vreparacion_suspension = 0
Vcambio_aceite = 0
Vreparacion_electrica = 0
Vplaca_vehiculos_ingresados = 0

def ingresar():
    global Vreparacion_frenos,Vreparacion_suspension,Vcambio_aceite,Vreparacion_electrica
    razones = int(input("Ingrese la razon por las cual trae su vehiculo al taller:\n1. Reparación de frenos\n2. Reparación de suspención\n3. Cambio de aceite\n4. Reparación eléctrica\nOpción elegida: "))
    placa_vehiculos = int(input("\nIngrese los digitos de su placa: "))
    if razones == 1:
        if Vreparacion_frenos < capacidad_taller:
            Vreparacion_frenos += 1
            print("El vehiculo se regristro con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 2:
        if Vreparacion_suspension < capacidad_taller:
            Vreparacion_suspension += 1
            print("El vehiculo se regristro con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 3:
        if Vcambio_aceite < capacidad_taller:
            Vcambio_aceite += 1
            print("El vehiculo se regristro con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 4:
        if Vreparacion_electrica < capacidad_taller:
            Vreparacion_electrica += 1
            print("El vehiculo se regristro con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
            
def Retirar():
    global Vreparacion_frenos,Vreparacion_suspension,Vcambio_aceite,Vreparacion_electrica
    placa_vehiculos = int(input("\nIngrese los digitos de su placa: "))
    razones = int(input("Ingrese la razon por las cual trae su vehiculo al taller:\n1. Reparación de frenos\n2. Reparación de suspención\n3. Cambio de aceite\n4. Reparación eléctrica\nOpción elegida: "))
    if razones == 1:
        if Vreparacion_frenos > 0:
            Vreparacion_frenos -= 1
            print("El vehiculo se ha retirado del sistema con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 2:
        if Vreparacion_suspension > 0:
            Vreparacion_suspension -= 1
            print("El vehiculo se ha retirado del sistema con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 3:
        if Vcambio_aceite > 0:
            Vcambio_aceite -= 1
            print("El vehiculo se ha retirado del sistema con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")
    if razones == 4:
        if Vreparacion_electrica > 0:
            Vreparacion_electrica -= 1
            print("El vehiculo se ha retirado del sistema con exito.")
        else: 
            print("Lo sentimos, el valor que ingreso es incorrecto.")

def Consultar():
    porcentaje_ocupacion_frenos = (Vreparacion_frenos * 100) // 20
    porcentaje_ocupacion_suspension = (Vreparacion_suspension * 100) // 20
    porcentaje_ocupacion_aceite = (Vcambio_aceite * 100) // 20
    porcentaje_ocupacion_electrica = (Vreparacion_electrica * 100) // 20
    porcentaje_total_ocupacion = porcentaje_ocupacion_aceite + porcentaje_ocupacion_electrica + porcentaje_ocupacion_frenos + porcentaje_ocupacion_suspension
    
    print("El porcentaje de ocupacion en el area de reparacion de frenos es: {}%".format(porcentaje_ocupacion_frenos))
    print("El porcentaje de ocupacion en el area de reparacion suspension es: {}%".format(porcentaje_ocupacion_suspension))
    print("El porcentaje de ocupacion en el area de cambio de aceite es: {}%".format(porcentaje_ocupacion_aceite))
    print("El porcentaje de ocupacion en el area de reparacion electrica es: {}%".format(porcentaje_ocupacion_electrica))
    print("El porcentaje de ocupacion en todo el taller es: {}%".format(porcentaje_total_ocupacion))

#Menu principal
Vmenu = 1
while Vmenu != 4:
    Vmenu = int(input("Bienvenido al taller mecanico La Mandarina, indique la funcion que desea realizar:\n1. Ingresar\n2. Retirar\n3. Consultar\n4. Salir\nOpción elegida: "))
    if Vmenu == 1:
        ingresar()
    elif Vmenu == 2:
        Retirar()
    elif Vmenu == 3:
        Consultar()
    else: 
        print("Gracias por visitarnos:)")