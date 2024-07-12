'''Crear un programa que solicite 5 números mediante prompt. Calcular la
suma acumulada y el promedio de los números ingresados.'''


suma = 0 
contador = 0  
while contador < 5:
        numero = float(input("Ingrese un número: "))
        suma += numero
        contador += 1
print("La suma acumulada es:", suma)
