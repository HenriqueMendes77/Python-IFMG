
import json
from os.path import isfile

PAI = "Pai"
MAE = "Mãe"


# Escreve linha na tela
def linha():
    print("-" * 50)


class Arvore:
    def __init__(self, nome_arquivo):
        # Arquivo e árvore de pessoas
        self._nome_arquivo = nome_arquivo
        self._arvore = {}
        # Checa se o arquivo existe
        if isfile(self._nome_arquivo):
            # Abre arquivo e lê usando JSON
            with open(self._nome_arquivo, encoding="utf-8") as arq:
                self._arvore = json.load(arq)

    def incluir(self, nome):
        # Verifica se o nome é válido
        if nome == "":
            print("Nome inválido!")
            input()
        elif nome in self._arvore:
            print("Pessoa já cadastrada ou nome inválido!")
            input()
        else:
            # Inclui nome na árvore (sem pai e mãe)
            self._arvore[nome] = {PAI: "", MAE: ""}

    def listar(self):
        # Testa se há pessoas na árvore
        if len(self._arvore) == 0:
            print("Nenhuma pessoa cadastrada!")
            linha()
        else:
            # Obtém e ordena lista de nomes
            lista_nomes = list(self._arvore.keys())
            lista_nomes.sort()
            # Para cada nome
            for nome in lista_nomes:
                # Obtém dados do nome
                dados = self._arvore[nome]
                # Cria lista de dados (campo: valor)
                lista_dados = []
                for campo, valor in dados.items():
                    if valor != "":
                        lista_dados.append(campo + ": " + str(valor))
                # Junta dados em str
                dados_str = ""
                if len(lista_dados) > 0:
                    dados_str = "(" + ", ".join(lista_dados) + ")"
                # Imprime nome e dados
                print(nome, dados_str)
            linha()

    def buscar(self, nome):
        # Verifica se nome existe e o retorna
        if nome in self._arvore:
            return self._arvore[nome]
        # Retorna '' se o nome não existir
        return ""

    def alterar_pais(self, nome):
        # Busca a pessoa na árvore
        pessoa = self.buscar(nome)
        if pessoa != "":
            # Obtém nome dos pais
            nome_pai = input("Pai: ").strip()
            nome_mae = input("Mãe: ").strip()
            # Altera nome dos pais (se existirem na árvore ou for '')
            if nome_pai in self._arvore or nome_pai == "":
                pessoa[PAI] = nome_pai
            if nome_mae in self._arvore or nome_mae == "":
                pessoa[MAE] = nome_mae

    def excluir(self, nome):
        # Busca a pessoa
        pessoa = self.buscar(nome)
        # Testa se a pessoa foi encontrada
        if pessoa != "":
            # Verifica se a pessoa é pai ou mãe de alguém
            for outro, dados in self._arvore.items():
                if dados[PAI] == nome:
                    print(nome, "é pai de", outro)
                    input()
                    return
                if dados[MAE] == nome:
                    print(nome, "é mãe de", outro)
                    input()
                    return
            self._arvore.pop(nome)

    def salvar(self):
        # Salva arquivo usando JSON
        with open(self._nome_arquivo, "w", encoding="utf-8") as arq:
            json.dump(self._arvore, arq, indent=2, ensure_ascii=False)

    def ancestrais(self, nome, nivel=0):
        # Busca pessoa
        pessoa = self.buscar(nome)
        if pessoa != "":
            # Imprime o nome da pessoa
            print(" " * nivel, nome, sep="")
            # Busca recursiva pelos ancestrais
            self.ancestrais(pessoa[PAI], nivel + 2)
            self.ancestrais(pessoa[MAE], nivel + 2)

    def menu(self):
        print("\n" * 5)
        linha()
        print("Árvore Genealógica")
        linha()
        self.listar()
        print("(+) | (-) | (P)ais | (A)ncestrais | (S)alvar | Sai(r)")
        return input("Informe a opção desejada: ").strip().lower()

    def executar(self):
        while True:
            resp = self.menu()
            if resp in ["-", "+", "p", "a", "d"]:
                nome = input("Informe o nome: ")
                if resp == "+":
                    self.incluir(nome)
                elif resp == "-":
                    self.excluir(nome)
                elif resp == "p":
                    self.alterar_pais(nome)
                elif resp == "a":
                    linha()
                    print("Árvore Genealógica:")
                    linha()
                    self.ancestrais(nome)
                    linha()
                    input()
                elif resp == "d":
                    print("Função de descendentes ainda não implementada!")
                    input()
            elif resp == "s":
                self.salvar()
            elif resp == "r":
                break


if __name__ == "__main__":
    arvore = Arvore("arvore.json")
    arvore.executar()
