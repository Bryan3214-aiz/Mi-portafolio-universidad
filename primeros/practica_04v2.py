baseRectangulo = input("Ingrese la base del rectangulo")
alturaRectangulo = input("Ingrese la altura del rectangulo")
calcularArea = int(baseRectangulo)*int(alturaRectangulo)
calcularPerimetro = (int(baseRectangulo)+int(alturaRectangulo))*2
print (f'''El area del rectangulo es: {calcularArea} 
El perimetro del rectangulo es: {calcularPerimetro}''')

# f-strings o + sirven para concatenar. Las 3 comillas sirven para hacer una cadena de texto de varias lineas.