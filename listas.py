# Crear y mostrar una lista
estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(estudiante)

# Crear y mostrar un diccionario
contacto = {"nombre": "Juan", "correo": "juan@correo.com"}
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

# Agregar elementos a una lista o actualizar un diccionario
estudiantes.append("Carlos")
contacto["telefono"] = "123456789"
print(estudiantes)
print(contacto)
