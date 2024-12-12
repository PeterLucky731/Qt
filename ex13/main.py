import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex13 import Ui_MainWindow

class entre10_20(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.entreDezeVinte)

    def entreDezeVinte(self):
        try:
            num = int(self.ui.num.text())
            if 10 <= num <= 20:
                self.ui.result.setText("O número está entre 10 e 20.")
            else:
                self.ui.result.setText("O número não está entre 10 e 20.")

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = entre10_20()
    janela.show()
    sys.exit(app.exec_())