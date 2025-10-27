"""
Ejercicio 10: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

invertido = {pais: capital for capital, pais in original.items()}
print(invertido)