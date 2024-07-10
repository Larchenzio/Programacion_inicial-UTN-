'''Enunciado:
Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).'''

#A

print("\nBienvenido al sistema de facturación, por favor a continuacion ingrese lo solicitado\n")
producto_a=input("Ingrese producto: ")
precio_1 = float(input(f"Ingrese precio {producto_a}: "))
producto_b=input("Ingrese producto: ")
precio_2 = float(input(f"Ingrese precio {producto_b}: "))
producto_c=input("Ingrese producto: ")
precio_3 = float(input(f"Ingrese precio {producto_c}: "))
IVA = 21 #Definos el IVA como una variable

suma = (precio_1 + precio_2 + precio_3)
promedio = (precio_1 + precio_2 + precio_3) / (3)
suma_con_IVA = (precio_1 + precio_2 + precio_3) * ((1+IVA/100))


print("\nEl total de los productos ingresados es de: \n", str(suma))
print("\nEl promedio de los productos es de: \n", str(promedio))
print("\nEl total de los productos con IVA incluido es de: \n", str(suma_con_IVA))