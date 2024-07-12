'''Crear un programa que solicite al usuario que ingrese una contraseña
mediante prompt.
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no
coincidir, volver a solicitarla hasta que coincidan.'''

contrasena_correcta = "utn750"

ingreso_contrasena = input("ingrese su contraseña: ")

while ingreso_contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intente nuevamente.")

    ingreso_contrasena=input("Ingrese su contraseña: ")

print("Contraseña correcta. Acceso concedido.")