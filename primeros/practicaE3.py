notaUno = int(input("Ingrese la nota que obtuvo en su primera materia: "))
notaDos = int(input("Ingrese la notas que obtuvo en su segunda materia: "))
notaTres = int(input("Ingrese la notas que obtuvo en su tercera materia: "))
notaCuatro = int(input("Ingrese la nota que obtuvo en su cuarta materia: "))
notaCinco = int(input("Ingrese la nota que obtuvo en su quinta materia: "))

promedioNotas = (notaUno + notaDos + notaTres + notaCuatro + notaCinco) / 5

if promedioNotas >= 70:
    print ("El estudiante aprobo en todas sus materias con un promedio de: ",promedioNotas)
    print ("Las notas que obtuvo en cada uno de sus cursos fueron las siguintes: ")
    print ("Primer materia: ",notaUno,"Segunda materia: ",notaDos,"Tercer materia: ",notaTres,"Cuarta materia: ",notaCuatro,"Quinta materia: ",notaCinco)
else:
    if promedioNotas >= 60:
        print ("El estudiante debera hacer examenes extraordinarios, ya que, reprobo en algunos cursos.")
        print ("Las notas que obtuvo en cada uno de sus cursos fueron las siguintes: ")
        print ("Primer materia: ",notaUno,"Segunda materia: ",notaDos,"Tercer materia: ",notaTres,"Cuarta materia: ",notaCuatro,"Quinta materia: ",notaCinco)
    else:
        if promedioNotas < 60:
            print ("El estudiante ha reprobado en mas de 3 cursos y debera matricular los cursos de nuevo.")