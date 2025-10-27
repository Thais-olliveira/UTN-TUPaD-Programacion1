"""
Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.

"""

def notas_alumnos():
    notas_alumnos = {}
    promedios = {}

    for i in range(3):
        nombre = input("Ingrese el nombre: ")
        nota_1 = float(input("Ingrese la primera nota: "))
        nota_2 = float(input("Ingrese la segunda nota: "))
        nota_3 = float(input("Ingrese la tercera nota: "))

        notas_alumnos[nombre] = (nota_1, nota_2, nota_3)

        promedio = (nota_1 + nota_2 + nota_3) / 3
        promedios[nombre] = promedio 

    return promedios

resultado = notas_alumnos()
print("\nPromedios de los alumnos:")
for nombre, promedio in resultado.items():
    print(f"{nombre}: {promedio:.2f}")