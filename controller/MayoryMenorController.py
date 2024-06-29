from PyQt5 import QtWidgets, uic

class MayoryMenorController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana =uic.loadUi("view/frmmayoorymenor.ui")
        self.ventana.show()
        app.exec()