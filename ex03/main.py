import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex3 import Ui_MainWindow

class fatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.factorial)

    def factorial(self):
        try:
            num = int(self.ui.num.text())
            if num < 0:
                QMessageBox.warning(self, "Erro", "Apenas números positivos")
            elif num == 0:
                self.ui.result.setText("1")
            else:
                result = 1
                for i in range(1, num + 1):
                    result *= i
                self.ui.result.setText(str(result))
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = fatorial()
    janela.show()
    sys.exit(app.exec_())