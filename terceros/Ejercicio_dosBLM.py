#Programa realizado por Bryan Leiva.
import os

try:
    if os.path.exists("datos.txt"):
        archivo = open("datos.txt", "r")
        contenido = archivo.read()
        valores = contenido.split("\n")
        archivo.close()
        valores.pop()
        print("Documento encontrado.")
except IOError as escrituralectura:
    print("Se ha generado un error de escritura:", escrituralectura)
    resultado = 0
except Exception as desconocido:
    print("Error desconocido:", desconocido)
else:
    print("El proceso fue correcto...")
finally:
    print("Fin del programa...")
