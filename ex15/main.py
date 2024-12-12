import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer
from ex15 import Ui_MainWindow


class contagemRegressiva(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.iniciar_contagem)
        self.contagem_atual = 10
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_contagem)

    def iniciar_contagem(self):
        self.timer.start(1000)  

    def atualizar_contagem(self):
        if self.contagem_atual > 0:
            self.ui.result.setText(str(self.contagem_atual))
            self.contagem_atual -= 1
        else:
            self.ui.result.setText("FIM")
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = contagemRegressiva()
    janela.show()
    sys.exit(app.exec_())