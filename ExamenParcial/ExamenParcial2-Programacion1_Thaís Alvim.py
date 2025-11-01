import csv
import os

def obtenerLibros(nombre_archivo):
    """
    Abre el archivo de catálogo y devuelve el catálogo como una lista de diccionarios.
    Si el archivo no existe, crea un catálogo vacío.
    Retorna: Lista de diccionarios con los títulos y ejemplares.
    """
    libros =[]
    
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
            escritor.writeheader()
            return libros
        
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for linea in lector:
            titulo = (linea.get("titulo") or linea.get("TITULO") or "").strip()
            cantidad_str = (linea.get("cantidad") or linea.get("CANTIDAD") or "").strip()
            if not cantidad_str.isdigit():
                continue
            libros.append({"titulo": titulo, "cantidad": int(cantidad_str)})
    return libros

def titulo_vacio(titulo):
    """
    Validación que el título ingresado no sea vacio
    Retorna: True si es válido, False si no es válido
    """
    if titulo.strip() == "":
        print("El título no puede ser vacío.")
        return False
    return True

def validar_titulo(titulo, nombre_archivo):
    """
    Validación se el título existe en el CSV
    Retorna:False si es válido, 
            True si no es válido
    """
    libros = obtenerLibros(nombre_archivo)
    for libro in libros:
        if libro["titulo"].strip().lower() == titulo.strip().lower():
            print("El título ya existe en el catálogo. Por favor, inténtelo nuevamente.")
            return True
    return False

def catalogo_vacio(catalogo):
    """
    Validación si el catálogo no esta vacio
    Retorna:True si el catálogo es válido, 
            False si no es válido.
    """
    
    if len(catalogo) == 0:
        print("El catálogo está vacío.")
        return False
    return True

def validar_cantidad (cantidad):
    """
    Valida si la cantidad de ejemplares es un numero y si es positiva.
    Retorna: True si es válido, False si no es válido.
    """
    
    cantidad_str = str(cantidad).strip()
    if not cantidad_str.isdigit():
        print("Debe ingresar un número entero válido.")
        return False
    
    cantidad_int = int(cantidad_str)
    if cantidad_int < 0:
        print("La cantidad de ejemplares no puede ser negativa.")
        return False
    return True

def agregar_LibroCatalogo(libro, nombre_archivo):
    """
    Agrega un libro en el archivo CSV
    """
    existe = os.path.exists(nombre_archivo)
    with open (nombre_archivo, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
        if not existe:
            escritor.writeheader()
        escritor.writerow(libro)

def actualizar_ejemplares(catalogo, nombre_archivo):
    """
    Actualiza la cantidad de ejemplares de un libro ya existente
    """
    
    with open (nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
        escritor.writeheader()
        escritor.writerows(catalogo)


def ingresar_titulos (nombre_archivo):
    """
    Carga múltiples libros al catálogo
    """
    
    print("---- Ingresar múltiples títulos ----")
    contador = 1
    cantidad_ingresada = (input("Ingrese la cantidad de libros a ingresar: ")).strip()
    
    cantidad_valida = validar_cantidad(cantidad_ingresada)
    if not cantidad_valida:
        return
    
    cantidad = int(cantidad_ingresada)
    
    while contador <= cantidad:
        titulo_ingresado = input("Nº"+ str(contador) + " - Ingrese el título: ").strip()
        
        titulo_valido = titulo_vacio(titulo_ingresado)
        if not titulo_valido:
            continue

        titulo_existe = validar_titulo(titulo_ingresado,nombre_archivo)
        if titulo_existe:
            continue
        
        ejemplares_ingresados = input("Ingrese la cantidad de ejemplares: ").strip()
        
        cantidad_valida = validar_cantidad(ejemplares_ingresados)
        if not cantidad_valida:
            continue

        ejemplares = int(ejemplares_ingresados)
        agregar_LibroCatalogo({"titulo": titulo_ingresado, "cantidad": ejemplares}, nombre_archivo)
        print(f"Libro '{titulo_ingresado}' agregado con {ejemplares} ejemplares.")
        contador += 1

def ingresar_ejemplares (nombre_archivo):
    """
    Suma ejemplares a un título específico
    """
    print("---- Ingresar ejemplares a un titulo ya existente ----")
    catalogo = obtenerLibros(nombre_archivo)
    
    catalogo_valido = catalogo_vacio(catalogo)
    if not catalogo_valido:
        return
    
    titulo_ingresado = input("Ingrese el titulo del libro que desea agregar ejemplares: ").strip()
    
    titulo_valido = titulo_vacio(titulo_ingresado)
    if not titulo_valido:
        return
    
    for titulo in catalogo:
        if titulo["titulo"].strip().lower() == titulo_ingresado.strip().lower():
            cantidad_ingresada = input ("Ingrese la cantidad que desea agregar: "). strip()
            
            cantidad_valida = validar_cantidad(cantidad_ingresada)
            if not cantidad_valida:
                return
            
            cantidad_ingresada = int(cantidad_ingresada)
            
            titulo["cantidad"] = int(titulo["cantidad"]) + cantidad_ingresada
            
            actualizar_ejemplares(catalogo,nombre_archivo)
            print(f"Se agregó correctamente. Nueva cantidad: {titulo['cantidad']}")
            break
            
    else:
        print ("No fue posible encontrar el título del libro")


def ingresar_Untitulo(nombre_archivo):
    """
    Agrega UN nuevo título al catálogo
    """
    while True:
        print ("--- Agregar un nuevo libro ---")
        titulo_ingresado = input ("Ingrese el título del libro: ").strip()
    
        titulo_valido = titulo_vacio(titulo_ingresado)
        if not titulo_valido:
            return
    
        titulo_existe = validar_titulo(titulo_ingresado,nombre_archivo)
        if titulo_existe:
            continue

        cantidad_ingresada = input("Ingrese la cantidad inicial:").strip()
    
        cantidad_valida = validar_cantidad(cantidad_ingresada)
        if not cantidad_valida:
            return
    
        cantidad = int(cantidad_ingresada)
        agregar_LibroCatalogo({"titulo": titulo_ingresado, "cantidad": cantidad}, nombre_archivo)
        print ("Se agregó correctamente.")
        return

def mostrar_catalogo(nombre_archivo):
    """
    Muestra el catálogo completo
    """
    print ("---- Listado de Libros y stock actual ----")
    
    catalogo = obtenerLibros(nombre_archivo)
    
    catalogo_valido = catalogo_vacio(catalogo)
    if not catalogo_valido:
        return

    for libro in catalogo:
        print (f"Título: {libro['titulo']} - Cantidad: {libro['cantidad']}")


def consultar_disponibilidad(nombre_archivo):
    """
    Consulta la disponibilidad de un título específico.\n
    """
    print ("---- Consultar disponibilidad ----")
    catalogo = obtenerLibros(nombre_archivo)
    
    catalogo_valido = catalogo_vacio(catalogo)
    if not catalogo_valido:
        return
    
    titulo_ingresado = input("Ingrese el titulo del libro que desea consultar disponibilidad: ").strip()
    
    titulo_valido = titulo_vacio(titulo_ingresado)
    if not titulo_valido:
            return
    
    for libro in catalogo:
        if libro["titulo"].strip().lower() == titulo_ingresado.strip().lower():
            print(f"Cantidad disponible del libro '{libro['titulo']}': {libro['cantidad']} ejemplar(es)")
            break
    else:
        print("No fue posible encontrar el título del libro")


def listar_agotados(nombre_archivo):
    """
    Lista los títulos que no tienen ejemplares disponibles
    """
    print ("---- Listado de Libros agotados ----")
    catalogo = obtenerLibros(nombre_archivo)
    
    catalogo_valido = catalogo_vacio(catalogo)
    if not catalogo_valido:
        return
    
    agotados = [libro for libro in catalogo if int(libro["cantidad"]) == 0]
    
    if not agotados:
        print("No hay títulos agotados")
        return

    for libro in agotados:
        print(f"Título: {libro['titulo']} - Cantidad: {libro['cantidad']}")


def prestamo_devolucion(nombre_archivo):
    """
    Realiza el préstamo o devolución de los libros 
    """
    catalogo = obtenerLibros(nombre_archivo)
    
    catalogo_valido = catalogo_vacio(catalogo)
    if not catalogo_valido:
        return
    
    titulo_ingresado = input("Ingrese el titulo del libro que desea hacer el préstamo o devolución: ").strip()
    
    titulo_valido = titulo_vacio(titulo_ingresado)
    if not titulo_valido:
            return
    
    for libro in catalogo:
        if libro["titulo"].strip().lower() == titulo_ingresado.strip().lower():
            accion = input("Ingrese 'P' para realizar un préstamo o 'D' para devolver un libro: ").lower()
            
            if accion == "p":
                if int(libro["cantidad"]) > 0:
                    libro["cantidad"] = int(libro["cantidad"]) - 1
                    print(f"Préstamo realizado con éxito. Ejemplares restantes de '{libro['titulo']}': {libro['cantidad']}")
                else:
                    print(f"No hay ejemplares disponibles para el libro '{libro['titulo']}'.")
            
            elif accion == "d":
                libro["cantidad"] = int(libro["cantidad"]) + 1
                print(f"Devolución realizada con éxito. Ejemplares disponibles de '{libro['titulo']}': {libro['cantidad']}")
            
            else:
                print("Opción no válida. Use 'P' para préstamo o 'D' para devolución.")
            
            actualizar_ejemplares(catalogo,nombre_archivo)
            break
    else:
        print("No fue posible encontrar el título del libro.")


def mostrar_menu():
    nombre_archivo = "catalogo.csv"
    
    while True:
        print("======= CATÁLOGO DE LIBROS ======")
        print("1. Ingresar títulos (varios títulos)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título (libro individual)")
        print("7. Actualizar ejemplares (préstamo/devolución)")
        print("8. Salir")
        print("===================================")
        opcion = input("Ingrese la opción deseada: ").strip()
        
        match opcion:
            case "1":
                ingresar_titulos(nombre_archivo=nombre_archivo)
            case "2":
                ingresar_ejemplares(nombre_archivo=nombre_archivo)
            case "3":
                mostrar_catalogo(nombre_archivo=nombre_archivo)
            case "4":
                consultar_disponibilidad(nombre_archivo=nombre_archivo)
            case "5":
                listar_agotados(nombre_archivo=nombre_archivo)
            case "6":
                ingresar_Untitulo(nombre_archivo=nombre_archivo)
            case "7":
                prestamo_devolucion(nombre_archivo=nombre_archivo)
            case "8":
                print("Gracias por utilizar nuestra aplicación!!")
                break
            case _:
                print("La opción seleccionada no es válida")
mostrar_menu ()


