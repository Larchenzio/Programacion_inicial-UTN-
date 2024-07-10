'''cree un programa que calcule el promedio de un alumno, ingresando su
nombre apellido, 3 notas, que muestre al final las leyendas pertinentes'''

nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1 + nota2 + nota3)/3
    
print(f"\nAlumno: {nombre} {apellido}\n")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")    
print(f"\nEl promedio de {nombre} {apellido} es de {promedio:.2f}\n")