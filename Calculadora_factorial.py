# Calculadora factorial

import math

def mostrar_menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Factorial")
    print("2. Logaritmo")
    print("0. Salir")

def calcular_factorial(numero):
    return math.factorial(numero)

def calcular_logaritmo(base, numero):
    return math.log(numero, base)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación deseada (0 para salir): ")
        
        if opcion == '0':
            print("Saliendo...")
            break
        
        if opcion not in ['1', '2']:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue
        
        if opcion == '1':
            numero = int(input("Ingrese el número para calcular el factorial: "))
            resultado = calcular_factorial(numero)
            print("El factorial de", numero, "es:", resultado)
        elif opcion == '2':
            base = float(input("Ingrese la base del logaritmo: "))
            numero = float(input("Ingrese el número para calcular el logaritmo: "))
            resultado = calcular_logaritmo(base, numero)
            print("El logaritmo de", numero, "en base", base, "es:", resultado)

if __name__ == "__main__":
    main()
