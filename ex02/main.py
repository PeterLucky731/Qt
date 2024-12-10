import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex2 import Ui_MainWindow

class parImpar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.parOuImpar)

    def parOuImpar(self):
        try:
            num = int(self.ui.num.text())
            
            if(num % 2) == 0:
                self.ui.result.setText("Par")
            else:
                self.ui.result.setText("Ímpar")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = parImpar()
    janela.show()
    sys.exit(app.exec_())