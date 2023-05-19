
notasEstudiante = []
for i in range (0,5):
    notaEstudiante = int(input("Ingrese la nota que obtuvo en 5 materias: "))
    notasEstudiante.append (notaEstudiante)
if (len(notaEstudiante)) > 70:
    print("El estudiante aprobo en todas sus materias.")
elif (len(notaEstudiante)) < 70 and (len(notaEstudiante)) > 60:
    print("El estudiante no aprobo en todos los cursos, por lo que, debera hacer examanes extraordianario.")
elif (len(notaEstudiante)) < 60:
    print("El estudiante reprobo en mas de 3 cursos, por lo que, debera matricular de nuevo.")