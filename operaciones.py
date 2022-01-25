def mundo_basura():
    estado_meta = {'A': '0', 'B': '0', 'C': '0'}
    costo = 0
    acciones(estado_meta, costo)


def acciones(estado_meta, costo):
    input_ubicacion = input("Ingrese la ubicacion: ")
    input_status = input(
        "Ingrese el estado del punto inicial: ")  # ! limpio o sucio (0,1)
    input_suciolimpio = input("Ingrese el estado otra habitacion: ")
    print("La ubicacion inicial es:" + str(estado_meta))

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

               if input_ubicacion == '1':
                   """"""