#Programa para restriccion de placas.

cantidad_placas_conductores = 0
cantidad_placas_lunes = 0

while cantidad_placas_conductores < 21:
    placa = int(input("Ingrese los digitos de su placa: "))
    ultimo_numero = placa % 10
    if ultimo_numero >= 1 or ultimo_numero <= 4:
        cantidad_placas_conductores = cantidad_placas_conductores + 1
    if ultimo_numero == 1 or ultimo_numero == 2:
        cantidad_placas_lunes = cantidad_placas_lunes + 1
print ("De las placas registradas, las que tienen restriccion el dia lunes son: ",cantidad_placas_lunes)