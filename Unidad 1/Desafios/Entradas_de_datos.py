#nombre_de_usuario= input("Ingresá tu nombre: ")
#print(nombre_de_usuario)

'''num= input("Poné un número: ")
print("El doble del número es...")
print(num*2)''' 

#Nos devuelve dos veces el numero que ponemos en vez de multiplicar ese numero por 2, ya que lo toma como una cadena de caracteres
#La funcion input siempre retorna el dato como cadenas de caracteres, los trata como si fueren palabras.

#Para que que ese numero que lo trata como una cadena, le agregamos adelante la funcion int
#asi puede tratarlo como un numero entero.

num= int(input("Poné un número: "))
print("El doble del número es...")
print(num*2) 