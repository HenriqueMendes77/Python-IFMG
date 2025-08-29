from datetime import datetime
import os
import csv
from os.path import isfile


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


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
                next(leitor)
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

    def listar_transacoes(self):
        if not self.transacoes:
            print("Nenhuma transação registrada.")
        else:
            for transacao in self.transacoes:
                print(transacao)

    def salvar(self, dados):
        with open(self._nome_arquivo, "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            escritor.writerow(["Código", "Data", "Tipo", "Descrição", "Categoria", "Valor"])
            for i, t in enumerate(dados):
                escritor.writerow(
                    [
                        i,
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
                print(f"Transação {codigo} excluída com sucesso.")
                return
        print(f"Transação {codigo} não encontrada.")



class Gerenciador:

    def __init__(self):
        self.arquivo = Arquivo("transacoes.csv")

    def pegar_dados(self):
        codigo = (self.arquivo.transacoes[-1].codigo if self.arquivo.transacoes else 0) + 1
        tipo = input("(+) Receita ou (-) Despesa: ")
        descricao = input("Descrição: ")
        valor = input("Valor: ")
        categoria = input("Categoria: ")
        transacao = Transacao(codigo, descricao, valor, categoria, datetime.now(), tipo)
        self.registrar_transacao(transacao)

    def registrar_transacao(self, transacao):
        self.arquivo.transacoes.append(transacao)

    def calcular_saldo(self):
        saldo = sum(t.valor if t.tipo == "receita" else -t.valor for t in self.arquivo.transacoes)
        print(f"Saldo atual: R${saldo:.2f}")

    def menu(self):
        print("=" * 50)
        print(" "*12,"Gerenciador Financeiro"," "*12)
        print("=" * 50)
        print("(1) - Adicionar Transação")
        print("(2) - Excluir Transação")
        print("(3) - Listar Transações")
        print("(4) - Ver Saldo")
        print("(5) - Salvar")
        print("(6) - Sair")
        print("=" * 50)

    def executar(self):
        while True:
            self.menu()

            try:
                escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha == 1:
                self.pegar_dados()
            elif escolha == 2:
                codigo = int(input("Código da transação a ser excluída: "))
                self.arquivo.excluir(codigo)
            elif escolha == 3:
                self.arquivo.listar_transacoes()
            elif escolha == 4:
                self.calcular_saldo()
            elif escolha == 5:
                self.arquivo.salvar(self.arquivo.transacoes)
            elif escolha == 6:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    g = Gerenciador()
    g.executar()
