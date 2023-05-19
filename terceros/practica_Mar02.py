categoria_uno = 0.10
categoria_dos = 0.12
categoria_tres = 0.15
categoria_cuatro = 0.20

salario_empleado = float(input("Ingrese su salario: "))
categoria = int(input("Elija su categoria:\n1. Categoria uno\n2. Categoria dos\n3. Categoria tres\n4. Categoria cuatro "))

if categoria == 1:
    nuevo_salario = salario_empleado * 1.10
    print("El nuevo salario que recibira el empleado es de %d colones" %(nuevo_salario))
elif categoria == 2:
    nuevo_salario = salario_empleado * 1.12
    print("El nuevo salario que recibira el empleado es de %d colones" %(nuevo_salario))
elif categoria == 3:
    nuevo_salario = salario_empleado * 1.15
    print("El nuevo salario que recibira el empleado es de %d colones" %(nuevo_salario))
elif categoria == 4:  
    nuevo_salario = salario_empleado * 1.20
    print("El nuevo salario que recibira el empleado es de %d colones" %(nuevo_salario))