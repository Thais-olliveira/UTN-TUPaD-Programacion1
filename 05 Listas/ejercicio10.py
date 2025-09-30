"""
Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana.
"""
ventas = [
    [12, 9, 15, 10, 14, 11, 13],
    [8, 11, 13, 7, 9, 10, 12],
    [5, 7, 6, 12, 9, 8, 7],
    [14, 10, 9, 11, 13, 15, 7],
]
contador = 0
suma_pan = 0
suma_leche = 0
suma_queso = 0
suma_manzana = 0

#Percorre cada produto y suma las ventas
for i, producto in enumerate(ventas):
    if i == 0:
        suma_pan = sum(producto)
    elif i == 1:
        suma_leche = sum(producto)
    elif i == 2:
        suma_queso = sum(producto)
    elif i == 3:
        suma_manzana = sum(producto)
        
maximo = 0
dia_max = 0
#Pecorre los dias para calcular el dia que tiene mayores ventas
for dia in range(7):
    total_dia = ventas[0][dia] + ventas[1][dia] + ventas[2][dia] + ventas[3][dia]
    if total_dia > maximo:
        maximo = total_dia
        dia_max = dia + 1 

totales = [suma_pan, suma_leche, suma_queso, suma_manzana]
productos = ["Pan", "Leche", "Queso", "Manzana"] 
#Producto con mayor venta en la semana
producto_mayor_venta = [0, totales[0]] 
for posicion in range(1, 4):
    if totales[posicion] > producto_mayor_venta[1]:
        producto_mayor_venta = [posicion, totales[posicion]]
        
print(f"Total vendido por producto")
print(f"Total pan: {suma_pan}")
print(f"Total leche: {suma_leche}")
print(f"Total queso: {suma_queso}")
print(f"Total manzana: {suma_manzana}")

print(f"El dia con más ventas fue el dia {dia_max}, con un total de {maximo} productos vendidos.")
print(f"El producto más vendido fue {productos[producto_mayor_venta[0]]} con {producto_mayor_venta[1]} unidades.")