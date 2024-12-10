import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex5 import Ui_MainWindow

class verPrimo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.primoVerify)

    def primoVerify(self):
        try:
            num = int(self.ui.num.text())
            if num <= 1:
                self.ui.result.setText(f"{num}  não é um número primo.")
            else:
                for i in range(2, num):
                    if (num % i) == 0:
                        self.ui.result.setText(f"{num}  não é um número primo.")
                        return
                self.ui.result.setText(f"{num}  é um número primo.")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = verPrimo()
    janela.show()
    sys.exit(app.exec_())