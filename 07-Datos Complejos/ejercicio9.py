"""
Ejercicio 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.
"""
agenda = {
    ("lunes","10:00"): "Reunion",
    ("martes","15:00"): "Clase de inglés",
    ("miercoles","19:00"): "Pilates",
    ("jueves","13:00"): "Almuerzn con el equipo",
    ("viernes","21:00"): "Vuelo"
}

dia = input('Ingrese el dia: ')
hora = input('Ingrese la hora: ')
evento = agenda.get((dia, hora), 'No hay evento en ese dia y hora')
print(evento)