#Programa realizado por Bryan Leiva.

#Sistema de cobro a clientes para un abogado.
print("\nSISTEMA DE PAGO EN LINEA DEL ABOGADO GAMBOA")
print("Ingrese el monto a pagar")
monto = int(input("-->"))
#Si el monto es menor a un millon
if monto < 1000000:
    cobro_timbre_abogados = int(monto * 0.015)
    timbre_colegio_ingenieros = int(monto * 0.005)
    impuesto_asociacion = int(monto * 0.0025)
    impuesto_hacienda = int(monto * 0.05)
    total_pagar = monto + timbre_colegio_ingenieros + cobro_timbre_abogados + impuesto_asociacion + impuesto_hacienda
    print(f"\n---FACTURA POR SERVICIO---\nMonto neto = ₡{monto}\n\n---COBROS E IMPUESTOS---\nTimbre del colegio de abogados = ₡{cobro_timbre_abogados}\nTimbre del colegio de ingenieros en informatica = ₡{timbre_colegio_ingenieros}\nImpuesto de la asociación de animales = ₡{impuesto_asociacion}\nImpuesto del ministerio de hacienda = ₡{impuesto_hacienda}\nTOTAL A PAGAR = ₡{total_pagar}\n")
#Si el monto es mayor a 1 millones pero menos a 10 millones
elif monto >= 1000000 and monto < 10000000:
    descuento = int(monto * 0.05)
    monto_neto = monto - descuento
    cobro_timbre_abogados = int(monto_neto * 0.015)
    timbre_colegio_ingenieros = int(monto_neto * 0.005)
    impuesto_asociacion = int(monto_neto * 0.0025)
    impuesto_hacienda = int(monto_neto * 0.05)
    total_pagar = monto_neto + timbre_colegio_ingenieros + cobro_timbre_abogados + impuesto_asociacion + impuesto_hacienda 
    print(f"\n---FACTURA POR SERVICIO---\nMonto original = ₡{monto}\nDescuento = ₡{descuento}\nMonto neto = ₡{monto_neto}\n\n---COBROS E IMPUESTOS---\nTimbre del colegio de abogados = ₡{cobro_timbre_abogados}\nTimbre del colegio de ingenieros en informatica = ₡{timbre_colegio_ingenieros}\nImpuesto de la asociación de animales = ₡{impuesto_asociacion}\nImpuesto del ministerio de hacienda = ₡{impuesto_hacienda}\nTOTAL A PAGAR = ₡{total_pagar}\n")
#Si el monto es mayor o igual a 10 millones
elif monto >= 10000000:
    descuento = int(monto * 0.1)
    monto_neto = monto - descuento
    cobro_timbre_abogados = int(monto_neto * 0.015)
    timbre_colegio_ingenieros = int(monto_neto * 0.005)
    impuesto_asociacion = int(monto_neto * 0.0025)
    impuesto_hacienda = int(monto_neto * 0.05)
    total_pagar = monto_neto + timbre_colegio_ingenieros + cobro_timbre_abogados + impuesto_asociacion + impuesto_hacienda
    print(f"\n---FACTURA POR SERVICIO---\nMonto original = ₡{monto}\nDescuento = ₡{descuento}\nMonto neto = ₡{monto_neto}\n\n---COBROS E IMPUESTOS---\nTimbre del colegio de abogados = ₡{cobro_timbre_abogados}\nTimbre del colegio de ingenieros en informatica = ₡{timbre_colegio_ingenieros}\nImpuesto de la asociación de animales = ₡{impuesto_asociacion}\nImpuesto del ministerio de hacienda = ₡{impuesto_hacienda}\nTOTAL A PAGAR = ₡{total_pagar}\n")