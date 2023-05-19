#Programa de estudiantes que viven en cada provincia.

Estudiantes_SanJose = 0
Estudiantes_Cartago = 0
Estudiantes_Alajuela = 0
Estudiantes_Guanacaste = 0
Estudiantes_Heredia = 0
Estudiantes_Puntarenas = 0
Estudiantes_Limon = 0

#El usuario puede ingresar la cantidad de estudiantes que hay en el grupo y luego seguir con todo el proceso del programa.
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes del grupo: "))
for i in range (cantidad_estudiantes):
    provincia = (input("Ingrese su provincia de residencia, Estudiante " + str(i + 1) + ": "))
    if provincia == "San José":
        Estudiantes_SanJose = Estudiantes_SanJose + 1
    elif provincia == "Alajuela":
        Estudiantes_Alajuela = Estudiantes_Alajuela + 1
    elif provincia == "Cartago":
        Estudiantes_Cartago = Estudiantes_Cartago + 1
    elif provincia == "Heredia":
        Estudiantes_Heredia = Estudiantes_Heredia + 1
    elif provincia == "Guanacaste":
        Estudiantes_Guanacaste = Estudiantes_Guanacaste + 1
    elif provincia == "Puntarenas":
        Estudiantes_Puntarenas = Estudiantes_Puntarenas + 1
    elif provincia == "Limón":
        Estudiantes_Limon = Estudiantes_Limon + 1

porcentaje_SanJose = (Estudiantes_SanJose * 100) // cantidad_estudiantes
porcentaje_Alajuela = (Estudiantes_Alajuela * 100) // cantidad_estudiantes
porcentaje_Cartago = (Estudiantes_Cartago * 100) // cantidad_estudiantes
porcentaje_Heredia = (Estudiantes_Heredia * 100) // cantidad_estudiantes
porcentaje_Guanacaste = (Estudiantes_Guanacaste * 100) // cantidad_estudiantes
porcentaje_Puntarenas = (Estudiantes_Puntarenas * 100) // cantidad_estudiantes
porcentaje_Limon = (Estudiantes_Limon * 100) // cantidad_estudiantes

print("Los porcentaje de estudiantes de San José es: {}%".format(porcentaje_SanJose))
print("El porcentaje de estudiantes de Alajuela es: {}%".format(porcentaje_Alajuela))
print("El porcentaje de estudiantes de Cartago es: {}%".format(porcentaje_Cartago))
print("El porcentaje de estudiantes de Heredia es: {}%".format(porcentaje_Heredia))
print("El porcentaje de estudiantes de Guanacaste es: {}%".format(porcentaje_Guanacaste))
print("El porcentaje de estudiantes de Puntarenas es: {}%".format(porcentaje_Guanacaste))
print("El porcentaje de estudiantes de Limón es:{} %".format(porcentaje_Limon))