"""Esta aplicacion sera una multiplicadora basica que tendra suma resta divicion y multiplicacion"

definimos las funciones que vamos a utilizar en la calculadora"""

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def divicion(a,b):
    return a/b

"definimos el menu de la calculadora"

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Divicion")
    print("5. Salir")

"definimos la funcion principal de la calculadora"

def calculadora():
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")

        if opcion == "5":
            print("Gracias por usar la calculadora")
            break

        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if opcion == "1":
            print("El resultado de la suma es: ", suma(num1,num2))
        elif opcion == "2":
            print("El resultado de la resta es: ", resta(num1,num2))
        elif opcion == "3":
            print("El resultado de la multiplicacion es: ", multiplicacion(num1,num2))
        elif opcion == "4":
            print("El resultado de la divicion es: ", divicion(num1,num2))
        else:
            print("Opcion invalida")

"llamamos a la funcion principal de la calculadora"

calculadora()