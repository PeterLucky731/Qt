import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from ex19 import Ui_MainWindow

class media(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.mediaCalc)

    def mediaCalc(self):
        try:
            qnt = int(self.ui.qnt.text())
            if qnt <= 0:
                QMessageBox.warning(self, "Erro", "A quantidade de números deve ser maior que zero.")
                return

            soma = 0

            for i in range(qnt):
                num, ok = QInputDialog.getInt(self, "Entrada de Número", f"Digite o número {i + 1}:")
                if not ok:
                    QMessageBox.warning(self, "Aviso", "Operação cancelada.")
                    return
                soma += num

            med = soma / qnt
            self.ui.result.setText(f'A média é {med:.2f}')

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = media()
    janela.show()
    sys.exit(app.exec_())