'''print("Introduce algun texto en el cursor titilando...")
input()

print("Introduce algun texto en el cursor parpadeando")
valorInputGuardado = input()
print(valorInputGuardado)

algo= input("Escribir lo que sea...")
print("Hmm...", algo ,"...¿en serio?")

numero = input("Ingresa un número:")
multiplicacion = numero *  2
print(numero, "multiplicado por 2 es: ", multiplicacion) # En este caso al no identificar que tipo de dato el resultado que arroja es 22

4. Conversión de tipos
Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().

Sus nombres indican cual es su función:

La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante);
La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).

numero = int(input("Ingresa un número: "))
algo = numero * 2
print(numero, "multiplicado por 2 es", algo)'''

#leg_a = float(input("Ingresa la longitud del primer cateto: "))
#leg_b = float(input("Ingresa la longitud del segundo cateto: "))
#ypo = (leg_a**2 + leg_b**2) ** .5
#print("La longitud de la hipotenusa es:", hypo)


#leg_a = float(input("Ingresa la longitud del primer cateto: "))
#leg_b = float(input("Ingresa la longitud del segundo cateto: "))
#print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)


fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")