#COMPRA DE MATERIALES CON DESCUENTO AL CONTADO Y AL CREDITO.
print("\nBienvenidos a la ferreteria Patas de gato S.A\n")
eleccion_material = int(input("Elija la cantidad de tipos de materiales que desea adquirir:\n1. I material\n2. II materiales\n3. III materiales\n4. Salir\nOpción elegida: "))

if eleccion_material == 1:
    materiales = int(input("\nElija la cantidad de tipos de materiales que desea adquirir:\n1. Hielo seco.\n2. Viguetas.\n3. Armazones.\nOpción elegida: "))
    if materiales == 1:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1: #Si el usuario elije pagar de contado se le aplica un descuento extra del 7%
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades hielo seco que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad del hielo seco: "))
            precio_neto_total = cantidad_hielo * precio_unitario
            descuento_hielo = int(precio_neto_total * 0.20)
            total = precio_neto_total - descuento_hielo 
            descuento_contado = int(total * 0.07)
            total_pagar = total - descuento_contado
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHojas de hielo = {total_pagar} colones\n")
        elif modo_pago == 2:#Si el usuario decide pagar a credito no se le aplica descuento.
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad del hielo seco: "))
            precio_neto_total = cantidad_hielo * precio_unitario
            descuento_hielo = int(precio_neto_total * 0.20)
            total_pagar = precio_neto_total - descuento_hielo 
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHojas de hielo = {total_pagar} colones\n")
    elif materiales == 2:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1: #Si el usuario elije pagar de contado se le aplica un descuento extra del 7%
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad de las viguetas: "))
            precio_neto_total = cantidad_viguetas * precio_unitario
            descuento_viguetas = int(precio_neto_total * 0.15)
            total = precio_neto_total - descuento_viguetas
            descuento_contado = int(total * 0.07)
            total_pagar = total - descuento_contado
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nViguetas = {total_pagar} colones\n")
        elif modo_pago == 2:#Si el usuario decide pagar a credito no se le aplica descuento.
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades viguetas que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad de las viguetas: "))
            precio_neto_total = cantidad_viguetas * precio_unitario
            descuento_viguetas = int(precio_neto_total * 0.15)
            total_pagar = precio_neto_total - descuento_viguetas
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nViguetas = {total_pagar} colones\n")
    elif materiales == 3:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1: #Si el usuario elije pagar de contado se le aplica un descuento extra del 7%
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad de los armazones: "))
            precio_neto_total = cantidad_armazones * precio_unitario
            descuento_contado = int(precio_neto_total * 0.07)
            total_pagar = precio_neto_total - descuento_contado
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nArmazones = {total_pagar} colones\n")
        elif modo_pago == 2:#Si el usuario decide pagar a credito no se le aplica descuento.
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            precio_unitario = int(input("Ingrese el precio por unidad de los armazones: "))
            total_pagar = cantidad_armazones * precio_unitario
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nArmazones = {total_pagar} colones\n")
elif eleccion_material == 2:
    materiales = int(input("\nElija los tipos de materiales que desea adquirir:\n1. Hielo seco y Viguetas.\n2. Hielo seco y Armazones.\n3. Viguetas y Armazones.\nOpción elegida: "))
    if materiales == 1:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1:
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
            unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
            unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
            #Costo neto de los productos de forma individual.
            precio_neto_hielo = cantidad_hielo * unidad_hielo
            precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
            #Descuentos a productos de forma individual.
            descuento_hielo = int(precio_neto_hielo * 0.20)
            descuento_viguetas = int(precio_neto_viguetas * 0.15)
            #Cuentas totales.
            total_hielo = precio_neto_hielo - descuento_hielo 
            total_viguetas = precio_neto_viguetas - descuento_viguetas
            #Descuento por contado.
            descuento_contado_hielo = int(total_hielo * 0.07)
            descuento_contado_viguetas = int(total_viguetas * 0.07)
            #Cuentas totales por pagar.
            total_pagar_hielo = total_hielo - descuento_contado_hielo
            total_pagar_viguetas = total_viguetas - descuento_contado_viguetas
            cuenta_cancelar = total_pagar_hielo + total_pagar_viguetas
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_pagar_hielo} colones\nViguetas = {total_pagar_viguetas} colones\nFactura total = {cuenta_cancelar} colones\n")
        elif modo_pago == 2:
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
            unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
            unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
            #Costo neto de los productos de forma individual.
            precio_neto_hielo = cantidad_hielo * unidad_hielo
            precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
            #Descuentos a productos de forma individual.
            descuento_hielo = int(precio_neto_hielo * 0.20)
            descuento_viguetas = int(precio_neto_viguetas * 0.15)
            #Cuentas totales.
            total_hielo = precio_neto_hielo - descuento_hielo 
            total_viguetas = precio_neto_viguetas - descuento_viguetas
            cuenta_cancelar = total_hielo + total_viguetas
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_hielo} colones\nViguetas = {total_viguetas} colones\nFactura total = {cuenta_cancelar} colones\n")
    elif materiales == 2:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1:
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
            unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
            #Costo neto de los productos de forma individual.
            precio_neto_hielo = cantidad_hielo * unidad_hielo
            precio_neto_armazones = cantidad_armazones * unidad_armazones
            #Descuentos a productos de forma individual.
            descuento_hielo = int(precio_neto_hielo * 0.20)
            #Cuentas totales.
            total_hielo = precio_neto_hielo - descuento_hielo 
            total_armazones = precio_neto_armazones
            #Descuento por contado.
            descuento_contado_hielo = int(total_hielo * 0.07)
            descuento_contado_armazones = int(total_armazones * 0.07)
            #Cuentas totales por pagar.
            total_pagar_hielo = total_hielo - descuento_contado_hielo
            total_pagar_armazones = total_armazones - descuento_contado_armazones
            cuenta_cancelar = total_pagar_hielo + total_pagar_armazones
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_pagar_hielo} colones\nArmazones = {total_pagar_armazones} colones\nFactura total = {cuenta_cancelar} colones\n")
        elif modo_pago == 2:
            cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
            unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
            #Costo neto de los productos de forma individual.
            precio_neto_hielo = cantidad_hielo * unidad_hielo
            precio_neto_armazones = cantidad_armazones * unidad_armazones
            #Descuentos a productos de forma individual.
            descuento_hielo = int(precio_neto_hielo * 0.20)
            #Cuentas totales.
            total_hielo = precio_neto_hielo - descuento_hielo 
            total_armazones = precio_neto_armazones
            cuenta_cancelar = total_hielo + total_armazones
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_hielo} colones\nArmazones = {total_armazones}colones\nFactura total = {cuenta_cancelar} colones\n")
    elif materiales == 3:
        modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
        if modo_pago == 1:
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
            unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
            #Costo neto de los productos de forma individual.
            precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
            precio_neto_armazones = cantidad_armazones * unidad_armazones
            #Descuentos a productos de forma individual.
            descuento_viguetas = int(precio_neto_viguetas * 0.15)
            #Cuentas totales.
            total_viguetas = precio_neto_viguetas - descuento_viguetas
            total_armazones = precio_neto_armazones
            #Descuento por contado. 
            descuento_contado_viguetas = int(total_viguetas * 0.07)
            descuento_contado_armazones = int(total_armazones * 0.07)
            #Cuentas totales por pagar.
            total_pagar_viguetas = total_viguetas - descuento_contado_viguetas
            total_pagar_armazones = total_armazones - descuento_contado_armazones
            cuenta_cancelar = total_pagar_armazones + total_pagar_viguetas
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nViguetas = {total_pagar_viguetas} colones\nArmazones = {total_pagar_armazones} colones\nFactura total = {cuenta_cancelar} colones\n")
        elif modo_pago == 2:
            cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
            unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
            cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
            unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
            #Costo neto de los productos de forma individual.
            precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
            precio_neto_armazones = cantidad_armazones * unidad_armazones
            #Descuentos a productos de forma individual.
            descuento_viguetas = int(precio_neto_viguetas * 0.15)
            #Cuentas totales.
            total_viguetas = precio_neto_viguetas - descuento_viguetas
            total_armazones = precio_neto_armazones
            cuenta_cancelar = total_viguetas + total_armazones
            print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nViguetas = {total_viguetas} colones\nArmazones = {total_armazones} colones\nFactura total = {cuenta_cancelar} colones\n")
elif eleccion_material == 3:
    modo_pago = int(input("\nElija el modo pago que utilizara:\n1. Contado.\n2. Credito.\nOpción elegida: "))
    if modo_pago == 1:
        cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
        unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
        cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
        unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
        cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
        unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
        #Costo neto de los productos de forma individual.
        precio_neto_hielo = cantidad_hielo * unidad_hielo
        precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
        precio_neto_armazones = cantidad_armazones * unidad_armazones
        #Descuentos a productos de forma individual.
        descuento_hielo = int(precio_neto_hielo * 0.20)
        descuento_viguetas = int(precio_neto_viguetas * 0.15)
        #Cuentas totales.
        total_hielo = precio_neto_hielo - descuento_hielo
        total_viguetas = precio_neto_viguetas - descuento_viguetas
        total_armazones = precio_neto_armazones
        #Descuento por contado. 
        descuento_contado_hielo = int(total_hielo * 0.07)
        descuento_contado_viguetas = int(total_viguetas * 0.07)
        descuento_contado_armazones = int(total_armazones * 0.07)
        #Cuentas totales por pagar.
        total_pagar_hielo = total_hielo - descuento_contado_hielo
        total_pagar_viguetas = total_viguetas - descuento_contado_viguetas
        total_pagar_armazones = total_armazones - descuento_contado_armazones
        cuenta_cancelar = total_pagar_hielo + total_pagar_armazones + total_pagar_viguetas
        print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_pagar_hielo} colones\nViguetas = {total_pagar_viguetas} colones\nArmazones = {total_pagar_armazones} colones\nFactura total = {cuenta_cancelar} colones\n")
    elif modo_pago == 2:
        cantidad_hielo = int(input("\nIngrese la cantidad de unidades de hielo seco que necesita: "))
        unidad_hielo = int(input("Ingrese el precio por unidad del hielo seco: "))
        cantidad_viguetas = int(input("\nIngrese la cantidad de unidades de viguetas que necesita: "))
        unidad_viguetas = int(input("Ingrese el precio por unidad de las viguetas: "))
        cantidad_armazones = int(input("\nIngrese la cantidad de unidades de armazones que necesita: "))
        unidad_armazones = int(input("Ingrese el precio por unidad de los armazones: "))
        #Costo neto de los productos de forma individual.
        precio_neto_hielo = cantidad_hielo * unidad_hielo
        precio_neto_viguetas = cantidad_viguetas * unidad_viguetas
        precio_neto_armazones = cantidad_armazones * unidad_armazones
        #Descuentos a productos de forma individual.
        descuento_hielo = int(precio_neto_hielo * 0.20)
        descuento_viguetas = int(precio_neto_viguetas * 0.15)
        #Cuentas totales.
        total_hielo = precio_neto_hielo - descuento_hielo
        total_viguetas = precio_neto_viguetas - descuento_viguetas
        total_armazones = precio_neto_armazones
        cuenta_cancelar = total_viguetas + total_armazones + total_hielo
        print(f"\n---CUENTAS POR CANCELAR---\nProductos:\nHielo seco = {total_hielo} colones\nViguetas = {total_viguetas} colones\nArmazones = {total_armazones} colones\nFactura total = {cuenta_cancelar} colones\n")
elif eleccion_material == 4: 
    print("\nGracias por visitar Ferreteria Patas de gato :)\n")

#LOGRADO