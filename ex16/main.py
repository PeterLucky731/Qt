import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex16 import Ui_MainWindow

class UmCemFor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.UmaCem)

    def UmaCem(self):
        numeros_pares = ""
        for i in range(1, 101):
            if i % 2 == 0:
                numeros_pares += str(i) + ", "
        self.ui.result.setText(numeros_pares[:-2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = UmCemFor()
    janela.show()
    sys.exit(app.exec_())