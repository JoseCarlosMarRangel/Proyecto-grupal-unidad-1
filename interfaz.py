from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys

class Recamara(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.ListaPuntos=[] 
        
    def initUI(self):      

        self.setGeometry(200, 150, 925, 500)
        self.setWindowTitle('Recamara')
        self.show()
        

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        
        self.DibujarRectanguloA(qp)
        self.DibujarRectanguloB(qp)
        self.DibujarRectanguloC(qp)
        self.DibujarCirculoA(qp)
        self.DibujarCirculoB(qp)
        self.DibujarCirculoC(qp)
        qp.end()
        
    def onClicked(self):
            self.flag = True
            self.update()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print("hola")

    

    def DibujarRectanguloA(self, qp):
        col = QColor(2, 0, 0)
        col.setNamedColor('#f4f4f4')
        qp.setPen(col)
        qp.setBrush(QColor(100, 10, 10, 40))
        qp.drawRect(15, 15, 300, 450)
        
    def DibujarRectanguloB(self, qp):
        col = QColor(2, 0, 0)
        col.setNamedColor('#f4f4f4')
        qp.setPen(col)
        qp.setBrush(QColor(100, 10, 10, 40))
        qp.drawRect(315, 15, 300, 450)

    def DibujarRectanguloC(self, qp):
        col = QColor(2, 0, 0)
        col.setNamedColor('#f4f4f4')
        qp.setPen(col)
        qp.setBrush(QColor(100, 10, 10, 40))
        qp.drawRect(615, 15, 300, 450)


    def DibujarCirculoA(self, qp):        
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.drawEllipse(110, 75, 120, 120)

    def DibujarCirculoB(self, qp):        
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.drawEllipse(410, 75, 120, 120)

    def DibujarCirculoC(self, qp):        
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.drawEllipse(710, 75, 120, 120)

    def DibujarTriangulo(self, qp):        
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.drawEllipse(710, 75, 90, 90)


        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Recamara()
    sys.exit(app.exec_())