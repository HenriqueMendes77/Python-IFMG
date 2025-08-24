import os
import json
from os.path import isfile

class Folha:

    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo
        self._funcionarios = []
        self._arquivo = {}

        if isfile(self._nome_arquivo):
            with open(self._nome_arquivo, encoding="utf-8") as arq:
                self._arquivo = json.load(arq)
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def pega_dados(self):
        nome = input("Nome: ")
        tempo = input("Tempo: ")
        dependentes = []
        print("Dependentes: (pressione ENTER para sair)")
        while True:
             d = input(">> ")
             if d == "":
                 break
             else:
                 dependentes.append(d)
        salario = self.calcula_salario(tempo, dependentes)
        return {"nome": nome, "tempo": tempo, "dependentes": dependentes, "salario": salario}
    
    @classmethod
    def calcula_salario(self, tempo, dependentes):
        return (2000 * float(tempo) * 0.01) + (len(dependentes) * 150)

    @classmethod
    def mostrar_funcionario(self, cpf, dados):
        print(f"CPF: {cpf}")
        for campo, valor in dados.items():
            print(f"{campo}: {valor}")            
        print("-"*60)

    def buscar(self, cpf):
        if cpf in self._arquivo:
            return self._arquivo[cpf]
        return ""

    def incluir(self, cpf):
        self.limpar_tela()
        if cpf == "":
            print("CPF inválido!")
        elif cpf in self._arquivo:
            print("Pessoa já cadastrada!")
        else:
            self._arquivo[cpf] = self.pega_dados()

    def alterar(self, cpf):
        self.limpar_tela()
        if cpf == "":
            print("CPF inválido!")
        else:
            dados = self.buscar(cpf)
            self.mostrar_funcionario(cpf, dados)
            self._arquivo[cpf] = self.pega_dados()
            self.mostrar_funcionario(cpf, dados)

    def excluir(self, cpf):
        self.limpar_tela()
        if cpf == "":
            print("CPF inválido!")
        else:
            dados = self.buscar(cpf)
            self.mostrar_funcionario(cpf, dados)
            confirma = input("excluir? [S/N] ").lower().strip()
            if confirma == "s":
                del self._arquivo[cpf]
                print("Cadastro removido!")
    
    def listar(self):
        print("="*60)
        print("     LISTA DE FUNCONARIOS")
        print("="*60)
        if len(self._arquivo) == 0:
            print("Nenhuma pessoa cadastrada!")
        else:
            lista_cpf = list(self._arquivo.keys())
            lista_cpf.sort()
            for cpf in lista_cpf:
                dados = self.buscar(cpf)
                self.mostrar_funcionario(cpf, dados)

    def salvar(self):
        with open(self._nome_arquivo, "w", encoding="utf-8") as arq:
            json.dump(self._arquivo, arq, ensure_ascii=False, indent=4)
        self.limpar_tela()
        print("Arquivo salvo")


    def menu(self):
        print("="*60)
        print("(1) Incluir | (2) Excluir | (3) Alterar | (4) Salvar | (5) Sair")
        print("="*60)
        return int(input(">>> "))

    def executar(self):
        while True:
            self.listar()
            opcao = self.menu()
            if opcao == 1:
                cpf = input("CPF: ")
                self.incluir(cpf)
            elif opcao == 2:
                cpf = input("CPF: ")
                self.excluir(cpf)
            elif opcao == 3:
                cpf = input("CPF: ")
                self.alterar(cpf)
            elif opcao == 4:
                self.salvar()
            elif opcao == 5:
                break
            else:
                print("\nOpção inválida")


if __name__ == "__main__":
    f = Folha("folha.json")
    f.executar()