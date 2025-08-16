from datetime import datetime

class Transacao:
    def __init__(self, descricao, valor, categoria, data, tipo):
        self.descricao = descricao
        self.valor = float(valor)
        self.categoria = categoria
        self.data = data
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo.capitalize()}: {self.descricao} | {self.categoria} | R${self.valor:.2f}"

class Gerenciador:

    def __init__(self):
        self.todas_transacoes = []

    def registrar_transacao(self, transacao):
        self.todas_transacoes.append(transacao)
    
    def listar_transacoes(self):
        if not self.todas_transacoes:
            print("Nenhuma transação registrada.")
        for t in self.todas_transacoes:
            print(t)
    
    def calcular_saldo(self):
        saldo = 0
        for t in self.todas_transacoes:
            if t.tipo == "receita":
                saldo += t.valor
            elif t.tipo == "despesa":
                saldo -= t.valor
        print(f"Saldo atual: R${saldo:.2f}")

    def menu(self):
        while True:
            print("\n--- Gerenciador de Finanças ---")
            print("1. Adicionar Receita")
            print("2. Adicionar Despesa")
            print("3. Listar Transações")
            print("4. Ver Saldo")
            print("5. Sair")
        
            try:
                escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha == 1:
                descricao = input("Descrição: ")
                valor = input("Valor: ")
                categoria = input("Categoria: ")
                transacao = Transacao(descricao, valor, categoria, datetime.now(), "receita")
                self.registrar_transacao(transacao)
            elif escolha == 2:
                descricao = input("Descrição: ")
                valor = input("Valor: ")
                categoria = input("Categoria: ")
                transacao = Transacao(descricao, valor, categoria, datetime.now(), "despesa")
                self.registrar_transacao(transacao)
            elif escolha == 3:
                self.listar_transacoes()
            elif escolha == 4:
                self.calcular_saldo()
            elif escolha == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    g = Gerenciador()
    g.menu()
