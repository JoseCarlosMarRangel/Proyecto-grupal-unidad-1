from os import stat

mundobasura = [['A', 'Limpio'], ['B', 'Limpio'], ['C', 'Limpio']]


def mundo_basura():
    acciones()


def acciones():
    posicion_inicial = input("Ingrese la ubicacion inicial: ")

    if posicion_inicial == mundobasura[0][0]:
        print("La posicion inicial es : ", mundobasura[0][0])
        mundobasura[0][1] = input("Ingrese el estado: ")
        resultado = ubicacin_A()
        print(resultado)

    elif posicion_inicial == mundobasura[1][0]:
        print("La posicion inicial es : ", mundobasura[1][0])
        mundobasura[1][1] = input("Ingrese el estado: ")

    elif posicion_inicial == mundobasura[2][0]:
        print("La posicion inicial es : ", mundobasura[2][0])
        mundobasura[2][1] = input("Ingrese el estado: ")


def ubicacin_A():
    if mundobasura[0][1] == '1':
        print("la ubicacion esta sucia")
        mundobasura[0][1] = 'Limpia'
        # print(mundobasura)
        print("Limpiando")
        return 'La ubicacion ' + mundobasura[0][0] + ' esta ' + mundobasura[0][1]
