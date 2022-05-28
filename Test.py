import pytest
import Player
import Dice
import Board

print("Executando os principais métodos, que são responsáveis por boa parte do funcionamento do game.\nNão aplicarei aqui os métodos grandes, do tipo, rodar um round, pois ocuparia tempo demais.")
dice = object
jogador_teste = object
gameArea = object

class TestCase():
    
    def criarVariavel(self):
        self.gameArea = gameArea;
        self.dice = dice;
        self.jogador_teste = jogador_teste; 
        
        print("\ncriaTabuleiro OK\n")


    def criarTabuleiro(self):
        
        self.gameArea = Board.Board([], 0, [], [], []);
        self.gameArea.setPropriedades();

        print("\ncriaTabuleiro OK\n")

    def criarDado (self):
        self.dice = Dice.Dice(0, []);    
        self.dice.setDice();
        print("Os lados do dado:\n{}\n".format(self.dice.arrayNum) );

        print("\ncriarDado OK\n")


    def rolarDice(self):
        self.dice.rollDice()

        print("\nrolarDice OK")

    def criaJogador(self):
        self.jogador_teste = Player.Player(1, 300, 0, 0, 0)
        print("Jogador criado:\nNumero: {}\nSaldo: {}\nVoltas: {}\nVitorias: {}\nCasas Andadas: {}\n".format(self.jogador_teste.numJogador, self.jogador_teste.saldo, self.jogador_teste.voltas, self.jogador_teste.vitorias, self.jogador_teste.casasAndadas))

        print("\ncriaJogador OK\n")

    def compraCasa(self,casa):
        self.gameArea.arr_casas[casa] = 2;
        self.gameArea.arr_comprados[casa] = self.jogador_teste.numJogador;
        
        price = self.gameArea.arr_valor_casa[casa]
        self.jogador_teste.compra(price);
        print("\ncompraCasa OK\n")

    def pagaAluguel(self,casa):
        if self.gameArea.arr_comprados[casa] == 1:
            price = self.gameArea.arr_valor_aluguel[casa]
            self.jogador_teste.pagarAluguel(price);
        print("\npagaAluguel OK\n") 

    def aumentaVitoria(self, vitorias):
        self.jogador_teste.addVitorias(vitorias);
        print("\naumentaVitoria OK\n")

    def aumentaVolta(self, voltas):
        self.jogador_teste.addVoltas(voltas, self.jogador_teste);
        print("\naumentaVolta OK\n")
        
    def main(self):
        self.criarVariavel()
        self.criarTabuleiro()
        self.criarDado()
        self.rolarDice()
        self.criaJogador()
        self.compraCasa(2)
        self.pagaAluguel(2)
        self.aumentaVitoria(1)
        self.aumentaVolta(2)

def main():
    foo = TestCase()

if __name__ == "__main__":
    main()
