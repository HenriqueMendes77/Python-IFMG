class Produto:

    def __init__(self, nome, descricao, preco):
        self._nome = nome
        self._descricao = descricao
        self._preco = preco

    def __str__(self):
        return f"{self._nome} - {self._descricao} (${self._preco:0.2f})"


class ProdutoEstoque(Produto):

    def __init__(self, nome, descricao, preco):
        super().__init__(nome, descricao, preco)
        self._estoque = 0.0

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    def entrada(self, quantidade):
        self._estoque += quantidade

    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False

    def __str__(self):
        return f"{super().__str__()}, Estoque: {self._estoque:0.3f}"


class ProdutoVenda(Produto):

    def __init__(self, nome, descricao, preco, quantidade):
        super().__init__(nome, descricao, preco)
        self._quantidade = quantidade

    @property
    def total(self):
        return self._quantidade * self._preco

    def __str__(self):
        return f"{super().__str__()}, Qtde: {self._quantidade:0.3f}, Total: ${self.total:0.2f}"


class Venda:

    def __init__(self):
        self._produtos = []
        self._total = 0.0

    @property
    def total(self):
        return self._total

    @property
    def numero_produtos(self):
        return len(self._produtos)

    def adiciona_produto(self, produto):
        self._produtos.append(produto)
        self._total += produto.total

    def __str__(self):
        texto = "\n" + "-" * 50
        texto += "\nProdutos:"
        for produto in self._produtos:
            texto += "\n" + str(produto)
        texto += "\n" + "-" * 50
        texto += f"\nTotal da venda: ${self._total:0.2f}"
        texto += "\n" + "-" * 50
        return texto


def pergunta(mensagem, tipo=int):
    while True:
        try:
            resp = input(mensagem)
            return tipo(resp)
        except ValueError:
            print("Valor inválido! Informe novamente.")


def confirma(mensagem, resposta):
    texto = input(mensagem).strip()
    return texto.lower() == resposta.lower()


class Caixa:

    def __init__(self):
        self._produtos = {}
        self._vendas = []
        self._codigo_atual = 1  # Código incremental

    @classmethod
    def menu(cls):
        print()
        print("********************************")
        print("* CAIXA *")
        print("********************************")
        print("(C) Cadastrar/atualizar produto ")
        print("(E) Entrada de estoque ")
        print("(V) Vender ")
        print("(R) Relatório de vendas ")
        print("(S) Sair ")
        print("********************************")
        escolha = input("Informe sua opção: ").upper()
        return escolha

    def busca_produto(self):
        if len(self._produtos) == 0:
            print("Nenhum produto cadastrado!")
            return None
        print("\nProdutos:")
        for cod, produto in self._produtos.items():
            print(cod, ":", produto)
        codigo = pergunta("Código do produto: ")
        if codigo in self._produtos:
            return self._produtos[codigo]
        print("Produto não encontrado!")
        return None

    @classmethod
    def dados_produto(cls):
        print("\nInforme os dados")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = pergunta("Preço: ", float)
        return nome, descricao, preco

    def cadastro_produto(self):
        produto = self.busca_produto()
        if produto is not None:
            print("Produto cadastrado:", produto)
            if confirma("Alterar? (S/N) ", "S"):
                nome, descricao, preco = self.dados_produto()
                produto._nome = nome
                produto.descricao = descricao
                produto.preco = preco
        else:
            if confirma("Incluir? (S/N) ", "S"):
                nome, descricao, preco = self.dados_produto()
                produto = ProdutoEstoque(nome, descricao, preco)
                self._produtos[self._codigo_atual] = produto
                self._codigo_atual += 1

    def entrada_estoque(self):
        produto = self.busca_produto()
        if produto is not None:
            quantidade = pergunta('Quantidade de entrada: ', float)
            produto.entrada(quantidade)

    def venda(self):
        print('Venda')
        venda = Venda()
        while True:
            produto = self.busca_produto()
            if produto is not None:
                quantidade = pergunta('Quantidade vendida: ', float)
                if produto.saida(quantidade):
                    produto_venda = ProdutoVenda(
                        produto._nome,
                        produto.descricao,
                        produto.preco,
                        quantidade
                    )
                    venda.adiciona_produto(produto_venda)
                print(venda)
            if confirma('Adicionar mais produtos? (S/N) ', 'N'):
                break
        if venda.numero_produtos > 0:
            self._vendas.append(venda)

    def relatorio_vendas(self):
        if len(self._vendas) == 0:
            print('Nenhuma venda encontrada!')
            return
        total_geral = 0
        for cont, venda in enumerate(self._vendas):
            print('\nVenda', cont + 1)
            print(venda)
            total_geral += venda.total
        print('TOTAL GERAL:', total_geral)
        input('Pressione ENTER para voltar')

    def iniciar(self):
        while True:
            escolha = self.menu()
            if escolha == 'C':
                self.cadastro_produto()
            elif escolha == 'E':
                self.entrada_estoque()
            elif escolha == 'V':
                self.venda()
            elif escolha == 'R':
                self.relatorio_vendas()
            elif escolha == 'S':
                break


if __name__ == '__main__':
    Caixa().iniciar()
