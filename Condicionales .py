# Verificar si un número es par o impar
numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Bucle for para imprimir los cuadrados de los números de una lista
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

# Bucle while para pedir una entrada hasta que sea válida
while True:
    respuesta = input("Escribe 'salir' para terminar: ")
    if respuesta.lower() == 'salir':
        break
