import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex9 import Ui_MainWindow

class tabuada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.tabuadaQt)

    def tabuadaQt(self):
        try:
            num = int(self.ui.num.text())
            
            
            self.ui.result.setText(f" {num} x 1: {num*1}\n {num} x 2: {num*2}\n {num} x 3: {num*3}\n {num} x 4: {num*4}\n {num} x 5: {num*5}\n {num} x 6: {num*6}\n {num} x 7: {num*7}\n {num} x 8: {num*8}\n {num} x 9: {num*9}\n {num} x 10: {num*10}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = tabuada()
    janela.show()
    sys.exit(app.exec_())