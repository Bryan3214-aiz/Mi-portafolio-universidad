#Programa realizado por Bryan Leiva.

class partidos_politicos:#Crea partidos nuevos en caso de que no existan.
    def __init__(self,candidato,bandera,partido):
        self.candidato = candidato 
        self.bandera = bandera
        self.partido = partido
        self.contador = 1

def votante(partidos_totales):
    for i in range(5):
        eleccion = int(input("\n---SELECCIONE UN PARTIDO---\n1. Union Nacional\n2. Social Democrata\n3. Republicano\n4. Otro\nOpcion elegida: "))
        if eleccion == 1:
            candidato = "Pedro Infante"
            bandera = "Negro y blanco"
            partido = "Union nacional"
            votante_nuevo = partidos_politicos(candidato,bandera,partido,contador)
            partidos_totales.append(votante_nuevo)

        elif eleccion == 2:
            candidato = "Roberto Casas"
            bandera = "Morado y blanco"
            partido = "Social democrata"
            contador += 1
            votante_nuevo = partidos_politicos(candidato,bandera,partido,contador)
            partidos_totales.append(votante_nuevo)
    
        elif eleccion == 3:
            candidato = "Pablo Escobar"
            bandera = "Azul y gris"
            partido = "Republicano"
            contador += 1
            votante_nuevo = partidos_politicos(candidato,bandera,partido,contador)
            partidos_totales.append(votante_nuevo)

        elif eleccion == 4:
            candidato = input("\nIngrese el nombre del candidatos: ")
            bandera = input("Ingrese los colores de la bandera: ")
            partido = input("Ingrese el nombre del partido politico: ")
            votante_nuevo = partidos_politicos(candidato,bandera,partido)
            partidos_totales.append(votante_nuevo)

def contador_votos(partidos_totales):
    for i in partidos_totales:
        if i.partido == 1:
            contador_votos_union += 1
    for i in partidos_totales:
        if i.partido == 2:
            contador_votos_union += 1
    for i in partidos_totales:
        if i.partido == 3:
            contador_votos_union += 1
    for i in partidos_totales:
        if i.partido == 4:
            contador_votos_union += 1
    
 
    
#Lista
partidos_totales = []

#Menu principal
while True:
    eleccion = int(input("\n¿Qué desea hacer?\n1. Votar.\n2. Contador de votos\n3. Salir del sistema de votación.\nOpcion elegida: "))
    if eleccion == 1:
        votante(partidos_totales)
    elif eleccion == 2:
        contador_votos(partidos_totales)
    elif eleccion == 3:
        break