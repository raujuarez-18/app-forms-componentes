from PyQt5 import QtWidgets, uic
from service import CalculadoraService

class CalculadoraController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana =uic.loadUi("view/frmcalculadora.ui")
        self.ventana.btcalcular.clicked.connect(self.onclickbtcalcular)
        self.ventana.show()
        app.exec()
    
    def onclickbtcalcular(self):
        resultado = 0
        operacion = ""
        try:
            num1 = int(self.ventana.txtnumero1.text())
            num2 = int(self.ventana.txtnumero2.text())
            if self.ventana.rbsuma.isChecked():
                resultado =  CalculadoraService.suma(num1,num2)
                operacion = "Suma"
            elif self.ventana.rbresta.isChecked():
                resultado =  CalculadoraService.resta(num1,num2)
                operacion = "Resta"
            elif self.ventana.rbmultiplica.isChecked():
                resultado =  CalculadoraService.multiplicacion(num1,num2)
                operacion = "Multiplicacion"
            elif self.ventana.rbdivide.isChecked():
                resultado =  CalculadoraService.divicion(num1,num2)
                operacion = "Divicion"
            else:
                resultado = 0
                operacion = "Elegir operacion"
        except:
            operacion = "Ingrese valor numéricos"
        finally:
            self.ventana.label_4.setText(operacion+ " = "+ 
                                         str(resultado))