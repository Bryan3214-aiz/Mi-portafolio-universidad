#Programa de sueldos a invertir.

salario_empleados = 0

for i in range (0,20):
    salario = int(input("Ingrese su salario " + str(i + 1) + ": "))
    if salario < 1000:
        salario_faltante = 1000 - salario 
        salario_empleados = salario_empleados + salario_faltante 
print("El monto que debera invertir la empresa:",salario_empleados)