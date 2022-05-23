class Player():
    def __init__(self, numJogador, saldo, voltas):
        self.numJogador = numJogador;
        self.saldo = saldo;
        self.voltas = voltas;

    def compra(self, valorProp):
        self.saldo = self.saldo - valorProp;

    def pagarAluguel(self, valorAluguel):
        self.saldo = self.saldo - valorAluguel;

    def receberAluguel(self, valorAluguel):
        self.saldo = self.saldo + valorAluguel