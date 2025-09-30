"""
Ejercicio 5: 
Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string. 
"""
# Solicita al usuario que ingrese una contraseña 
contrasena_usuario = (input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: "))
# Asigna el tamaño a varible
tamaño = (len(contrasena_usuario))
#Verifica se el tamaño esta entre el rango entre 8 y 14
if tamaño >=8 and tamaño <=14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14" \
    " caracteres")
