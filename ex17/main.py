import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex17 import Ui_MainWindow

class UmCemFor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.UmaCinquentaImpar)

    def UmaCinquentaImpar(self):
        num = 1
        resultado = ""
        while num <= 50:
            if num % 2 != 0:
                resultado += str(num) + ", "
            num += 1
        self.ui.result.setText(resultado[:-2])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = UmCemFor()
    janela.show()
    sys.exit(app.exec_())