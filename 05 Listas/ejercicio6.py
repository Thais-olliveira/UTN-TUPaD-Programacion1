"""
Ejercicio 6:  Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero).
"""
num = [1, 2, 3, 4, 5, 6, 7]
num_inverso = []

for i in num:
    num_inverso = [i] + num_inverso
    
print(f"La lista invertida es {num_inverso}")

