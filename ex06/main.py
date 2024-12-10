import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex6 import Ui_MainWindow

class qntVogais(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn.clicked.connect(self.vogais)

    def vogais(self):
        try:
            input = self.ui.input.text()
            if not input.isalpha():
                raise ValueError
            vogais = 'aeiou'
            qnt = sum(1 for char in input.lower() if char in vogais)
            self.ui.result.setText(f"A quantidade de vogais é: {qnt}")
        
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira somente letras")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = qntVogais()
    janela.show()
    sys.exit(app.exec_())