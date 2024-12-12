import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex12 import Ui_MainWindow

class maiorNum(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.maiorEntreOs3)

    def maiorEntreOs3(self):
        try:
            num = float(self.ui.num.text())
            num2 = float(self.ui.num2.text())
            num3 = float(self.ui.num3.text())
         
            maior = max(num, num2, num3)
            self.ui.result.setText(f"O maior número é: {maior}")
            
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = maiorNum()
    janela.show()
    sys.exit(app.exec_())