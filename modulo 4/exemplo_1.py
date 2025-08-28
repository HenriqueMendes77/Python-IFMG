from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
# Cria uma aplicação com a bibliteca Qt
app = QApplication([])
# Cria uma janela principal
win = QMainWindow()
# Definie posição (0, 0) e dimensões da janela (500x300)
win.setGeometry(0, 0, 500, 300)
# Definie o título da janela
win.setWindowTitle('Exemplo com Qt')
# Cria um componente de rótulo
label = QtWidgets.QLabel(win)
inp = QtWidgets.QPushButton(win)
# Define o texto do componente
label.setText('Olá, Mundo!')
# Posiciona o componente na posição 100, 100
label.move(100, 100)
inp.move(100, 50)
# Mostra a janela
win.show()
# Executa a aplicação
app.exec_()