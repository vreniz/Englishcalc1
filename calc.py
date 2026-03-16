print("Welcome to our Basic two numbers - Integer Calculator")

continuar = True

while continuar:

    print("Select the mathematical operation you wish to use")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    operacion = int(input("Option: "))

    numero1 = float(input("Enter first number: "))
    numero2 = float(input("Enter second number: "))

    if operacion == 1:
        resultado = numero1 + numero2
        print("Result:", resultado)

    elif operacion == 2:
        resultado = numero1 - numero2
        print("Result:", resultado)

    elif operacion == 3:
        resultado = numero1 * numero2
        print("Result:", resultado)

    elif operacion == 4:
        while numero2 == 0:
            numero2 = float(input("Enter a valid second number different from 0: "))
        resultado = numero1 / numero2
        print("Result:", resultado)

    respuesta = input("Do you want to use the calculator again? yes/no: ")

    if respuesta == "no":
        continuar = False
        print("Thanks for using our calculator!!!")