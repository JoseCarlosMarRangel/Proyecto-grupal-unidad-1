# Libreria temporal para el manejo de la interfaz de comandos
import os
from time import sleep

import operaciones as op


class main:

    def __init__(self):

        Banner = "Ejecutando el programa"
        print(Banner)
        sleep(1)

        op.mundo_basura()


objeto = main()
