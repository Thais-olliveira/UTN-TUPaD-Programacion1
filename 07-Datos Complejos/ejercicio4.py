"""
Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""

def cargar_contactos():
    num_telefonicos = {}
    for i in range(5):
        nombre = input("Ingrese el nombre: ")
        numero = input("Ingrese el número telefónico: ")
        num_telefonicos[nombre] = numero
    return num_telefonicos

def consultar_contactos(num_telefonicos):
    numero_asociado = input("Ingrese un nombre para verificar su numero asociado: ")
    if numero_asociado in num_telefonicos:
        print(num_telefonicos[numero_asociado])
    else:
        print (f"{numero_asociado} no existe en la lista de contactos")

num_telefonicos = cargar_contactos()
consultar_contactos(num_telefonicos)