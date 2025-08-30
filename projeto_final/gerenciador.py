from datetime import datetime
import os
import csv
from os.path import isfile
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QMessageBox
)
from PyQt5 import uic

class Transacao:
    def __init__(self, codigo, descricao, valor, categoria, data, tipo):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = float(valor)
        self.categoria = categoria
        self.data = data
        self.tipo = tipo

    def __str__(self):
        return f"{self.codigo} - {self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo.capitalize()}: {self.descricao} | {self.categoria} | R${self.valor:.2f}"


class Arquivo:
    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo
        self.transacoes = []

        if isfile(self._nome_arquivo):
            with open(self._nome_arquivo, encoding="utf-8") as arq:
                leitor = csv.reader(arq)
                next(leitor, None)
                for linha in leitor:
                    codigo = int(linha[0])
                    data = datetime.strptime(linha[1], "%d/%m/%Y %H:%M:%S")
                    tipo = linha[2]
                    descricao = linha[3]
                    categoria = linha[4]
                    valor = float(linha[5])
                    self.transacoes.append(
                        Transacao(codigo, descricao, valor, categoria, data, tipo)
                    )

    def salvar(self):
        with open(self._nome_arquivo, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            escritor.writerow(["Código", "Data", "Tipo", "Descrição", "Categoria", "Valor"])
            for t in self.transacoes:
                escritor.writerow(
                    [
                        t.codigo,
                        t.data.strftime("%d/%m/%Y %H:%M:%S"),
                        t.tipo,
                        t.descricao,
                        t.categoria,
                        f"{t.valor:.2f}"
                    ]
                )

    def excluir(self, codigo):
        for i, t in enumerate(self.transacoes):
            if t.codigo == codigo:
                self.transacoes.pop(i)
                return True
        return False


class GerenciadorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gerenciador.ui', self)
        self.arquivo = Arquivo("transacoes.csv")
        self.atualizar_tabela()
        self.calcular_saldo_ui()

        # Conectar botões
        self.btnAdicionar.clicked.connect(self.adicionar_transacao)
        self.btnExcluir.clicked.connect(self.excluir_transacao)
        self.btnSalvar.clicked.connect(self.salvar_transacoes)

    def atualizar_tabela(self):
        self.tabelaTransacoes.setRowCount(len(self.arquivo.transacoes))
        for row, t in enumerate(self.arquivo.transacoes):
            self.tabelaTransacoes.setItem(row, 0, QTableWidgetItem(str(t.codigo)))
            self.tabelaTransacoes.setItem(row, 1, QTableWidgetItem(t.data.strftime("%d/%m/%Y %H:%M:%S")))
            self.tabelaTransacoes.setItem(row, 2, QTableWidgetItem(t.tipo))
            self.tabelaTransacoes.setItem(row, 3, QTableWidgetItem(t.descricao))
            self.tabelaTransacoes.setItem(row, 4, QTableWidgetItem(t.categoria))
            self.tabelaTransacoes.setItem(row, 5, QTableWidgetItem(f"{t.valor:.2f}"))

        self.tabelaTransacoes.resizeColumnsToContents()

    def adicionar_transacao(self):
        codigo = (self.arquivo.transacoes[-1].codigo + 1) if self.arquivo.transacoes else 1
        tipo = self.comboTipo.currentText().lower()
        descricao = self.inputDescricao.text()
        categoria = self.inputCategoria.text()
        valor_texto = self.inputValor.text()
        try:
            valor = float(valor_texto)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Valor inválido!")
            return

        transacao = Transacao(codigo, descricao, valor, categoria, datetime.now(), tipo)
        self.arquivo.transacoes.append(transacao)
        self.atualizar_tabela()
        self.calcular_saldo_ui()
        self.limpar_campos()

    def excluir_transacao(self):
        codigo_texto = self.inputCodigoExcluir.text()
        try:
            codigo = int(codigo_texto)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Código inválido!")
            return

        if self.arquivo.excluir(codigo):
            QMessageBox.information(self, "Sucesso", f"Transação {codigo} excluída!")
            self.atualizar_tabela()
            self.calcular_saldo_ui()
        else:
            QMessageBox.warning(self, "Erro", f"Transação {codigo} não encontrada!")

    def salvar_transacoes(self):
        self.arquivo.salvar()
        QMessageBox.information(self, "Sucesso", "Transações salvas com sucesso!")

    def calcular_saldo_ui(self):
        saldo = sum(t.valor if t.tipo == "receita" else -t.valor for t in self.arquivo.transacoes)
        self.labelSaldoValor.setText(f"R$ {saldo:.2f}")


    def limpar_campos(self):
        self.inputDescricao.clear()
        self.inputCategoria.clear()
        self.inputValor.clear()
        self.comboTipo.setCurrentIndex(0)
        self.inputCodigoExcluir.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = GerenciadorUI()
    window.show()
    app.exec_()
