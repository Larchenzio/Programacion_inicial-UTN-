secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
| ¿Cuál es el número secreto? |
+================================+
""")
numero_ingresado = int(input("Ingresa el número secreto: "))

while numero_ingresado != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero_ingresado = int(input("Ingresa el número secreto: "))

print(
"""
+================================+
| ¡Bien hecho, Junior!            |
| Eres libre ahora.               |
| El número secreto era """ + str(secret_number) + """. |
+================================+
""")