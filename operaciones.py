from os import stat


def mundo_basura():
    estado_meta = {'A': '0', 'B': '0', 'C': '0'}
    costo = 0
    acciones(estado_meta, costo)


def acciones(estado_meta, costo):
    input_ubicacion = input("Ingrese la ubicacion: ")
    input_status = input(
        "Ingrese el estado del punto inicial: ")  # ! limpio o sucio (0,1)
    input_suciolimpio = input("Ingrese el estado de B: ")
    input_suciolimpio2 = input("Ingrese el estado de C: ")
    print("La condicion inicial es:" + str(estado_meta))

    if input_ubicacion == 'A':
        print("La ubicacion es A")
        if input_status == '1':
            print("El punto inicial esta sucio")

            if input_suciolimpio == '1':
                print("La ubicacion A esta sucia")
                estado_meta['A'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion A esta limpia")

                if input_suciolimpio == '1':
                    print("La ubicacion B esta sucia")
                    print("Moviendo robot la ubicacion de B")
                    costo += 1
                    print("El costo por moverse es: " + str(costo))
                    estado_meta['B'] = '0'
                    costo += 1
                    print("El costo por limpiar a es: " + str(costo))
                    print("La ubicacion B esta limpia")

                else:
                    print("Sin accion" + str(costo))
                    print("La  ubicacion B esta limpia")

        if input_status == '0':
            print("La ubicacion A esta limpia")
            if input_suciolimpio == '1':
                print("La ubicacion B esta sucia")
                print("Moviendo robot la ubicacion de B")
                costo += 1
                print("El costo por moverse es: " + str(costo))
                estado_meta['B'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion B esta limpia")
            else:
                print("Sin accion" + str(costo))
                print(costo)
                print("La  ubicacion B esta limpia")

    elif input_ubicacion == 'B':
        print("La ubicacion es B")
        if input_status == '1':
            print("El punto inicial esta sucio")
            estado_meta['B'] = '0'
            costo += 1
            print("El costo por limpiar a es: " + str(costo))
            print("La ubicacion B esta limpia")

            if input_suciolimpio == '1':
                print("La ubicacion A esta sucia")
                print("Moviendo robot la ubicacion de A")
                costo += 1
                print("El costo por moverse es: " + str(costo))
                estado_meta['A'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion A esta limpia")

        else:
            print("costo" + str(costo))
            print("La ubicacion B esta limpia")
            if input_suciolimpio == '1':
                print("La ubicacion A esta sucia")
                print("Moviendo robot la ubicacion de A")
                costo += 1
                print("El costo por moverse es: " + str(costo))
                estado_meta['A'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion A esta limpia")
            else:
                print("Sin accion" + str(costo))
                print("La  ubicacion A esta limpia")

    elif input_ubicacion == 'C':
        print("La ubicacion es C")
        if input_status == '1':
            print("El punto inicial esta sucio")
            estado_meta['C'] = '0'
            costo += 1
            print("El costo por limpiar a es: " + str(costo))
            print("La ubicacion C esta limpia")

            if input_suciolimpio == '1':
                print("La ubicacion A esta sucia")
                print("Moviendo robot la ubicacion de A")
                costo += 1
                print("El costo por moverse es: " + str(costo))
                estado_meta['A'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion A esta limpia")

        else:
            print("costo" + str(costo))
            print("La ubicacion C esta limpia")
            if input_suciolimpio == '1':
                print("La ubicacion A esta sucia")
                print("Moviendo robot la ubicacion de A")
                costo += 1
                print("El costo por moverse es: " + str(costo))
                estado_meta['A'] = '0'
                costo += 1
                print("El costo por limpiar a es: " + str(costo))
                print("La ubicacion A esta limpia")
            else:
                print("Sin accion" + str(costo))
                print("La  ubicacion A esta limpia")

    # Limpieza terminada
    print("La condicion final es:" + str(estado_meta))
    print("El preformance es: " + str(costo))
