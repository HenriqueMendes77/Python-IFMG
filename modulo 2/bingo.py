import random
import os

class Jogador:
    def __init__(self, nome):
        self._nome = nome
        self.numeros = set()
        self.marcados = set()
    
    @property
    def nome(self):
        return self._nome
    
    def marca(self, numero):
        if numero in self.numeros:
            self.marcados.add(numero)
    
    def faltantes(self):
        return self.numeros - self.marcados
    
    def imprime(self):
        print(f"\nJogador: {self.nome}")
        print(f"Números faltantes: {sorted(self.faltantes())}")

class Bingo:
    def __init__(self, numeros_total):
        self.numeros = list(range(1, numeros_total + 1))
        random.shuffle(self.numeros)
        self.sorteados = []
        self.jogadores = []
        self.vencedores = []

    def adiciona_jogador(self, nome):
        copia = self.numeros[:]
        random.shuffle(copia)
        numeros_jogador = set(copia[:int(len(copia) * 0.3)])
        jogador = Jogador(nome)
        jogador.numeros = numeros_jogador
        self.jogadores.append(jogador)

    def imprime(self):
        print(f"\nNúmeros sorteados: {sorted(self.sorteados)}")
        for jogador in self.jogadores:
            jogador.imprime()

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def sorteia(self):
        numero = self.numeros.pop()
        self.sorteados.append(numero)

        for jogador in self.jogadores:
            jogador.marca(numero)
            if not jogador.faltantes() and jogador not in self.vencedores:
                self.vencedores.append(jogador)

    def jogar(self):
        if not self.jogadores:
            print("Nenhum jogador cadastrado!")
            return

        while not self.vencedores:
            self.imprime()
            input("\n\nPressione ENTER para sortear...")
            self.limpar_tela()
            self.sorteia()

        print("\n==== VENCEDOR ====")
        for vencedor in self.vencedores:
            print(f"- {vencedor.nome}")
        input("\nPressione ENTER para fechar...")

    def menu(self):
        self.limpar_tela()

        while True:
            nome = input(f"Jogador {len(self.jogadores)+1} (ENTER para parar): ")
            if nome == "":
                break
            self.adiciona_jogador(nome)

        if not self.jogadores:
            print("Nenhum jogador foi adicionado!")
            input("Pressione ENTER...")
            self.menu()
            

        self.limpar_tela()
        self.jogar()

if __name__ == "__main__":
    bingo = Bingo(50)
    bingo.menu()
