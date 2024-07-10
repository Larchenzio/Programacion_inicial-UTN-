'''Escribe un programa que muestre por consola el resultado de la siguiente
operación (10+3) * (6+6), ¿qué sucede si realizas la misma operación pero sin
los paréntesis?'''

print((10 + 3)*( 6 + 6)) #Al encerrarlo entre parentesis le da la prioridad a las operaciones dentro de ellas (resultado = 156)

print(10 + 3 * 6 +6 ) #En este caso al no contar con los parentesis,  primero hace la multiplicacion y luego las suma (resultados = 34)

