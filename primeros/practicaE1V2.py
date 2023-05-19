primerValor = int(input("ingrese un primer numero: "))
segundoValor = int(input("ingrese un segundo numero: "))
tercerValor = int(input("ingrese un tercer numero: "))
cuartoValor = int(input("ingrese un cuarto numero: "))

if segundoValor < primerValor > tercerValor and primerValor > cuartoValor:
    print ("El valor mayor es el primer numero: ",primerValor)
else:
    if primerValor < segundoValor > tercerValor and segundoValor > cuartoValor:
        print ("El valor mayor es el segundo numero: ",segundoValor)
    else: 
        if segundoValor < tercerValor > primerValor and tercerValor > cuartoValor:
            print ("El tercer valor es el numero mayor: ",tercerValor)
        else:
            if cuartoValor > tercerValor:
                print("El cuarto valor es el numero mayor: ",cuartoValor)