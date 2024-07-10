'''Enunciado:
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).'''

#A

precio_1 = float(input("Ingrese precio producto A: "))
precio_2 = float(input("Ingrese precio producto B: "))
precio_3 = float(input("Ingrese precio producto C: "))

suma = (precio_1 + precio_2 + precio_3)

print("El total es: ", suma)

#B

precio_1 = float(input("Ingrese precio producto A: "))
precio_2 = float(input("Ingrese precio producto B: "))
precio_3 = float(input("Ingrese precio producto C: "))
promedio = (precio_1 + precio_2 + precio_3) / (3)

print("El promedio es de: ", promedio)

#C

precio_1 = float(input("Ingrese precio producto A: "))
precio_2 = float(input("Ingrese precio producto B: "))
precio_3 = float(input("Ingrese precio producto C: "))
IVA = 21 #Definos el IVA como una variable
suma = (precio_1 + precio_2 + precio_3) * (1+IVA/100)

print("El total con IVA incluido es de: ",suma)