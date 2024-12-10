import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex1 import Ui_MainWindow

class somaNum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.somaInteiros)

    def somaInteiros(self):
        try:
            num = int(self.ui.num.text())
            num2 = int(self.ui.num2.text())
            
            resultado = num + num2
            
            self.ui.result.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira números inteiros válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = somaNum()
    janela.show()
    sys.exit(app.exec_())