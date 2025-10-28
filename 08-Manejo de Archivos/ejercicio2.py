"""
Ejercicio 2: Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato
"""

with open("./08-Manejo de Archivos/productos.txt", "r") as archivo:
    for linea in archivo:
        producto, precio, cantidad = linea.strip().split(',')
        print(f"Producto: {producto} - Precio: ${precio} - Cantidad: {cantidad}")