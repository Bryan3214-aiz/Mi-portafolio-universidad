#Programado por Bryan Leiva Mejia.

#Calcular precio de autobus.
costo_total_viaje = 0
monto_alquiler = 100000
capacidad_buses = 40

cantidad_estudiantes = int(input("Ingresa la cantidad de estudiantes que viajaran en autobus: "))

if cantidad_estudiantes % capacidad_buses == 0:
    cantidad_buses = cantidad_estudiantes / capacidad_buses
else:
    cantidad_buses = cantidad_estudiantes // capacidad_buses + 1

costo_total_bruto = cantidad_buses * monto_alquiler
pago_iva = int(costo_total_bruto * 0.13)
costo_total_neto = int(costo_total_bruto + pago_iva)
cuota_estudiante = int(costo_total_neto / cantidad_estudiantes)

print(f"\n--- TRANSPORTES GALILEO S.A. ---\n\nCantidad de autobuses = {cantidad_buses}\nCuota por estudiante = ₡{cuota_estudiante}\nFactura total = ₡{costo_total_neto}\n")
print("GRACIAS POR VIAJAR CON NOSOTROS :D\n")