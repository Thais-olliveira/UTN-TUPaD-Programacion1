"""
Ejercicio 10: 
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. 
"""

hemisferio = (input("Por favor ingrese en cuál hemisferio se encontra (N/S): ")).lower()
mes = (input("Por favor ingrese que mes del año: ")).lower()
dia = int(input("Por favor ingrese que día es: "))

if hemisferio == "n":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("Invierno")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("Primavera")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        print("Verano")
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("Otoño")

elif hemisferio == "s": 
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("Verano")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("Otoño")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        print("Invierno")
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("Primavera")
else:
    print("Hemisferio inválido. Use 'N' o 'S'.")

