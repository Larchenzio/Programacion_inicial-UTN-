'''Cree un programa que pida el nombre, número de comisión, asignatura,
docente y si el usuario estuvo presente, luego que muestre los datos por
consola con las leyendas pertinentes'''

nombre = input("Ingrese su Nombre: ")
comision = int(input("Ingresar número de comision: "))
asignatura = input("Ingrese asignatura: ")
docente = input("Ingrese el nombre del docente: ")
presente= input("¿Estuvo presente? (SI/NO) : ")

print('\n Los datos ingresados: \n')
print("Tu nombre es: ",nombre)
print("Tu número de comisión es: ",comision)
print("La asignatura es: ",asignatura)
print("El docente es: ",docente)
print("Presente: ",presente)