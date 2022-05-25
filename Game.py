import Board as Board
import Player as Player
import Dice as Dice
import time
import random
import datetime
import sys

begin_time = datetime.datetime.now()

current_house = [];
current_player = [];
start_house = 1;
continuar = [0,0,0,0]

def getEndTime():
    print("\n\nTempo decorrido(HH:MM:SS:MS):" );
    print(datetime.datetime.now() - begin_time );

def encerrar():
    exit()

def loading():
    time.sleep(0.5);

def round(ordem_jogadores, dice, gameArea, j1, j2, j3, j4):
    count = 0
    go_ahead = 0;

    
    while count < 4:
        if ordem_jogadores[count] != -1:
            loading();
            dado_sorteado = dice.rollDice();
            
            print("-------------------------------------------------------------------------------------------------" );
            print("O jogador {} tirou o n {}.".format(ordem_jogadores[count],dado_sorteado) );
            
            go_ahead = dado_sorteado;
            current_house.insert(count, go_ahead+continuar[count]);
            current_player.insert(count, ordem_jogadores[count]);
            
            if gameArea.arr_casas[go_ahead] == 0:
                print("\nO jogador {} caiu em uma casa sem propriedades para adquirir".format(ordem_jogadores[count]) );
            
            elif gameArea.arr_casas[go_ahead] == 1:
                print("\nO jogador {} comprou a propriedade na casa: {}".format(ordem_jogadores[count], go_ahead) );
                
                if ordem_jogadores[count] == 1:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 1;
                    
                    price = random.randint(50, 175);
                    j1.compra(price);
                    print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );

                elif ordem_jogadores[count] == 2:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 2;
                
                    price = random.randint(50, 175);
                    j2.compra(price);
                    print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );

                elif ordem_jogadores[count] == 3:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 3;
                
                    price = random.randint(50, 175);
                    j3.compra(price);
                    print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );

                elif ordem_jogadores[count] == 4:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 4;

                    price = random.randint(50, 175);
                    j4.compra(price);
                    print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );


            elif gameArea.arr_casas[go_ahead] == 2:
                print("\nO jogador {} caiu na casa {}, anteriormente comprada, devera pagar aluguel.".format(ordem_jogadores[count], go_ahead) );
                
                if ordem_jogadores[count] == 1:
                    
                    price = random.randint(15, 75);
                    j1.pagarAluguel(price);
                    print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );

                    if gameArea.arr_comprados[go_ahead] == 2:
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                        j3.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                        j4.receberAluguel(price)

                    if j1.saldo < 0:
                        print("O jogador 1 teve o saldo zerado, portando será retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j1.saldo = 0;

                elif ordem_jogadores[count] == 2:
                    
                    price = random.randint(15, 75);
                    j2.pagarAluguel(price);
                    print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );

                    if gameArea.arr_comprados[go_ahead] == 1:
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                        j3.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                        j4.receberAluguel(price)

                    if j2.saldo < 0:
                        print("O jogador 2 teve o saldo zerado, portando será retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j2.saldo = 0;

                elif ordem_jogadores[count] == 3:
                    
                    price = random.randint(15, 75);
                    j3.pagarAluguel(price);
                    print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );

                    if gameArea.arr_comprados[go_ahead] == 1:
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 2:
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                        j4.receberAluguel(price)
                    
                    if j3.saldo < 0:
                        print("O jogador 3 teve o saldo zerado, portando será retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j3.saldo = 0;

                elif ordem_jogadores[count] == 4:
                    
                    price = random.randint(15, 75);
                    j4.pagarAluguel(price);
                    print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );

                    if gameArea.arr_comprados[go_ahead] == 1:
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 2:
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                        j3.receberAluguel(price)
                    
                    if j4.saldo < 0:
                        print("O jogador 4 teve o saldo zerado, portando será retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j4.saldo = 0;

            if(current_house[count] > 60):
                current_house.insert(count, 0+go_ahead)
                
                if current_player[count] == 1:
                    j1.addVoltas(1, j1);
                
                elif current_player[count] == 2:
                    j2.addVoltas(1, j2);
            
                elif current_player[count] == 3:
                    j3.addVoltas(1, j3);

                elif current_player[count] == 4:
                    j4.addVoltas(1, j4);

            count+= 1
        elif ordem_jogadores[count] == -1:
            count+= 1
            #pass
    
    if ordem_jogadores[0] == -1 and ordem_jogadores[1] == -1 and ordem_jogadores[2] == -1:
        print("Sobrou apenas um jogador, o jogo está terminado, o vencedor é o jogador {}".format(ordem_jogadores[3]))

        print("\n-------------------------------------------------------------------------------------------------" );
        print("Exibindo placar final:\n" );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        
        getEndTime();
        encerrar()

    elif ordem_jogadores[0] == -1 and ordem_jogadores[1] == -1 and ordem_jogadores[3] == -1:
        print("Sobrou apenas um jogador, o jogo está terminado, o vencedor é o jogador {}".format(ordem_jogadores[2]))
        
        print("Exibindo placar final:\n" );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        
        getEndTime();
        encerrar()

    elif ordem_jogadores[1] == -1 and ordem_jogadores[2] == -1 and ordem_jogadores[3] == -1:
        print("Sobrou apenas um jogador, o jogo está terminado, o vencedor é o jogador {}".format(ordem_jogadores[0]))
        
        print("Exibindo placar final:\n" );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        
        getEndTime();
        encerrar()

    elif ordem_jogadores[1] == -1 and ordem_jogadores[2] == -1 and ordem_jogadores[0] == -1:
        print("Sobrou apenas um jogador, o jogo está terminado, o vencedor é o jogador {}".format(ordem_jogadores[3]))
        
        print("Exibindo placar final:\n" );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        
        getEndTime();
        encerrar()

    elif ordem_jogadores[2] == -1 and ordem_jogadores[3] == -1 and ordem_jogadores[0] == -1:
        print("Sobrou apenas um jogador, o jogo está terminado, o vencedor é o jogador {}".format(ordem_jogadores[1]))
        getEndTime();
        encerrar()

    print("-------------------------------------------------------------------------------------------------\n" );
    continuar.insert(0, current_house[0])
    continuar.insert(1, current_house[1])
    continuar.insert(2, current_house[2])
    continuar.insert(3, current_house[3])

    


def main():

    print("Iniciando o jogo..." )
    print("Por favor, veja o arquivo 'log.txt' caso queira rever o andamento do jogo." )
     
    stdoutOrigin=sys.stdout 
    sys.stdout = open("log.txt", "w")

    print("Iniciando o jogo...\n" )
    
    print("Iniciando modulos...\n" );
    loading();

    print("Gerando tabuleiro...\n" );
    
    loading();
    #Criando objeto do tabuleiro...;
    gameArea = Board.Board([], 0, 0, []);
    
    loading();
    #definindo as propriedades...;
    gameArea.setPropriedades();

    loading();
    num_casas_tabuleiro = gameArea.arr_casas.count(0)+gameArea.arr_casas.count(1);
    
    print("Tabuleiro gerado!\n" );

    loading();
    print("Informacoes do tabuleiro:\nN de casas no tabuleiro: {}\nN de propriedades:{}\nN de propiedades compradas: {}\n".format(num_casas_tabuleiro,gameArea.n_propriedades, gameArea.n_prop_compradas) );

    loading();
    loading();

    print("Conectando jogadores...\n" );

    loading();

    print("Jogador 1 encontrado!\n" );
    j1 = Player.Player(1, 300, 0);

    loading();
    print("Jogador 2 encontrado!\n" );
    j2 = Player.Player(2, 300, 0);

    loading();
    print("Jogador 3 encontrado!\n" );
    j3 = Player.Player(3, 300, 0);

    loading();
    print("Jogador 4 encontrado!\n" );
    j4 = Player.Player(4, 300, 0);

    print("Exibindo informacoes dos jogadores:\n" );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
    print("-------------------------------------------------------------------------------------------------" );

    loading();
    print("Gerando o dado...\n" );

    #criando objeto do Dado;
    dice = Dice.Dice(0, []);

    #definindo dados do Dado;
    dice.setDice();

    loading();

    print("Os lados do dado:\n{}\n".format(dice.arrayNum) );

    loading();

    print("Reordenando jogadores em uma ordem aleatoria...\n" );

    loading();

    array_numbers = [1, 2, 3, 4];
    array_players = list(array_numbers);
    random.shuffle(array_players)

    print("E a ordem de jogada dos jogadores sera:\n{}".format(array_players) );

    print("Iniciando partida...\n" );

    loading();

    iterations = 0;
    end = 2000;

    while iterations < end:
        print("Rolando dados...\n" );
        round(array_players, dice, gameArea, j1, j2, j3, j4);
        
        loading();
        
        print("Exibindo resultados...\n" )
        
        print("O jogador {} parou na casa {}.".format(current_player[0], current_house[0]) )
        print("-------------------------------------------------------------------------------------------------\n" );
        
        print("O jogador {} parou na casa {}.".format(current_player[1], current_house[1]) )
        print("-------------------------------------------------------------------------------------------------\n" );
        
        print("O jogador {} parou na casa {}.".format(current_player[2], current_house[2]) )
        print("-------------------------------------------------------------------------------------------------\n" );
        
        print("O jogador {} parou na casa {}.".format(current_player[3], current_house[3]) )
        print("-------------------------------------------------------------------------------------------------\n" );
        
        loading()
        iterations+=1;

        print("Exibindo informacoes dos jogadores:\n" );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j1.numJogador, j1.saldo, j1.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j2.numJogador, j2.saldo, j2.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j3.numJogador, j3.saldo, j3.voltas) );
        print("-------------------------------------------------------------------------------------------------" );
        print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}".format(j4.numJogador, j4.saldo, j4.voltas) );
        print("-------------------------------------------------------------------------------------------------" );

        if j1.voltas == 1000:
            print("O jogador 1 chegou ao limite de iterações, portando o jogo será encerrado por timeout.");
            getEndTime();
            encerrar();
        elif j2.voltas == 1000:
            print("O jogador 2 chegou ao limite de iterações, portando o jogo será encerrado por timeout.");
            getEndTime();
            encerrar();
        elif j3.voltas == 1000:
            print("O jogador 3 chegou ao limite de iterações, portando o jogo será encerrado por timeout.");
            getEndTime();
            encerrar();
        elif j4.voltas == 1000:
            print("O jogador 4 chegou ao limite de iterações, portando o jogo será encerrado por timeout.");
            getEndTime();
            encerrar();


    getEndTime();

    sys.stdout.close();
    sys.stdout=stdoutOrigin;
    
    encerrar();


if __name__ == "__main__":
    main();