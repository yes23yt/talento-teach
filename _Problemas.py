# Calculadora básica
def calculadora():
    operacion = input("Introduce la operación (+, -, *, /): ")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == "+":
        print(f"Resultado: {num1 + num2}")
    elif operacion == "-":
        print(f"Resultado: {num1 - num2}")
    elif operacion == "*":
        print(f"Resultado: {num1 * num2}")
    elif operacion == "/":
        print(f"Resultado: {num1 / num2}")
    else:
        print("Operación no válida")

calculadora()

# Juego de adivinanza
import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print(f"¡Adivinaste! El número era {numero_aleatorio}. Lo lograste en {intentos} intentos.")
        break
