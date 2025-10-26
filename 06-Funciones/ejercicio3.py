"""
Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
def informacion_personal ():
    nombre = input("Ingrese tu nombre:")
    apellido = input("Ingrese tu apellido:")
    edad = int(input("Ingrese tu edad:"))
    residencia= input("Ingrese tu residencia:")
    
    saludar_persona = ("Soy "+nombre+ " "+apellido+", tengo " +str(edad)+" anõs y vivo en "+residencia+"!")
    return saludar_persona

print (informacion_personal())