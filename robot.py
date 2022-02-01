import sys
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QRect, QPoint, QSize
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import (
    QPainter,
    QPen,
    QFont,
    QColor,
    QLinearGradient,
    QGradient,
    QPainterPath,
    QPixmap,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # configuracion actual de la ventana
        self.ancho = 1360
        self.alto = 768
        self.costo = 0
        self.initGUI()

    def initGUI(self):
        # inicializacion de la ventana
        self.setGeometry(50, 50, self.ancho, self.alto)
        self.setWindowTitle("Mundo basrua.")

        # inicializacion de los botones
        self.boton_iniciar = QPushButton("Iniciar", self)
        self.boton_iniciar.move(50, 50)
        self.boton_iniciar.clicked.connect(self.iniciar)

        self.position = QLineEdit(self)
        self.position.move(80, 20)
        self.position.resize(200, 32)

        self.statusA = QLineEdit(self)
        self.statusA.move(80, 80)
        self.statusA.resize(200, 32)

        self.statusB = QLineEdit(self)
        self.statusB.move(80, 120)
        self.statusB.resize(200, 32)

        self.statusC = QLineEdit(self)
        self.statusC.move(80, 160)
        self.statusC.resize(200, 32)

        # Dibujar la caja de texto
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Inicio:')
        self.nameLabel.move(20, 20)

        self.nameLabelA = QLabel(self)
        self.nameLabelA.setText('Estado A:')
        self.nameLabelA.move(20, 80)

        self.nameLabelB = QLabel(self)
        self.nameLabelB.setText('Estado B:')
        self.nameLabelB.move(20, 120)

        self.nameLabelC = QLabel(self)
        self.nameLabelC.setText('Estado C:')
        self.nameLabelC.move(20, 160)

        # inicializacion del puzzle

        self.show()

    def iniciar(self):

        status_list = []
        posicion = self.position.text()
        status_list.append(int(self.statusA.text()))
        status_list.append(int(self.statusB.text()))
        status_list.append(int(self.statusC.text()))

        self.iniciar_limpieza(posicion, status_list, 0)

    def iniciar_limpieza(self, ubicacion, mapa, costo):

        # Si la posicion inicial es A
        if ubicacion == 'A':
            if mapa != [0, 0, 0]:  # SI el mapa no esta limpio
                print('Robot se encuentra en A.')

                # self.aspiradoraA()
                sleep(10)
                # Si la posicion A se encuentra sucio.
                if mapa[0] == 1:
                    print('La posicion actual "A" esta sucia.')
                    # self.basuraA()
                    sleep(10)
                    mapa[0] = 0  # limpia la ubicacion actual
                    costo += 1
                    self.limpiarA
                    print('la ubicacion "A" ha sido limpiada.')
                    sleep(10)
                    # Si la posicion B se encuentra sucio.
                    if mapa[1] == 1:
                        self.basuraB()
                        print('\nLa posicion "B" se encuentra sucia.')
                        sleep(10)
                        self.flechaAB()
                        print('Robot moviendose hacia "B"')
                        sleep(10)
                        self.aspiradoraB()
                        ubicacion = 'B'
                        costo += 1
                        self.limpiarB
                        sleep(10)
                        mapa[1] = 0  # limpia la ubicacion actual
                        costo += 1
                        print("La ubicacion B esta limpia.")

                        # Si la posicion C se encuentra sucio.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion C se encuentra sucia.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            costo += 1
                            ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "A" se encuentra limpia')
                    # Si la posicion B se encuentra sucio.
                    if mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        ubicacion = 'B'
                        costo += 1
                        mapa[1] = 0  # limpia la ubicacion actual
                        costo += 1
                        print("La ubicacion B esta limpia.")

                        # Si la posicion C se encuentra sucio.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion C se encuentra sucia.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            costo += 1
                            ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")
        # Si la ubicacion inicial es "B".
        elif ubicacion == 'B':
            if mapa != [0, 0, 0]:  # SI el mapa no esta limpio
                print('Robot se encuentra en B.')
                # Si la posicion B se encuentra sucio.
                if mapa[1] == 1:
                    print('La posicion actual "B" esta sucia.')
                    mapa[1] = 0  # limpia la ubicacion actual
                    costo += 1
                    print('la ubicacion "B" ha sido limpiada.')

                    # Si la posicion A se encuentra sucio.
                    if mapa[0] == 1:
                        print('\nLa posicion "A" se encuentra sucia.')
                        print('Robot moviendose hacia "A"')
                        ubicacion = 'A'
                        costo += 1
                        mapa[0] = 0  # limpia la ubicacion actual
                        costo += 1
                        print("La ubicacion A esta limpia.")

                        # Si la posicion C se encuentra sucio.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "B"')
                            costo += 1
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion A se encuentra limpia
                    else:
                        print('\nLa posicion "A" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion C se encuentra sucia.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "B" se encuentra limpia.')
                    # Si la posicion A se encuentra sucio.
                    if mapa[0] == 1:
                        print('\nLa posicion "A" se encuentra sucia.')
                        print('Robot moviendose hacia "A"')
                        ubicacion = 'A'
                        costo += 1
                        mapa[0] = 0  # limpia la ubicacion actual
                        costo += 1
                        print('La ubicacion "A" esta limpia.')

                        # Si la posicion C se encuentra sucio.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            costo += 1
                            ubicacion = 'B'
                            print('Robot moviendose hacia "C"')
                            ubicacion = 'C'
                            costo += 1
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "A" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion C se encuentra sucia.
                        if mapa[2] == 1:
                            print('\nLa posicion "C" se encuentra sucia.')
                            print('Roboto moviendose hacia "C"')
                            costo += 1
                            ubicacion = 'C'
                            mapa[2] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion C esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "C" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")
        # Si la ubicacion inicial es "C".
        elif ubicacion == 'C':
            if mapa != [0, 0, 0]:  # SI el mapa no esta limpio
                print('Robot se encuentra en C.')
                # Si la posicion C se encuentra sucio.
                if mapa[2] == 1:
                    print('La posicion actual "C" esta sucia.')
                    mapa[2] = 0  # limpia la ubicacion actual
                    costo += 1
                    print('la ubicacion "C" ha sido limpiada.')

                    # Si la posicion B se encuentra sucio.
                    if mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        ubicacion = 'B'
                        costo += 1
                        mapa[1] = 0  # limpia la ubicacion actual
                        costo += 1
                        print("La ubicacion B esta limpia.")

                        # Si la posicion A se encuentra sucio.
                        if mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Robot moviendose hacia "A"')
                            ubicacion = 'A'
                            costo += 1
                            mapa[0] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion A esta limpia.")
                        # SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion A se encuentra sucia.
                        if mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            costo += 1
                            ubicacion = 'B'
                            print('Robot moviendose hacia "A"')
                            ubicacion = 'A'
                            costo += 1
                            mapa[0] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion A esta limpia.")
                        # SI la posicion C se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                else:
                    print('La posicion "C" se encuentra limpia')
                    # Si la posicion B se encuentra sucio.
                    if mapa[1] == 1:
                        print('\nLa posicion "B" se encuentra sucia.')
                        print('Robot moviendose hacia "B"')
                        ubicacion = 'B'
                        costo += 1
                        mapa[1] = 0  # limpia la ubicacion actual
                        costo += 1
                        print("La ubicacion B esta limpia.")

                        # Si la posicion A se encuentra sucio.
                        if mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Robot moviendose hacia "A"')
                            ubicacion = 'A'
                            costo += 1
                            mapa[0] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion A esta limpia.")
                        # SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
                    # SI la posicion B se encuentra limpia
                    else:
                        print('\nLa posicion "B" se encuentra limpia.')
                        print('el robot mantiene su posicion actual.')
                        # SI la posicion A se encuentra sucia.
                        if mapa[0] == 1:
                            print('\nLa posicion "A" se encuentra sucia.')
                            print('Roboto moviendose hacia "B"')
                            costo += 1
                            ubicacion = 'B'
                            print('Robot moviendose hacia "A"')
                            ubicacion = 'A'
                            costo += 1
                            mapa[0] = 0  # limpia la ubicacion actual
                            costo += 1
                            print("La ubicacion A esta limpia.")
                        # SI la posicion A se encuentra limpia.
                        else:
                            print('\nLa posicion "A" se encuentra limpia.')
                            print('el robot mantiene su posicion actual.')
            else:
                print("Todos los campos se encuentran limpios.")

        print("\nEl robot ha terminado")
        print("El robot termino en:", ubicacion)

    def paintEvent(self, event):
        # inicializacion del painter
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        # qp.setFont(QFont("", 10))
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        col.setNamedColor('#f4f4f4')
        qp.setPen(col)
        qp.setBrush(QColor(100, 10, 10, 40))
        qp.drawRect(15, 200, 300, 450)
        qp.drawRect(400, 200, 300, 450)
        qp.drawRect(800, 200, 300, 450)

        #im = QPixmap("./basura.png")
        #direccion = QRect(15, 400, 246, 246)
        #qp.drawPixmap(direccion, im)
        #direccion1 = QRect(400, 400, 246, 246)
        #qp.drawPixmap(direccion1, im)
        #direccion2 = QRect(800, 400, 246, 246)
        #qp.drawPixmap(direccion2, im)

        self.aspiradoraA(qp, self.event)
        self.basuraA(qp, self.event)
        # dibujar las recamaras
        # Dibujar la basura dependiendo de los inputs del usuario en la caja de texto.
        # Dibujar la aspiradora en su estado iniciar

        # dibujar los misioneros y canibales segun el estado actual
        # dibujar la aspiradora dependiendo del estado
        # Seera algo de este estilo. donde if self.estado[0] == "estado":

    def aspiradoraA(self, qp, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        im = QPixmap("./robot.png")
        direccion = QRect(15, 200, 320, 126)
        qp.drawPixmap(direccion, im)

    def aspiradoraB(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./robot.png")
        direccion = QRect(400, 200, 320, 126)
        qp.drawPixmap(direccion, im)

    def aspiradoraC(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./robot.png")
        direccion = QRect(800, 200, 320, 126)
        qp.drawPixmap(direccion, im)

    def flechaAB(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./FlechaDerecha.png")
        direccion = QRect(300, 200, 100, 126)
        qp.drawPixmap(direccion, im)

    def flechaBC(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./FlechaDerecha.png")
        direccion = QRect(700, 200, 100, 126)
        qp.drawPixmap(direccion, im)

    def flechaCB(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./FlechaIzquierda.png")
        direccion = QRect(700, 200, 100, 126)
        qp.drawPixmap(direccion, im)

    def flechaBA(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./FlechaIzquierda.png")
        direccion = QRect(300, 200, 100, 126)
        qp.drawPixmap(direccion, im)

    def basuraA(self, qp, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./basura.png")
        direccion = QRect(15, 400, 246, 246)
        qp.drawPixmap(direccion, im)

    def basuraB(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./basura.png")
        direccion = QRect(400, 400, 246, 246)
        qp.drawPixmap(direccion, im)

    def basuraC(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./basura.png")
        direccion = QRect(800, 400, 246, 246)
        qp.drawPixmap(direccion, im)

    def limpiarA(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./Escoba.png")
        direccion = QRect(15, 400, 246, 246)
        qp.drawPixmap(direccion, im)

    def limpiarB(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./Escoba.png")
        direccion = QRect(400, 400, 246, 246)
        qp.drawPixmap(direccion, im)

    def limpiarC(self):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QPen(QColor(0, 0, 0, 0), 1))
        col = QColor(2, 0, 0)
        im = QPixmap("./Escoba.png")
        direccion = QRect(800, 400, 246, 246)
        qp.drawPixmap(direccion, im)

# Codigo de prueba.


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
