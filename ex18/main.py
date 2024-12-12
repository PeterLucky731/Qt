import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex18 import Ui_MainWindow

class maiorEntreDez(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.maior)

    def maior(self):
        try:
            num = int(self.ui.num.text())
            num2 = int(self.ui.num2.text())
            num3 = int(self.ui.num3.text())
            num4 = int(self.ui.num4.text())
            num5 = int(self.ui.num5.text())
            num6 = int(self.ui.num6.text())
            num7 = int(self.ui.num7.text())
            num8 = int(self.ui.num8.text())
            num9 = int(self.ui.num9.text())
            num10 = int(self.ui.num10.text())

            maior_num = max(num, num2, num3, num4, num5, num6, num7, num8, num9, num10)

            self.ui.result.setText(f'O maior número é: {maior_num}')
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = maiorEntreDez()
    janela.show()
    sys.exit(app.exec_())