primerValor = int(input("Ingrese un primer valor: "))
segundoValor = int(input("Ingrese un segundo valor: "))
tercerValor = int(input("Ingrese un tercer valor: "))

if primerValor > segundoValor and segundoValor > tercerValor:
    print(primerValor," - ",segundoValor," - ",tercerValor)
else:
    if primerValor > tercerValor and tercerValor > segundoValor:
        print(primerValor," - ",tercerValor," - ",segundoValor)
    else:
        if segundoValor > primerValor and primerValor > tercerValor:
            print(segundoValor," - ",primerValor," - ",tercerValor)
        else:
            if segundoValor > tercerValor and tercerValor > primerValor:
                print(segundoValor," - ",tercerValor," - ",primerValor)
            else:
                if tercerValor > primerValor and primerValor > segundoValor:
                    print(tercerValor," - ",primerValor," - ",segundoValor)
                else:
                    if tercerValor > segundoValor and segundoValor > primerValor:
                        print(tercerValor," - ",segundoValor," - ",primerValor)