"""
Ejercicio 8:  Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
productos_diccionario = {
    'Producto 1': 5,
    'Producto 2': 7,
    'Producto 3': 9
}

def productos_stock (productos_diccionario):
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    if nombre_producto in productos_diccionario:
        stock = productos_diccionario[nombre_producto]
        print(f"Producto: {nombre_producto}, Stock: {stock}")
    else:
        print(f"El producto {nombre_producto} no se encuentra en el inventario.")
        
    return productos_diccionario
    
def agregar_unidades(productos_diccionario):
    nombre_producto = input("Ingrese el nombre del producto que desea agregar stock: ")
    
    if nombre_producto in productos_diccionario:
        cantidad_ingresada = int(input("Ingrese la cantidad que desea agregar stock: "))
        nuevo_stock = productos_diccionario[nombre_producto]
        productos_diccionario[nombre_producto] = nuevo_stock + cantidad_ingresada
        print(f"Nuevo stock de {nombre_producto}: {productos_diccionario[nombre_producto]}")
    else:
        print(f"El producto {nombre_producto} no existe en el inventario.")
        
    return productos_diccionario
        
def agregar_nuevo_producto (productos_diccionario):
    nombre_producto = input("Ingrese el nombre del producto: ")
    for i in range(1):
        if nombre_producto not in productos_diccionario:
            stock_producto = input("Ingrese el stock del producto: ")
            productos_diccionario[nombre_producto] = stock_producto
            print("Produto agregado!")
            print(productos_diccionario)
        else:
            print(f"Ya existe el producto {nombre_producto} con {stock_producto}unidades")
    return productos_diccionario

#Programa Principal
def main ():
    global productos_diccionario
    
    while True:
        print("Menu:")
        print("1. Consultar el stock:")
        print("2. Agregar unidades a un producto ya existente:")
        print("3. Agregar un nuevo producto:")
        print("4. Salir:")
    
        opcion = int(input("Ingrese le opcion deseada:"))
    
        if opcion == 1:
            productos_diccionario = productos_stock(productos_diccionario)
        elif opcion == 2:
            productos_diccionario = agregar_unidades(productos_diccionario)
        elif opcion == 3:
            productos_diccionario = agregar_nuevo_producto(productos_diccionario)
        elif opcion == 4:
            print("Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intente nuevamente.")
main()