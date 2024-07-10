'''Crear un programa que a partir del ingreso de la altura de un
basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
medir más de 1.80 metros'''

altura=float(input("Ingrese la altura del basquebolista en metros: "))
if altura > 1.80:
    print("El basquetbolista pivot")
else:
    print("El basquetbolista no es pivot")