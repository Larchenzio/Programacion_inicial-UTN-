'''Crear un programa que solicite al usuario que ingrese una letra. Se deberá
validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que
la condición se cumpla'''

letra1="U"
letra2="T"
letra3="N"

letra=input("Ingrese una letra: ")

while letra != letra1 and letra != letra2 and letra != letra3:

    print("Letra incorrecta: ")

    letra=input("Ingrese una letra: ")
    
print("opcion correcta: ", letra)
