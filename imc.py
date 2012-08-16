def imc():
    p=int(input("Ingrese su peso: "))
    a=float(input("Ingrese su altura: "))
    v= p/(a*a)
    if v<=16.00:
        print("Delgadez Severa")
    elif v>16.00 and v<=18.49:
        print("Delgadez No muy pronunciada")
    elif v>=18.5 and v<24.99:
        print("Normal")
    elif v>=25.00 and v<30.00:
        print("sobre peso")
    elif v>=30.00:
        print("Obeso")

