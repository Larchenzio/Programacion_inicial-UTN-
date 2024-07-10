'''Cree un programa que permite ingresar el nombre de un producto, el
precio y que calcule el IVA'''

producto = input("Ingrese nombre del producto: ")
precio_producto = float(input("Ingrese precio del producto: $ "))

tasa_IVA = 21  # Tasa de IVA del 21% (lo maneje de esta manera en caso de que cambie la tasa del IVA)

precio_con_IVA = (precio_producto) * (1 + tasa_IVA / 100)

print(f"\nEl total con IVA incluido es de: $ {precio_con_IVA:.2f}\n")