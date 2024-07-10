nombre_de_usuario=input("Ingresa tu nombre: ")
print("Hola",nombre_de_usuario,"!!!") #Para concatenar puedo utilizar , (coma)

''' TENER EN CUENTA QUE Al concatenar utilizando Coma, esta incluye espacios de separación'''

'''¿Cómo modifico esto?
utilizando al final de la función print, sep="", Esto indica a Python que tipo de separación quiero entre palabra y palabra'''

nombre_de_usuario=input("Ingresa tu nombre: ")
print("Hola",nombre_de_usuario,"!!!",sep="") #Agregamos la funcion sep para delimitar que tipo de separador, en este caso no habra espacios

nombre_de_usuario=input("Ingresa tu nombre: ")
print("Hola",nombre_de_usuario,"!!!",sep="-") #Agregamos la funcion sep para delimitar que tipo de separador, en este caso utilizara - (guion)

'''tambien podemos utilizar el signo  + (mas) para concatenar
pero en esta caso actua distinto a la coma, ya que este no deja espacios'''

nombre_de_usuario=input("Ingresa tu nombre: ")
print("Hola" + nombre_de_usuario + "!!!") 

'''En caso si quiero agregar espacios lo puedo hacer de forma manual dentro de las comillas'''

nombre_de_usuario=input("Ingresa tu nombre: ")
print("Hola " + nombre_de_usuario + " !!!") 

'''La concatenacion podemos tambien incluirla dentro de una variable, no solo en la funcion print()'''

nombre_de_usuario=input("Ingresa tu nombre: ")
saludo="Hola " + nombre_de_usuario + " !!!"
print(saludo) 

'''ATENCIÓN Para concatenar Valores dentro de una variable, 
debo usar si o si el operador +, 
ya que si utilizo coma, estoy formando una estructura de datos(ahora no importa)'''

nombre_de_usuario=input("Ingresa tu nombre: ")
saludo="Hola " , nombre_de_usuario , " !!!"
print(saludo) 

'''Saldra de la siguiente forma Ingresa tu nombre: lalo
('Hola ', 'lalo', ' !!!')'''

#RECORDAR QUE EL OPERADOR + SOLO CONCATENARÁ VALORES DE TIPO CADENA (STRING O str) 

'''edad_de_usuario=int(input("Ingrese su edad: "))
saludo2="Tenés " + edad_de_usuario + " años"
print(saludo2)

#Este es el error que arroja si no lo tratamos como str
 saludo2="Tenés " + edad_de_usuario + " años"
            ~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "int") to str'''

#edad_de_usuario=int(input("Ingrese su edad: "))
#saludo2="Tenés " + str(edad_de_usuario) + " años"
#print(saludo2) #Modo correcto de representarlo para que no arroje el error

'''Aquí en una primera instancia, Python toma el dato ingresado por el usuario como un número entero (int), 
pero luego, solo por la variable saludo2, lo expresa como cadena de caracteres. 
ESTO NO APLICA A LA CONCATENACIÓN POR COMA DENTRO DE print(), POR QUE YA DE POR SI, print() TOMA todo SU CONTENIDO COMO CADENA DE TEXTO'''

edad_de_usuario=int(input("Ingrese su edad: "))
#saludo2="Tenés " + str(edad_de_usuario) + " años"
print("Tenés", edad_de_usuario , "años")