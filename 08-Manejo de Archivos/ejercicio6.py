"""
Ejercicio 6: Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""

def lista_productos():
    productos = []
    with open("./08-Manejo de Archivos/productos.txt", "r") as archivo:
        for line in archivo:
            producto, precio, cantidad = line.strip().split(",", 2)
            productos.append({"nombre": producto, "precio": precio, "cantidad": cantidad})
            
    return productos

def recorrer_producto(productos, nombre_producto):
    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            return producto
    return None

def agregar_producto(productos):
    with open("./08-Manejo de Archivos/productos.txt", "a") as archivo:
        producto = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")
        archivo.write(f"{producto},{precio},{cantidad}\n")
        print ("Producto Agregado correctamente")
    return productos

productos = lista_productos()
print(productos)

producto = recorrer_producto(productos, "Goma")
print = (producto)

producto = agregar_producto(productos)
recorrer_producto(productos)

