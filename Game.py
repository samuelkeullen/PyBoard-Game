import Board as Board
import Player as Player
import Dice as Dice
import time
import random
import datetime

log = open("log.txt", "w");


def loading():
    time.sleep(0.5);

def round(ordem_jogadores, dice, gameArea):
    count = 0

    while count < 4:
        loading();
        dado_sorteado = dice.rollDice();
        print("-------------------------------------------------------------------------------------------------", file=log);
        print("O jogador {} tirou o n {}.".format(ordem_jogadores[count],dado_sorteado), file=log);

        go_ahead = 0 + dado_sorteado;

        if gameArea.arr_casas[go_ahead] == 0:
            print("\nO jogador {} caiu em uma casa sem propriedades para adquirir".format(ordem_jogadores[count]), file=log)
        elif gameArea.arr_casas[go_ahead] == 1:
            print("\nO jogador {} comprou a propriedade na casa: {}".format(ordem_jogadores[count], go_ahead), file=log)
        elif gameArea.arr_casas[go_ahead] == 2:
            print("\nO jogador {} caiu na casa {}, anteriormente comprada, devera pagar aluguel.".format(ordem_jogadores[count], go_ahead), file=log)

        count+= 1
    print("-------------------------------------------------------------------------------------------------", file=log);
    


def main():

    print("Iniciando o jogo...")
    print("Por favor, veja o arquivo 'log.txt' caso queira rever o andamento do jogo.")

    #inicio = time.time()
    begin_time = datetime.datetime.now()

    print("Iniciando o jogo...", file=log)
    print("Por favor, veja o arquivo 'log.txt' caso queira rever o andamento do jogo.", file=log)
    
    print("Iniciando modulos...\n", file=log);
    loading();

    print("Gerando tabuleiro...\n", file=log);
    
    loading();
    #Criando objeto do tabuleiro...;
    gameArea = Board.Board([], 0, 0, []);
    
    loading();
    #definindo as propriedades...;
    gameArea.setPropriedades();

    loading();
    num_casas_tabuleiro = gameArea.arr_casas.count(0)+gameArea.arr_casas.count(1);
    
    print("Tabuleiro gerado!\n", file=log);

    loading();
    print("Informacoes do tabuleiro:\nN de casas no tabuleiro: {}\nN de propriedades:{}\nN de propiedades compradas: {}\n".format(num_casas_tabuleiro,gameArea.n_propriedades, gameArea.n_prop_compradas), file=log);

    loading();
    loading();

    print("Conectando jogadores...\n", file=log);

    loading();

    print("Jogador 1 encontrado!\n", file=log);
    j1 = Player.Player(1, 300, 0);

    loading();
    print("Jogador 2 encontrado!\n", file=log);
    j2 = Player.Player(2, 300, 0);

    loading();
    print("Jogador 3 encontrado!\n", file=log);
    j3 = Player.Player(3, 300, 0);

    loading();
    print("Jogador 4 encontrado!\n", file=log);
    j4 = Player.Player(4, 300, 0);

    print("Exibindo informacoes dos jogadores:\n", file=log);
    print("-------------------------------------------------------------------------------------------------", file=log);
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas), file=log);
    print("-------------------------------------------------------------------------------------------------", file=log);
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas), file=log);
    print("-------------------------------------------------------------------------------------------------", file=log);
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas), file=log);
    print("-------------------------------------------------------------------------------------------------", file=log);
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas), file=log);
    print("-------------------------------------------------------------------------------------------------", file=log);

    loading();
    print("Gerando o dado...\n", file=log);

    #criando objeto do Dado;
    dice = Dice.Dice(0, []);

    #definindo dados do Dado;
    dice.setDice();

    loading();

    print("Os lados do dado:\n{}\n".format(dice.arrayNum), file=log);

    loading();

    print("Reordenando jogadores em uma ordem aleatoria...\n", file=log);

    loading();

    array_numbers = [1, 2, 3, 4];
    array_players = list(array_numbers);
    random.shuffle(array_players)

    print("E a ordem de jogada dos jogadores sera:\n{}".format(array_players), file=log);

    print("Iniciando partida...\n", file=log);

    loading();

    print("Rolando dados...\n", file=log);
    round(array_players, dice, gameArea);

    loading();

    print("\n\nTempo decorrido(HH:MM:SS:MS):",file=log)
    print(datetime.datetime.now() - begin_time, file=log)

    print("\n\nTempo decorrido(HH:MM:SS:MS):")
    print(datetime.datetime.now() - begin_time)


if __name__ == "__main__":
    main();