"""
Ejercicio 2: Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""
productos = []
lista_productos = []
producto_remove = []
#Solicita al usuario ingresar hasta 5 productos
while len(lista_productos) < 5:
    producto = input("Ingrese los productos: ").lower()
    if producto:
        lista_productos.append(producto)
#Ordena los productos alfabeticamente
productos_ordenados = sorted (lista_productos)

print("Lista ordenada:", productos_ordenados)

eliminar = input("Desea eliminar algun producto (S/N): ").strip().lower()

if eliminar == "s":
    producto_eliminar = input("Cual producto desea eliminar: ").strip().lower()

    if producto_eliminar in productos_ordenados:
        productos_ordenados.remove(producto_eliminar)
        print(f"{producto_eliminar} fue eliminado correctamente.")
    else:
        print(f"{producto_eliminar} no está en la lista.")
else:
    print("No se eliminó nada.")

print("Lista final:", productos_ordenados)
