from os import stat

"""
Robot limpiador que se encarga de limpiar valga la redundancia
un cuarto de 3 casillas con conocimiento de su area.
"""
class robot_limpiador():
    """
    el robot maneja su entorno como un arreglo de 3, el cual este se
    maneja de la siguiente forma: [0,0,0]
    el cual hacen referencia a las posiciones: A, B y C
    estos campos indican si estan sucios o no.

    Ademas el robot guarda por si mismo su propia ubicacion
    por lo que el esta siempre consciente donde se encuentra.
    """
    mapa = []

    def __init__(self, ubi, estado_mapa, costo = 0) -> None:
        self.ubicacion = ubi.upper()
        self.mapa = estado_mapa
        self.costo = costo
    
    def iniciar(self):
        
        ## Si la posicion inicial es A
        if self.ubicacion == 'A':
            if self.mapa != [0,0,0]: ## SI el mapa no esta limpio
                print('Robot se encuentra en A.')
                ## Si la posicion A se encuentra sucio.
                if self.mapa[0] == 1:
                    print('La posicion actual "A" esta sucia.')
                    self.mapa[0] = 0 ## limpia la ubicacion actual
                    self.costo +=1
                    print('la ubicacion "A" ha sido limpiada.')

                    ## Si la posicion B se encuentra sucio.
                    if self.mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        self.ubicacion = 'B'
                        self.costo += 1
                        self.mapa[1] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print("La ubicacion B esta limpia.")

                        ## Si la posicion C se encuentra sucio.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion C se encuentra sucia.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            self.costo +=1
                            self.ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "A" se encuentra limpia')
                    ## Si la posicion B se encuentra sucio.
                    if self.mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        self.ubicacion = 'B'
                        self.costo += 1
                        self.mapa[1] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print("La ubicacion B esta limpia.")

                        ## Si la posicion C se encuentra sucio.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion C se encuentra sucia.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            self.costo +=1
                            self.ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")
        ## Si la ubicacion inicial es "B".
        elif self.ubicacion == 'B':
            if self.mapa != [0,0,0]: ## SI el mapa no esta limpio
                print('Robot se encuentra en B.')
                ## Si la posicion B se encuentra sucio.
                if self.mapa[1] == 1:
                    print('La posicion actual "B" esta sucia.')
                    self.mapa[1] = 0 ## limpia la ubicacion actual
                    self.costo +=1
                    print('la ubicacion "B" ha sido limpiada.')

                    ## Si la posicion A se encuentra sucio.
                    if self.mapa[0] == 1:
                        print('\nLa posicion "A" se encuentra sucia.')
                        print('Robot moviendose hacia "A"')
                        self.ubicacion = 'A'
                        self.costo += 1
                        self.mapa[0] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print("La ubicacion A esta limpia.")

                        ## Si la posicion C se encuentra sucio.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "B"')
                            self.costo += 1
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion A se encuentra limpia
                    else:
                        print('\nLa posicion "A" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion C se encuentra sucia.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "B" se encuentra limpia.')
                    ## Si la posicion A se encuentra sucio.
                    if self.mapa[0] == 1:
                        print('\nLa posicion "A" se encuentra sucia.')
                        print('Robot moviendose hacia "A"')
                        self.ubicacion = 'A'
                        self.costo += 1
                        self.mapa[0] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print('La ubicacion "A" esta limpia.')

                        ## Si la posicion C se encuentra sucio.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            self.costo +=1
                            self.ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            self.ubicacion = 'C'
                            self.costo += 1
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "A" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion C se encuentra sucia.
                        if self.mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "C"')
                            self.costo +=1
                            self.ubicacion = 'C'
                            self.mapa[2] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion C esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")
        ## Si la ubicacion inicial es "C".
        elif self.ubicacion == 'C':
            if self.mapa != [0,0,0]: ## SI el mapa no esta limpio
                print('Robot se encuentra en C.')
                ## Si la posicion C se encuentra sucio.
                if self.mapa[2] == 1:
                    print('La posicion actual "C" esta sucia.')
                    self.mapa[2] = 0 ## limpia la ubicacion actual
                    self.costo +=1
                    print('la ubicacion "C" ha sido limpiada.')

                    ## Si la posicion B se encuentra sucio.
                    if self.mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        self.ubicacion = 'B'
                        self.costo += 1
                        self.mapa[1] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print("La ubicacion B esta limpia.")

                        ## Si la posicion A se encuentra sucio.
                        if self.mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Robot moviendose hacia "A"')
                            self.ubicacion = 'A'
                            self.costo += 1
                            self.mapa[0] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion A esta limpia.")
                        ## SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion A se encuentra sucia.
                        if self.mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            self.costo +=1
                            self.ubicacion = 'B'
                            print('Robot moviendose hacia "A"')
                            self.ubicacion = 'A'
                            self.costo += 1
                            self.mapa[0] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion A esta limpia.")
                        ## SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "C" se encuentra limpia')
                    ## Si la posicion B se encuentra sucio.
                    if self.mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        self.ubicacion = 'B'
                        self.costo += 1
                        self.mapa[1] = 0 ## limpia la ubicacion actual
                        self.costo +=1
                        print("La ubicacion B esta limpia.")

                        ## Si la posicion A se encuentra sucio.
                        if self.mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Robot moviendose hacia "A"')
                            self.ubicacion = 'A'
                            self.costo += 1
                            self.mapa[0] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion A esta limpia.")
                        ## SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    ## SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        ## SI la posicion A se encuentra sucia.
                        if self.mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            self.costo +=1
                            self.ubicacion = 'B'
                            print('Robot moviendose hacia "A"')
                            self.ubicacion = 'A'
                            self.costo += 1
                            self.mapa[0] = 0 ## limpia la ubicacion actual
                            self.costo +=1
                            print("La ubicacion A esta limpia.")
                        ## SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")

        print("\nEl robot ha terminado")
        print("El robot termino en:", self.ubicacion)

##Codigo de prueba.
if __name__ == "__main__":
    roby = robot_limpiador('c',[1,0,0])
    roby.iniciar()