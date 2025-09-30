titulos = []
ejemplares = []
#Bucle principal del menu
while True:
    print("\n------- Menú Biblioteca -------")
    print("1. Ingresar títulos (sin ejemplares)")
    print("2. Ingresar ejemplares (sin título)")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título (con ejemplares)")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("Ingrese el número deseado: ")
    #Valida si la opcion ingresada sea numerica.
    if not opcion.isdigit():
        print("Entrada inválida. Debe ingresar un número del 1 al 8.")
        continue
    #Convierte la variable opcion a intero.
    opcion = int(opcion)

    #Ingresar títulos.
    if opcion == 1:
        titulo = input("Ingrese el título del libro: ")
        repetido = 0
        
        if titulo == "":
            print("El título no puede estar en blanco. Intente nuevamente.")
        else:
            #Recorre los titulos para verificar titulos repetidos.
            for t in titulos:
                if t.lower() == titulo.lower():
                    repetido = 1
                    print("Título repetido. Intente nuevamente.")
                    break
            
            if repetido == 0:
                print(f"Título ingresado: {titulo}")
                titulos.append(titulo)
                ejemplares.append(0)

    #Ingresar ejemplares.
    elif opcion == 2:
        #Lista numerada para elegir el titulo.
        for i in range(len(titulos)):
            print(f"{i+1}. Libro: {titulos[i]} - {ejemplares[i]} ejemplares")
        
        posicion = input("Seleccione el número del título para añadir ejemplares:")
        if posicion == "" or not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(titulos):
            print("Entrada inválida.Intente nuevamente")
        else:    
            posicion= int(posicion) - 1       
            cantidad = input("Ingrese la cantidad de ejemplares del libro: ")
            if cantidad == "" or not cantidad.isdigit() or  int(cantidad) < 0 :
                print("Entrada inválida. Intente nuevamente")
            else:
                cantidad = int(cantidad)
                ejemplares[posicion] += cantidad 
                
                print(f"Ejemplares agregados correctamente. Ahora '{titulos[posicion]}' tiene {ejemplares[int(posicion)]} ejemplares.")

    #Mostrar catálogo.
    elif opcion == 3:
        for i in range(len(titulos)):
            print(f"Libro: {titulos[i]} - {ejemplares[i]} ejemplares")

    #Consultar disponibilidad.
    elif opcion == 4:
        buscar = input("Ingrese el nombre del libro que desea buscar: ").lower()
        if buscar == "":
            print("El título no puede estar en blanco. Intente nuevamente.")
        else:
            for i in range(len(titulos)):
                if titulos[i].lower() == buscar:
                    print(f"Libro: {titulos[i]} - {ejemplares[i]} ejemplares")
                    break
            else:
                print("Título no encontrado. Intente nuevamente.")

    #Listar agotados.
    elif opcion == 5:
        agotados = False
        
        for e in ejemplares:
            if e == 0:
                agotados = True
                break
        if agotados:
            print ("Libros Agotados:")
            for i in range(len(titulos)): 
                if ejemplares[i] == 0:
                    print(f"Libro: {titulos[i]} - {ejemplares[i]} ejemplares")
        else:
            print("Ningún título contiene 0 ejemplares.")

    #Agregar título.
    elif opcion == 6:
        titulo = input("Ingrese el título del libro: ")
        repetido = 0
        
        if titulo == "":
            print("El título no puede estar en blanco. Intente nuevamente.")
        else:
            for t in titulos:
                if t.lower() == titulo.lower():
                    repetido = 1
                    print("Título repetido. Intente nuevamente.")
                    break
            
            if repetido == 0:
                ejemplar = input("Ingrese la cantidad de ejemplares del libro: ")
                if ejemplar.isdigit():
                    #Agrega el titulo apenas si el usuario ingrese la cantidad de ejemplares.
                    titulos.append(titulo)  
                    ejemplares.append(int(ejemplar))
                    print("Libro agregado correctamente.")
                else:
                    print("Debe ingresar un número válido.")

    #Actualizar ejemplares (préstamo/devolución).
    elif opcion == 7:
        #Lista numerada para elegir el titulo.
        for i in range(len(titulos)):
            print(f"{i+1}. Libro: {titulos[i]} - {ejemplares[i]} ejemplares")
            
        posicion = input("Seleccione el número del título:")
        if posicion == "" or not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(titulos):
            print("Entrada inválida.Intente nuevamente")
        else:    
            posicion= int(posicion) - 1
                    
            accion = input("Ingrese 'P' para realizar un préstamo o 'D' para devolver un libro:").lower()
                
            if accion == "p":
                    #Verifica se el libro tiene mas que 0 ejemplares.
                    if ejemplares[posicion] > 0: 
                        #Resta uno (Préstamo).
                        ejemplares[posicion] -= 1 
                        print(f"Préstamo realizado con éxito. Ejemplares disponibles en: {titulos[posicion]}: {ejemplares[posicion]}")
                    else:
                        print("No hay ejemplares disponibles.")
            elif accion == "d":
                    #Suma uno (devolución).
                    ejemplares[posicion] += 1 
                    print(f"Devolución realizada con éxito. Ejemplares disponibles en: {titulos[posicion]}: {ejemplares[posicion]}")
            else:
                    print("Acción inválida, utilice 'P' o 'D'")

    #Salir.
    elif opcion == 8:
        print("Gracias! Hasta luego...")
        break

    #Opción fuera del menu.
    else:
        print("Opción inválida. Intente nuevamente.")
