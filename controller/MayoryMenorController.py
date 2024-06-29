from PyQt5 import QtWidgets, uic
from service import MayorMenorService
class MayoryMenorController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana =uic.loadUi("view/frmmayorymenor.ui")
        self.ventana.btcalcular.clicked.connect(self.onclickbtcalcular)
        self.ventana.show()
        app.exec()
    
    def onclickbtcalcular(self):
        resultado = 0

        try:
            n1 = int(self.ventana.txtnumero1.text())
            n2 = int(self.ventana.txtnumero2.text())
            n3 = int(self.ventana.txtnumero3.text())
            n4 = int(self.ventana.txtnumero4.text())
            if self.ventana.rbmayor.isChecked():
                resultado = MayorMenorService.mayor(n1,n2,n3,n4)
            elif self.ventana.rbmenor.isChecked():
                resultado = MayorMenorService.menor(n1,n2,n3,n4)
            else:
                resultado = 0
        except:
            resultado = 0
        finally:
            self.ventana.label_5.setText(str(resultado))