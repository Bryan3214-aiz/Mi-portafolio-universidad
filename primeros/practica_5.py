usuario = ""
clave = ""
while usuario != "Admin" or clave != "123":
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == "Admin" and clave == "123":
        print("Bienvenido")
    else:
        print("Error en algunos de los datos, intenta otra vez")