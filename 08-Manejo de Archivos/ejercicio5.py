"""
Ejercicio 5:  Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
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

productos = lista_productos()
nombre_producto = input("Ingrese el nombre del producto: ")
producto = recorrer_producto(productos, nombre_producto)

if producto:
    print(producto)
else:
    print("Este producto no existe en la lista, intente nuevamente")