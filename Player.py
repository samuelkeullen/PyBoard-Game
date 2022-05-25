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
        self.saldo = self.saldo + valorAluguel;

    def addVoltas(self, volta, jogador):
        self.voltas = self.voltas + volta;
        print("O jogador {} completou uma volta, seu saldo aumentou em 100.".format(jogador.numJogador) );
        self.saldo = self.saldo + 100;

    def contaCasas(self, board, casaAtual, jogador):
        
        if board.arr_casas[casaAtual] == board.arr_casas[60] or board.arr_casas[casaAtual] > board.arr_casas[60]:
            self.addVoltas(1);
            print("O jogador {} completou uma volta, seu saldo aumentou em 100.".format(jogador.numJogador) );
            self.saldo = self.saldo + 100;