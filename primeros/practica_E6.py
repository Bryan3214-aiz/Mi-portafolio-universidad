#Programa para salario de 10 empleados.

salario_empleados = 0
salario_total_pagar = 0

for i in range (0,10):
    salario_empleados = int(input("Ingrese el salario " + str(i + 1) + ": "))
    salario_total_pagar += salario_empleados
    deducciones_salario = salario_total_pagar * 0.9
print("El salario total a pagar aplicando una deducción del 9% por cargas sociales es de",deducciones_salario,"colones.")