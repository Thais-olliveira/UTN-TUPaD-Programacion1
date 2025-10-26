"""
Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función
"""

def segundos_a_horas(segundos):
    total_horas = segundos / 3600
    return total_horas

segundos = int(input("Ingrese los segundos: "))

print(f"{segundos} segundos son equivalentes a {segundos_a_horas(segundos):.2f} horas")




