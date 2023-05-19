#Programa edades porcentaje joven/adulto
menores = 0
adultos = 0
adultos_mayores = 0
promedio = 0

for i in range(0,30):
    edad_personas = int(input("Ingrese su edad, persona " + str(i+1) + ": "))
    if edad_personas < 18:
        menores = menores + 1
    else:
        if edad_personas >= 18:
            adultos = adultos + 1
            promedio = promedio + adultos
        else:
            if edad_personas == 65:
                adultos_mayores = adultos_mayores + 1
                promedio = promedio + adultos_mayores

porcentaje_edad_menores = (menores * 100) / 30                
porcentaje_edad_adultos = (adultos * 100) / 30
porcentaje_edad_adultos_mayores = (adultos_mayores* 100) / 30                
promedio = promedio / (adultos + adultos_mayores)

print("El promedio de edad es: ",promedio,"%")      
print("El porcentaje de personas menores es: ",porcentaje_edad_menores,"%")
print("El porcentaje de personas adultas es: ",porcentaje_edad_adultos,"%")
print("El porcentaje de personas adultaa mayores es: ",porcentaje_edad_adultos_mayores,"%")