'''Enunciado:

De los 3 Jugadores de un Reality Show, se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan mediante input()'''

nombre_max_votos=""
nombre_min_votos=""
max_votos=float('-inf')
min_votos=float('inf')
edad_min=26 #Definimos como edad minima 26 años, ya que debe ser mayor de 25 años

suma_edades = 0
total_votos = 0
jugadores = 0

while jugadores < 3:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad (Mayor a 25): "))
    
    if edad <= edad_min:
        print("La edad debe ser mayor a 25.")
        edad = int(input("Ingrese su edad (mayor a 25): "))
    
    votos = int(input("Cantidad de votos (No menor a cero): "))
    
    if votos < 0:
        print("La cantidad de votos no puede ser menor a cero.")
        votos = int(input("Cantidad de votos (No menor a cero): "))

    if votos > max_votos:
        max_votos = votos
        nombre_max_votos = nombre

    if votos < min_votos:
        min_votos = votos
        nombre_min_votos = nombre
        edad_min = edad
        
    
    jugadores += 1 
    total_votos += votos
    suma_edades += edad
    promedio_edad = suma_edades // jugadores

print("\nResultados:")
print("El nombre del mas votado es: ", nombre_max_votos)
print("El nombre del menos votado es: ", nombre_min_votos,"con", edad_min, "años")
print("El total de votos emitidos fue de: ", total_votos)
print("El promedio de edades de los candidatos es: ", promedio_edad)
