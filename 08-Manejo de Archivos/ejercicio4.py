"""
Ejercicio 4:  Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""

diccionario_productos = []

with open("./08-Manejo de Archivos/productos.txt", "r") as archivo:
    for line in archivo:
        producto, precio, cantidad = line.strip().split(',')
        diccionario_productos.append({"nombre": producto, "precio": precio, "cantidad": cantidad})

print(diccionario_productos)