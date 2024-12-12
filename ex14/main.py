import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex14 import Ui_MainWindow

class verSinal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.nuloPosNeg)

    def nuloPosNeg(self):
        try:
            num = int(self.ui.num.text())
            if num < 0:
                self.ui.result.setText("Negativo")
            elif num > 0:
                self.ui.result.setText("Positivo")
            else:
                self.ui.result.setText("Zero")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = verSinal()
    janela.show()
    sys.exit(app.exec_())