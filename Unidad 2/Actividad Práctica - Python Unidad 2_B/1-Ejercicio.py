'''Crear un programa que pueda sumar los números pares comprendidos
entre el 1 y el 10.'''

inicio= 1
fin = 10
suma_pares = 0
while inicio <= fin:
    if inicio % 2 == 0:
        suma_pares += inicio
    inicio += 1
print("La suma de los números pares entre 1 y 10 es:", suma_pares)
