#Programa para autobuses.
costo_total_viaje = 0
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que asistiran al viaje: "))
costo_autobus = int(input("Ingrese el costo del autobus: "))
capacidad_autobus = int(input("Ingrese la capacidad de estudiantes: "))

if cantidad_estudiantes % capacidad_autobus == 0:
    cantidad_autobus = cantidad_estudiantes / capacidad_autobus
else:
    cantidad_autobus = cantidad_estudiantes // capacidad_autobus + 1
total_bruto = cantidad_autobus * costo_autobus
pago_IVA = int(total_bruto * 0.13)
total_neto = total_bruto + pago_IVA
costo_estudiante = int(total_neto / cantidad_estudiantes)

print ("Cantidad de buses:",cantidad_autobus)
print ("Costo de viaje por estudiante:",costo_estudiante)
