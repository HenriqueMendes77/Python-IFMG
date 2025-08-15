class Cliente:

    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco


class ClientePF(Cliente):

    def __init__(self, nome, endereco, cpf, nascimento):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self._nascimento = nascimento

    def imprime(self):
        print(self._nome, '\nCPF:' + self._cpf,
              '\nNascimento: ' + self._nascimento)


class ClientePJ(Cliente):

    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self._cnpj = cnpj

    def imprime(self):
        print(self._nome, '\nCNPJ: ' + self._cnpj)



class Conta:
    quant = 0

    @classmethod
    def adiciona_conta(cls):
        cls.quant += 1

    @classmethod
    def quantidade(cls):
        return cls.quant

    def __init__(self, numero, cliente):
        self.adiciona_conta()
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0

    def depositar(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False

    def imprime(self):
        print('Conta:', str(self._numero),
              '\nSaldo: ', str(self._saldo))
        self._cliente.imprime()

class ContaInvestimento(Conta):
    
    def depositar(self, valor):
        self._saldo += valor * 1.01

