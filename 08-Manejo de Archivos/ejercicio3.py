"""
Ejercicio 3: 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""
with open("./08-Manejo de Archivos/productos.txt", "a") as archivo:
    producto = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    archivo.write(f"{producto},{precio},{cantidad}\n")
    print ("Producto Agregado correctamente")