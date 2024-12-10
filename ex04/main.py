import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex4 import Ui_MainWindow

class fibo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.fiboSeq)

    def fiboSeq(self):
        
        try:
            num = int(self.ui.num.text())
            if num < 0:
                QMessageBox.warning(self, "Erro", "Apenas números positivos")
            else:
                fib_sequence = [0, 1]
                while len(fib_sequence) < num:
                    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
                self.ui.result.setText(str(fib_sequence))

        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = fibo()
    janela.show()
    sys.exit(app.exec_())