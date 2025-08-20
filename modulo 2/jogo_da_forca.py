import os

class Palavra:

    def __init__(self, palavra, dica):
        self._palavra = palavra
        self._dica = dica if dica else ""
        self._tela = ["_"] * len(self._palavra)

    @property
    def tela(self):
        print("\nDica: "+self._dica)
        print("-"*20)
        print(" ".join(self._tela))
    
    @property
    def completada(self):
        return "_" not in self._tela
    
    def tem_letra(self, letra):
        index = self._palavra.find(letra)
        if index != -1:
            self._tela[index] = letra
            return True
        else:
            return False

    @classmethod    
    def validar_palavra(self, palavra):
        if not palavra.isalpha():
            return False
        if not palavra.isascii():
            return False
        return True
    
class Forca:

    def __init__(self, palavra):
        self._palavra = palavra
        self._erros = 0
        self._digitadas = []

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar(self):
        self.limpar_tela()
        print("Tentativas: ", "-".join(self._digitadas))
        print("Erros: ", self._erros)
        self._palavra.tela

    def eh_letra_valida(self, letra):
        return len(letra) == 1 and not letra in self._digitadas and letra >= 'A' or letra <= 'Z'

    def jogar(self):
        while True:
            self.mostrar()
            letra = input("\nletra: ")
            if self.eh_letra_valida(letra):
                self._digitadas.append(letra)
                if not self._palavra.tem_letra(letra):
                    self._erros += 1

            if self._erros == 5:
                self.mostrar()
                print("\nVoce perdeu!")
                break
            
            if self._palavra.completada:
                self.mostrar()
                print("\nVoce ganhou!")
                break

if __name__ == "__main__":
    palavra = input("Palavra: ")
    dica = input("Dica: ")

    p1 = Palavra(palavra, dica)

    if p1.validar_palavra(palavra):
        forca = Forca(p1)
        forca.jogar()