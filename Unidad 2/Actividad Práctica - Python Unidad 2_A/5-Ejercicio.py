'''Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad.'''

edad = int(input("Ingrese su edad: "))

if edad < 10:
    print("Niño/a")
elif 10 <= edad < 13:
    print("Pre-adolescente")
elif 13 <= edad < 18:
    print("Adolescente")
else:
    print("Mayor de edad")