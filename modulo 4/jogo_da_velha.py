from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class JogoDaVelhaUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('jogo_da_velha.ui', self)

        self._simbolo = "X"
        self._tabuleiro = [["", "", ""],["", "", ""],["", "", ""]]
        
        for i in range(0, 9):
            btn = getattr(self, f"btn_{i}", None)
            btn.clicked.connect(lambda checked, b=btn, i=i: self.preenche(b, i))

        self.btn_novo_jogo.clicked.connect(self.reset)

    def preenche(self, btn, i):
        if btn.text() != "":
            return
        btn.setText(self._simbolo)
        self._tabuleiro[i // 3][i % 3] = self._simbolo
        if self.verifica_ganhador():
            for j in range(0, 9):
                btn = getattr(self, f"btn_{j}", None)
                btn.setEnabled(False)

    def reset(self):
        self.mensagem.setText(f"Vez do jogador: {self._simbolo}")
        self._tabuleiro = [["", "", ""],["", "", ""],["", "", ""]]
        for i in range(0, 9):
            btn = getattr(self, f"btn_{i}", None)
            btn.setText("")
            btn.setEnabled(True)

    def verifica_ganhador(self):
        for i in range(3):
            if self._tabuleiro[i][0] == self._tabuleiro[i][1] == self._tabuleiro[i][2] != "":
                self.mensagem.setText(f"Jogador {self._simbolo} ganhou!")
                return True
            if self._tabuleiro[0][i] == self._tabuleiro[1][i] == self._tabuleiro[2][i] != "":
                self.mensagem.setText(f"Jogador {self._simbolo} ganhou!")
                return True
        if self._tabuleiro[0][0] == self._tabuleiro[1][1] == self._tabuleiro[2][2] != "":
            self.mensagem.setText(f"Jogador {self._simbolo} ganhou!")
            return True
        elif self._tabuleiro[0][2] == self._tabuleiro[1][1] == self._tabuleiro[2][0] != "":
            self.mensagem.setText(f"Jogador {self._simbolo} ganhou!")
            return True
        elif all(cell != "" for row in self._tabuleiro for cell in row):
            self.mensagem.setText("Empate!")
            return True
        else:
            self._simbolo = "O" if self._simbolo == "X" else "X"
            self.mensagem.setText(f"Vez do jogador: {self._simbolo}")
            return False

if __name__ == '__main__':
    app = QApplication([])
    window = JogoDaVelhaUI()
    window.show()
    app.exec_()
