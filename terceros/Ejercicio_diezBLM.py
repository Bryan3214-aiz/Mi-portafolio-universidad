#Programa realizado por Bryan Leiva para el retorno a la presencialidad en la UH.

#Duracion de una semana de clases y de un cuatrimestre completo en dias.
semana = 7
cuatrimestre = 105 

print("\nBIENVENIDO A LA UNIVERSIDAD HISPANOAMERICANA\n")
distancia_kilometros = int(input("Ingrese la distancia en kilotretros de su casa a la universidad: "))
costo_kilometro = int(input("Ingrese el costo por kilometro recorrido de su casa a la universidad: "))
cantidad_materias = int(input("Ingrese la cantidad de materias matriculadas: "))

if cantidad_materias == 1:
    monto = (distancia_kilometros * costo_kilometro) * 2
    monto_semana = monto * cantidad_materias
    monto_cuatrimestre = monto_semana * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es: ₡{costo_kilometro}")
    print(f"Materias matriculadas: {cantidad_materias}")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 2:
    monto = (distancia_kilometros * costo_kilometro) * 2
    monto_semana = monto * 2
    monto_cuatrimestre = monto_semana * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es: ₡{costo_kilometro}")
    print(f"Materias matriculadas: {cantidad_materias}")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 3:
    monto = ((distancia_kilometros * costo_kilometro) * cantidad_materias) * 2
    monto_semana = monto * 3
    monto_cuatrimestre = monto_semana * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es ₡{costo_kilometro}")
    print(f"Tiene una cantidad de {cantidad_materias} matriculada")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 4:
    monto = ((distancia_kilometros * costo_kilometro) * cantidad_materias) * 2
    monto_semana = monto * 4
    monto_cuatrimestre = monto_semana * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es ₡{costo_kilometro}")
    print(f"Tiene una cantidad de {cantidad_materias} matriculada")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 5:
    monto = ((distancia_kilometros * costo_kilometro) * cantidad_materias) * 2
    monto_semana = monto * semana
    monto_cuatrimestre = monto * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es ₡{costo_kilometro}")
    print(f"Tiene una cantidad de {cantidad_materias} matriculada")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 6:
    monto = ((distancia_kilometros * costo_kilometro) * cantidad_materias) * 2
    monto_semana = monto * semana
    monto_cuatrimestre = monto * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es ₡{costo_kilometro}")
    print(f"Tiene una cantidad de {cantidad_materias} matriculada")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")

elif cantidad_materias == 7:
    monto = ((distancia_kilometros * costo_kilometro) * cantidad_materias) * 2
    monto_semana = monto * semana
    monto_cuatrimestre = monto * cuatrimestre
    print(f"\nEl estudiante vive a {distancia_kilometros} kilometros de la universidad")
    print(f"El costo por kilometro de su hogar a la universidad es ₡{costo_kilometro}")
    print(f"Tiene una cantidad de {cantidad_materias} matriculada")
    print(f"\nEl monto total por día, de ida y vuelta de su hogar a la universidad es: ₡{monto}\npor semana: ₡{monto_semana} y por el cuatrimestre completo: ₡{monto_cuatrimestre}\n")