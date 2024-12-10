import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex10 import Ui_MainWindow

class somaAteN(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.somaN)

    def somaN(self):
        try:
            num = int(self.ui.num.text())
            soma = sum(range(1, num + 1))
            self.ui.result.setText(f"A soma dos números de 1 até {num} é: {soma}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = somaAteN()
    janela.show()
    sys.exit(app.exec_())