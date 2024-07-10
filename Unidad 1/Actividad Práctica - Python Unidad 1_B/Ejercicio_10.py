'''Cree un programa en el cual pida al usuario el nombre y la edad y muestre
por consola la edad que tentra dentro de 10 años'''

nombre_usuario = input("Ingrese su nombre de usuario: ")
edad = int(input("Ingrese su edad: "))

'''En es caso genero esta variable porque aca me pide que calcule cuanto tendra
el usuario dentro de 10 años, pero si el enunciado cambia y me pide 20 años por ejemplo solo debo cambiar este dato'''
años = 10 

calculo = edad + años
print(f"\nUsted {nombre_usuario} en {años} años tendra {calculo}\n")