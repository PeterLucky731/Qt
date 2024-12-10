import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex8 import Ui_MainWindow

class media(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.mediaCalc)

    def mediaCalc(self):
        try:
            num = int(self.ui.num.text())
            
            resultado = num ** 2
            
            self.ui.result.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = media()
    janela.show()
    sys.exit(app.exec_())