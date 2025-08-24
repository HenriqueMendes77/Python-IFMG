#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv                     # Módulo para ler e escrever arquivos CSV
from os.path import isfile     # Função para verificar se o arquivo existe

# Função utilitária
def linha():
    print('-' * 50)            # Imprime uma linha separadora na tela

# =========================================
# Classe Contato
# =========================================
class Contato:
    # Campos fixos de cada contato
    campos = ['Nome', 'Telefone', 'Aniversário']

    def __init__(self, valores):
        self._dic = {}         # Guarda os campos em um dicionário
        # Associa cada campo ao valor correspondente
        for cont, campo in enumerate(self.campos):
            self._dic[campo] = valores[cont]

    def alterar(self):
        linha()
        print('Alteração de contato')
        linha()
        # Percorre cada campo e permite editar
        for campo, valor in self._dic.items():
            print(campo + ' (' + valor + ')')
            novo_valor = input('Novo valor: ').strip()
            if novo_valor != '':
                self._dic[campo] = novo_valor  # Atualiza se não estiver vazio

    @property
    def valores(self):
        # Retorna os valores como lista (para salvar em CSV)
        lista_valores = []
        for campo in self.campos:
            lista_valores.append(self._dic[campo])
        return lista_valores

    def __str__(self):
        # Exibe o contato formatado: Campo: Valor
        lista_cv = [campo + ': ' + self._dic[campo] for campo in self._dic]
        return '\n'.join(lista_cv)

    def __lt__(self, other):
        # Permite comparar e ordenar contatos
        return tuple(self.valores) < tuple(other.valores)

    @classmethod
    def novo(cls):
        linha()
        print('Novo contato')
        linha()
        lista_valores = []
        # Pede cada campo ao usuário
        for campo in cls.campos:
            valor = input(campo + ': ').strip()
            lista_valores.append(valor)
        # Nome não pode ser vazio
        if len(lista_valores[0]) == 0:
            print('Contato inválido, o nome é obrigatório!')
            return None
        else:
            return Contato(lista_valores)

# =========================================
# Classe Arquivo (manipula CSV)
# =========================================
class Arquivo:
    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo
        self._lista_contatos = []
        # Se o arquivo já existir, lê os contatos
        if isfile(self._nome_arquivo):
            with open(self._nome_arquivo) as arq:
                leitor = csv.reader(arq)
                next(leitor)  # Ignora cabeçalho
                for linha_csv in leitor:
                    contato = Contato(linha_csv)
                    self._lista_contatos.append(contato)

    def listar(self):
        # Lista todos os contatos cadastrados
        if len(self._lista_contatos) == 0:
            print('Nenhum contato cadastrado!')
            linha()
        else:
            self._lista_contatos.sort()
            for cont, contato in enumerate(self._lista_contatos):
                print('Código:', cont)  # Código é o índice do contato
                print(str(contato))    # Mostra dados do contato
                linha()

    def buscar(self, codigo):
        # Busca contato pelo índice
        if 0 <= codigo < len(self._lista_contatos):
            return self._lista_contatos[codigo]
        return None

    def incluir(self):
        # Cria um novo contato e adiciona à lista
        contato = Contato.novo()
        if contato is not None:
            self._lista_contatos.append(contato)

    def excluir(self, codigo):
        # Remove contato pelo índice
        if 0 <= codigo < len(self._lista_contatos):
            self._lista_contatos.pop(codigo)

    def salvar(self):
        # Salva todos os contatos no arquivo CSV
        with open(self._nome_arquivo, 'w', newline='') as arq:
            escritor = csv.writer(arq)
            escritor.writerow(Contato.campos)  # Cabeçalho
            for contato in self._lista_contatos:
                escritor.writerow(contato.valores)

# =========================================
# Classe Agenda (interação com usuário)
# =========================================
class Agenda:
    def __init__(self, nome_arquivo):
        self._arq = Arquivo(nome_arquivo)  # Usa a classe Arquivo

    def menu(self):
        linha()
        print('Agenda de contatos')
        linha()
        self._arq.listar()  # Mostra contatos já salvos
        # Mostra opções
        print('(I)ncluir | (E)xcluir | (A)lterar | (S)alvar | Sai(r)')
        return input('Informe a opção desejada: ').strip().lower()

    def executar(self):
        # Loop principal da agenda
        while True:
            resp = self.menu()
            if resp == 'i':   # Incluir contato
                self._arq.incluir()
            elif resp == 'e': # Excluir contato
                codigo = int(input('Código do contato: '))
                self._arq.excluir(codigo)
            elif resp == 'a': # Alterar contato
                codigo = int(input('Código do contato: '))
                contato = self._arq.buscar(codigo)
                if contato is not None:
                    contato.alterar()
            elif resp == 's': # Salvar no CSV
                self._arq.salvar()
            elif resp == 'r': # Sair
                break

# =========================================
# Execução
# =========================================
if __name__ == '__main__':
    agenda = Agenda('contatos.csv')  # Nome do arquivo CSV
    agenda.executar()                # Inicia a agenda
