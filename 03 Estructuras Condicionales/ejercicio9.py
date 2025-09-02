"""
Ejercicio 9: 
Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
"""
# Pedimos al usuario que ingrese la magnitud del terremoto
magnitud = int(input("Por favor ingrese la magnitud del terremoto: "))
# Verifica cada una de las condiciones
if magnitud <3:
    print ("Menor que 3: 'Muy Leve' (Imperceptible)")
elif magnitud >=3 and magnitud <4:
    print ("Mayor o igual que 4 y menor que 5: 'Moderado' (sentido por pessoas, pero generalmente no causa daños)")
elif magnitud >=5 and magnitud <6:
    print ("Mayor o igual que 5 y menor que 6: 'Fuerte' (Puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud <7:
    print ("Mayor o igual que 6 y menor que 7: 'Muy Fuerte' (Puede causar daños significativos)")
else:
    print ("Mayor o igual que 7: 'Extremo' (Puede causar graves daños a gran escala)")