import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex11 import Ui_MainWindow

class baseExpo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.expoBase)

    def expoBase(self):
        try:
            base = int(self.ui.base.text())
            expo = int(self.ui.expo.text())

            resultado = base ** expo

            self.ui.result.setText(f"{base} elevado a {expo} = {resultado}")
            
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = baseExpo()
    janela.show()
    sys.exit(app.exec_())