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
continuar = [0,0,0,0];

timeout_times = 0;

finished = False;
sum_rounds = 4;

def getEndTime():
    print("\n\nTempo decorrido(HH:MM:SS:MS):" );
    print(datetime.datetime.now() - begin_time );

def encerrar():
    exit()

def loading():
    time.sleep(0.5);

def round(ordem_jogadores, dice, gameArea, j1, j2, j3, j4, sum_rounds):
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

                    j1.contaPassos(dado_sorteado);
                    
                    price = gameArea.arr_valor_casa[go_ahead]
                    j1.compra(price);
                    print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );

                elif ordem_jogadores[count] == 2:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 2;

                    j2.contaPassos(dado_sorteado);
                     
                    if gameArea.arr_valor_aluguel[go_ahead] > 50:
                        price = gameArea.arr_valor_casa[go_ahead]
                        j2.compra(price);
                        print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );
                    else:
                        print("O jogador {} caiu em uma propriedade que pode ser comprada, porem, pelo aluguel nao ser superior a 50 como demanda suas exigencias, nao comprara.".format(j2.numJogador))

                elif ordem_jogadores[count] == 3:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 3; 
                     
                    price = gameArea.arr_valor_casa[go_ahead]

                    j3.contaPassos(dado_sorteado);

                    if j3.saldo - price > 80:
                        j3.compra(price);
                        print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );
                    else:
                        print("O jogador {} caiu em uma propriedade que pode ser comprada, porem, pelo fato de ficar com saldo inferior a 80 apos a compra, nao demanda com suas exigencias.".format(j3.numJogador))

                elif ordem_jogadores[count] == 4:
                    
                    gameArea.arr_casas[go_ahead] = 2;
                    gameArea.arr_comprados[go_ahead] = 4;

                    choice = random.randint(0,1);

                    j4.contaPassos(dado_sorteado);

                    if choice == 0:
                        price = gameArea.arr_valor_casa[go_ahead]
                        j4.compra(price);
                        print("Apos a compra do jogador {}, no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );

                    elif choice == 1:
                        print("O jogador {}, devido a seu comportamento aleatorio, decidiu nao comprar a proprieade".format(j4.numJogador))


            elif gameArea.arr_casas[go_ahead] == 2:
                print("\nO jogador {} caiu na casa {}, anteriormente comprada, devera pagar aluguel.".format(ordem_jogadores[count], go_ahead) );
                
                if ordem_jogadores[count] == 1:

                    if gameArea.arr_comprados[go_ahead] == 2:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j1.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );
                        
                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j2.numJogador, price))
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j1.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j3.numJogador, price))
                        j3.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j1.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j1.numJogador, price, j1.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j4.numJogador, price))
                        j4.receberAluguel(price)

                    if j1.saldo < 0:
                        print("O jogador 1 teve o saldo zerado, portando sera retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j1.saldo = 0;

                elif ordem_jogadores[count] == 2:

                    if gameArea.arr_comprados[go_ahead] == 1:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j2.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j1.numJogador, price))
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j2.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j3.numJogador, price))
                        j3.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j2.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j2.numJogador, price, j2.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j4.numJogador, price))
                        j4.receberAluguel(price)

                    if j2.saldo < 0:
                        print("O jogador 2 teve o saldo zerado, portando sera retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j2.saldo = 0;

                elif ordem_jogadores[count] == 3:

                    if gameArea.arr_comprados[go_ahead] == 1:
                        
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j3.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j1.numJogador, price))
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 2:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j3.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j2.numJogador, price))
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 4:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j3.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j3.numJogador, price, j3.saldo) );
                        
                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j4.numJogador, price))
                        j4.receberAluguel(price)
                    
                    if j3.saldo < 0:
                        print("O jogador 3 teve o saldo zerado, portando sera retirado da partida.")
                        ordem_jogadores[count] = -1;
                        j3.saldo = 0;

                elif ordem_jogadores[count] == 4:

                    if gameArea.arr_comprados[go_ahead] == 1:
                        
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j4.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );
                        
                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j1.numJogador, price))
                        j1.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 2:
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j4.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j2.numJogador, price))
                        j2.receberAluguel(price)

                    elif gameArea.arr_comprados[go_ahead] == 3:
                        
                         
                        price = gameArea.arr_valor_aluguel[go_ahead]
                        j4.pagarAluguel(price);
                        print("Apos o jogador {} pagar o aluguel , no valor de {}, o saldo atual e: {}\n".format(j4.numJogador, price, j4.saldo) );

                        print("O jogador {} ira receber {} de saldo pelo aluguel.".format(j3.numJogador, price))
                        j3.receberAluguel(price)
                    
                    if j4.saldo < 0:
                        print("O jogador 4 teve o saldo zerado, portando sera retirado da partida.")
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

    if ordem_jogadores[0] == -1 and ordem_jogadores[1] == -1 and ordem_jogadores[2] == -1:
        
        if ordem_jogadores[3] == 1:
            j2.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[3] == 2:
            j1.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[3] == 3:
            j1.saldo = 0
            j2.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[3] == 4:
            j1.saldo = 0
            j2.saldo = 0
            j3.saldo = 0
        
        print("\nSobrou apenas um jogador, o jogo esta terminado, o vencedor e o jogador {}".format(ordem_jogadores[3]))

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
        finished = True;

    elif ordem_jogadores[0] == -1 and ordem_jogadores[1] == -1 and ordem_jogadores[3] == -1:

        if ordem_jogadores[2] == 1:
            j2.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[2] == 2:
            j1.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[2] == 3:
            j1.saldo = 0
            j2.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[2] == 4:
            j1.saldo = 0
            j2.saldo = 0
            j3.saldo = 0
        
        print("Sobrou apenas um jogador, o jogo esta terminado, o vencedor e o jogador {}".format(ordem_jogadores[2]))
        
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
        finished = True;

    elif ordem_jogadores[1] == -1 and ordem_jogadores[2] == -1 and ordem_jogadores[3] == -1:

        if ordem_jogadores[0] == 1:
            j2.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[0] == 2:
            j1.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[0] == 3:
            j1.saldo = 0
            j2.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[0] == 4:
            j1.saldo = 0
            j2.saldo = 0
            j3.saldo = 0
        
        print("Sobrou apenas um jogador, o jogo esta terminado, o vencedor e o jogador {}".format(ordem_jogadores[0]))
        
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
        finished = True;         

    elif ordem_jogadores[2] == -1 and ordem_jogadores[3] == -1 and ordem_jogadores[0] == -1:

        if ordem_jogadores[1] == 1:
            j2.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[1] == 2:
            j1.saldo = 0
            j3.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[1] == 3:
            j1.saldo = 0
            j2.saldo = 0
            j4.saldo = 0
        elif ordem_jogadores[1] == 4:
            j1.saldo = 0
            j2.saldo = 0
            j3.saldo = 0

        print("Sobrou apenas um jogador, o jogo esta terminado, o vencedor e o jogador {}".format(ordem_jogadores[1]))
        
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
        finished = True;
      
    print("-------------------------------------------------------------------------------------------------\n" );
    continuar.insert(0, current_house[0])
    continuar.insert(1, current_house[1])
    continuar.insert(2, current_house[2])
    continuar.insert(3, current_house[3])

def output(j1,j2,j3,j4,timeout_times, sum_rounds):
    
    print("\n300 partidas encerradas.\n")

    print("Gerando os resultados..." )
    print("Por favor, veja o arquivo 'output.txt' para ver o resultado." )
                        
    stdoutOriginOutput=sys.stdout 
    sys.stdout = open("output.txt", "w")

    victory_tax_j1 = float("{:.2f}".format((j1.vitorias / 300)*100))
    victory_tax_j2 = float("{:.2f}".format((j2.vitorias / 300)*100))
    victory_tax_j3 = float("{:.2f}".format((j3.vitorias / 300)*100))
    victory_tax_j4 = float("{:.2f}".format((j4.vitorias / 300)*100))

    end = 300

    mean_turns = int(sum_rounds / end)

    print("A quantidade de partidas que terminaram por timeout foi: {}".format(timeout_times))
    print("-------------------------------------------------------------------------------------------------" );
    print("A media de turnos em uma partida e: {}".format(mean_turns))
    print("-------------------------------------------------------------------------------------------------" );
    print("A taxa de vitorias do jogador 1 e: {}%".format(victory_tax_j1));
    print("-------------------------------------------------------------------------------------------------" );
    print("A taxa de vitorias do jogador 2 e: {}%".format(victory_tax_j2));
    print("-------------------------------------------------------------------------------------------------" );
    print("A taxa de vitorias do jogador 3 e: {}%".format(victory_tax_j3));
    print("-------------------------------------------------------------------------------------------------" );
    print("A taxa de vitorias do jogador 4 e: {}%".format(victory_tax_j4));
    print("-------------------------------------------------------------------------------------------------" );
    if j1.vitorias > j2.vitorias and j1.vitorias > j3.vitorias and j1.vitorias > j4.vitorias:
        print("O comportamento do jogador 1 foi o com mais vitorias")
    elif j2.vitorias > j1.vitorias and j2.vitorias > j3.vitorias and j2.vitorias > j4.vitorias:
        print("O comportamento do jogador 2 foi o com mais vitorias")
    elif j3.vitorias > j1.vitorias and j3.vitorias > j2.vitorias and j3.vitorias > j4.vitorias:
        print("O comportamento do jogador 3 foi o com mais vitorias")
    elif j4.vitorias > j1.vitorias and j4.vitorias > j2.vitorias and j4.vitorias > j3.vitorias:
        print("O comportamento do jogador 4 foi o com mais vitorias")
    else:
        print("Houve um ou mais jogadores que tiveram a mesma porcentagem de vitoria.")

    sys.stdout.close();
    sys.stdout=stdoutOriginOutput;
            
    encerrar();   


def main(timeout_times, finished, sum_rounds):
    
    print("Iniciando o jogo..." )
    print("Por favor, veja o arquivo 'log.txt' caso queira ver como foi a partida em detalhes." )
     
    stdoutOrigin=sys.stdout 
    sys.stdout = open("log.txt", "w")

    print("Iniciando o jogo...\n" )
    
    print("Iniciando modulos...\n" );
    loading();

    print("Gerando tabuleiro...\n" );
    
    loading();
    #Criando objeto do tabuleiro...;
    gameArea = Board.Board([], 0, [], [], []);
    
    loading();
    #definindo as propriedades...;
    gameArea.setPropriedades();
    
    print("Tabuleiro gerado!\n" );

    loading();

    print("Conectando jogadores...\n" );

    loading();

    print("Jogador 1 encontrado!\n" );
    j1 = Player.Player(1, 300, 0, 0, 0);

    loading();
    print("Jogador 2 encontrado!\n" );
    j2 = Player.Player(2, 300, 0, 0, 0);

    loading();
    print("Jogador 3 encontrado!\n" );
    j3 = Player.Player(3, 300, 0, 0, 0);

    loading();
    print("Jogador 4 encontrado!\n" );
    j4 = Player.Player(4, 300, 0, 0, 0);

    print("Exibindo informacoes dos jogadores:\n" );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}\nN de vitorias: {}".format(j1.numJogador, j1.saldo, j1.voltas, j1.vitorias) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}\nN de vitorias: {}".format(j2.numJogador, j2.saldo, j2.voltas, j2.vitorias) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}\nN de vitorias: {}".format(j3.numJogador, j3.saldo, j3.voltas, j3.vitorias) );
    print("-------------------------------------------------------------------------------------------------" );
    print("Jogador {}:\nSaldo: {}\nN de voltas no tabuleiro: {}\nN de vitorias: {}".format(j4.numJogador, j4.saldo, j4.voltas, j4.vitorias) );
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

    inicio = 0
    fim = 300

    while inicio < fim:

        inicio+=1;

        while finished == False:
            print("Rolando dados...\n" );
            round(array_players, dice, gameArea, j1, j2, j3, j4, sum_rounds);
            sum_rounds += 4
            
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

            if sum_rounds == 1000:
                print("O jogo atingiu o numero maximo de rodadas, por tanto encerrara com timeout");
                timeout_times +=1;

                if j4.saldo > j1.saldo and j4.saldo > j2.saldo and j4.saldo > j3.saldo:
                    print("Para criterio de desempate, o jogador 4 ganhou por ter mais saldo.")
                    j4.addVitorias(1.0);
                    
                elif j3.saldo > j1.saldo and j3.saldo > j2.saldo and j3.saldo > j4.saldo:
                    print("Para criterio de desempate, o jogador 3 ganhou por ter mais saldo.")
                    j3.addVitorias(1.0);
                    
                elif j2.saldo > j1.saldo and j2.saldo > j3.saldo and j2.saldo > j4.saldo:
                    print("Para criterio de desempate, o jogador 2 ganhou por ter mais saldo.")
                    j2.addVitorias(1.0);
                    
                elif j1.saldo > j2.saldo and j1.saldo > j3.saldo and j1.saldo > j4.saldo:
                    print("Para criterio de desempate, o jogador 1 ganhou por ter mais saldo.")
                    j1.addVitorias(1.0);
                
                getEndTime();
                finished = True;
        
        print("Gerando um novo tabuleiro...\n" );
    
        loading();
        #Criando objeto do tabuleiro...;
        gameArea = Board.Board([], 0, [], [], []);
        
        loading();
        #definindo as propriedades...;
        gameArea.setPropriedades();
        
        print("Tabuleiro gerado!\n" );

        loading();

        print("Conectando novos jogadores...\n" );

        loading();

        print("Jogador 1 encontrado!\n" );
        j1 = Player.Player(1, 300, 0, j1.vitorias, 0);

        loading();
        print("Jogador 2 encontrado!\n" );
        j2 = Player.Player(2, 300, 0, j2.vitorias, 0);

        loading();
        print("Jogador 3 encontrado!\n" );
        j3 = Player.Player(3, 300, 0, j3.vitorias, 0);

        loading();
        print("Jogador 4 encontrado!\n" );
        j4 = Player.Player(4, 300, 0, j4.vitorias, 0);


        print("Reordenando jogadores em uma ordem aleatoria...\n" );

        loading();

        array_numbers = [1, 2, 3, 4];
        array_players = list(array_numbers);
        random.shuffle(array_players)

        print("E a ordem de jogada dos jogadores sera:\n{}".format(array_players) );

        print("Iniciando partida...\n" );

        finished = False;
                

    sys.stdout.close();
    sys.stdout=stdoutOrigin;


    output(j1,j2,j3,j4,timeout_times, sum_rounds)


if __name__ == "__main__":
    main(timeout_times, finished, sum_rounds);