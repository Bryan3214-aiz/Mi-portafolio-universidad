#Programa realizado por Bryan Leiva.

#Calcular el area de las bodegas y determinar cual es la grande.
areas_rectangulo = []
for i in range (5):
    print(f"\nIngrese las dimensiones de la bodega " + (str(i + 1)))
    frente = int(input("Frente: "))
    profundidad = int(input("Profundidad: "))
    altura = int(input("Altura: "))
    
    area = frente * profundidad * altura
    areas_rectangulo.append(area)

if areas_rectangulo[0] > areas_rectangulo[1] and areas_rectangulo[2] and areas_rectangulo[3] and areas_rectangulo[4]:
    print(f"\nLa bodega 1 es la más grande, con un área de almacenamiento de {areas_rectangulo[0]} m²\n") 
    
elif areas_rectangulo[1] > areas_rectangulo[0] and areas_rectangulo[2] and areas_rectangulo[3] and areas_rectangulo[4]:
    print(f"\nLa bodega 2 es la más grande, con un área de almacenamiento de {areas_rectangulo[1]} m²\n") 
    
elif areas_rectangulo[2] > areas_rectangulo[0] and areas_rectangulo[1] and areas_rectangulo[3] and areas_rectangulo[4]:
    print(f"\nLa bodega 3 es la más grande, con un área de almacenamiento de {areas_rectangulo[2]} m²\n") 
    
elif areas_rectangulo[3] > areas_rectangulo[0] and areas_rectangulo[1] and areas_rectangulo[2] and areas_rectangulo[4]:
    print(f"\nLa bodega 4 es la más grande, con un área de almacenamiento de {areas_rectangulo[3]} m²\n") 

elif areas_rectangulo[4] > areas_rectangulo[0] and areas_rectangulo[1] and areas_rectangulo[2] and areas_rectangulo[3]:
    print(f"\nLa bodega 5 es la más grande, con un área de almacenamiento de {areas_rectangulo[4]} m²\n") 
