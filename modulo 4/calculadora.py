#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


# Classe herdando de QMainWindow
class CalculadoraUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Carrega o arquivo ui com a interface
        uic.loadUi('calculadora.ui', self)
        # Conecta clique do botão com o método calcula
        self.button_calc.clicked.connect(self.calcula)

    def calcula(self):
        # Obtém números digitados
        n1 = float(self.edit_n1.text())
        n2 = float(self.edit_n2.text())
        # Obtém operação selecionada
        op = self.combo_op.currentText()
        # Calcula de acordo com a operação
        if op == '+':
            res = n1 + n2
        elif op == '-':
            res = n1 - n2
        elif op == '*':
            res = n1 * n2
        elif op == '/':
            res = n1 / n2
        else:
            res = n1 ** n2
        # Mostra o resultado
        self.edit_res.setText(str(res))


if __name__ == '__main__':
    # Cria aplicação e a janela
    app = QApplication([])
    window = CalculadoraUI()
    # Exibe janela e executa a aplicação
    window.show()
    app.exec_()
