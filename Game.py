import Board as Board
import Player as Player
import Dice as Dice
import time
import random

def loading():
    time.sleep(0.5);

def round(ordem_jogadores, dice, gameArea):
    count = 0

    while count < 4:
        loading();
        dado_sorteado = dice.rollDice();
        print("-------------------------------------------------------------------------------------------------");
        print("O jogador {} tirou o n° {}.".format(ordem_jogadores[count],dado_sorteado));

        go_ahead = 0 + dado_sorteado;

        if gameArea.arr_casas[go_ahead] == 0:
            print("\nO jogador {} caiu em uma casa sem propriedades para adquirir".format(ordem_jogadores[count]))
        elif gameArea.arr_casas[go_ahead] == 1:
            print("\nO jogador {} comprou a propriedade na casa: {}".format(ordem_jogadores[count], go_ahead))
        elif gameArea.arr_casas[go_ahead] == 2:
            print("\nO jogador {} caiu na casa {}, anteriormente comprada, deverá pagar aluguel.".format(ordem_jogadores[count], go_ahead))

        count+= 1
    print("-------------------------------------------------------------------------------------------------");
    


def main():
    print("Iniciando módulos...\n");
    loading();

    print("Gerando tabuleiro...\n");
    
    loading();
    #Criando objeto do tabuleiro...;
    gameArea = Board.Board([], 0, 0, []);
    
    loading();
    #definindo as propriedades...;
    gameArea.setPropriedades();

    loading();
    num_casas_tabuleiro = gameArea.arr_casas.count(0)+gameArea.arr_casas.count(1);
    
    print("Tabuleiro gerado!\n");

    loading();
    print("Informações do tabuleiro:\nN° de casas no tabuleiro: {}\nN° de propriedades:{}\nN° de propiedades compradas: {}\n".format(num_casas_tabuleiro,gameArea.n_propriedades, gameArea.n_prop_compradas));

    loading();
    loading();

    print("Conectando jogadores...\n");

    loading();

    print("Jogador 1 encontrado!\n");
    j1 = Player.Player(1, 300, 0);

    loading();
    print("Jogador 2 encontrado!\n");
    j2 = Player.Player(2, 300, 0);

    loading();
    print("Jogador 3 encontrado!\n");
    j3 = Player.Player(3, 300, 0);

    loading();
    print("Jogador 4 encontrado!\n");
    j4 = Player.Player(4, 300, 0);

    print("Exibindo informações dos jogadores:\n");
    print("-------------------------------------------------------------------------------------------------");
    print("Jogador {}:\nSaldo: {}\nN° de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas));
    print("-------------------------------------------------------------------------------------------------");
    print("Jogador {}:\nSaldo: {}\nN° de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas));
    print("-------------------------------------------------------------------------------------------------");
    print("Jogador {}:\nSaldo: {}\nN° de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas));
    print("-------------------------------------------------------------------------------------------------");
    print("Jogador {}:\nSaldo: {}\nN° de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas));
    print("-------------------------------------------------------------------------------------------------");

    loading();
    print("Gerando o dado...\n");

    #criando objeto do Dado;
    dice = Dice.Dice(0, []);

    #definindo dados do Dado;
    dice.setDice();

    loading();

    print("Os lados do dado:\n{}\n".format(dice.arrayNum));

    loading();

    print("Reordenando jogadores em uma ordem aleatória...\n");

    loading();

    array_numbers = [1, 2, 3, 4];
    array_players = list(array_numbers);
    random.shuffle(array_players)

    print("E a ordem de jogada dos jogadores será:\n{}".format(array_players));

    print("Iniciando partida...\n");

    loading();

    print("Rolando dados...\n");
    round(array_players, dice, gameArea);

    loading();


    




if __name__ == "__main__":
    main();