import datetime
import time
import random
import sys

#para contar quantas partdas basta calcular uma variável no campo onde é dado timeout e aumentar um em cada ocorrencia
num_match_timeout = 25;

#para saber a porcentagem de vitoria do jogador, use a quantidade de vitorias dividido por 300 e multiplicado por 100

victory_j1 = float(100);
victory_j2 = float(32);
victory_j3 = float(7);
victory_j4 = float(11);


victory_tax_j1 = float("{:.2f}".format((victory_j1 / 300)*100))
victory_tax_j2 = float("{:.2f}".format((victory_j2 / 300)*100))
victory_tax_j3 = float("{:.2f}".format((victory_j3 / 300)*100))
victory_tax_j4 = float("{:.2f}".format((victory_j4 / 300)*100))

#no metodo que decide o vencedor por timeout e por saldo, adicionar 1 na variavel de contagem de vitorias do jogador e comparar depois.
player_with_more_victory = 1;

# CALCULO DE MEDIA RODADAS POR PARTIDA OK.

#crie uma variavel para estocar a quantidade de turnos de cada partida.
mean_turn_per_match = []

start = 0
end = 300

while start < end:
    #aqui usei um numero randomizado, mas a cada encerramento de partida, popule o array 300 vezes com a quantidade de rodadas que a partida foi encerrada
    minutes_test = random.randint(3, 100)
    mean_turn_per_match.insert(start, minutes_test);
    start+=1;

start = 0
end = 300

#criei uma variável para fazer a soma dos minutos.
sum_time = 0

#aqui mapearemos o array anteriormente criado com os minutos de cada partida
while start < end:
    sum_time = sum_time + mean_turn_per_match[start];
    start+=1;

#divida a soma total pelo numero total de partidas, sairá um valor float, então converta para int.
mean_turns = int(sum_time / end)

stdoutOrigin=sys.stdout 
sys.stdout = open("output.txt", "w")

print("A quantidade de partidas que terminaram por timeout foi: {}".format(num_match_timeout))
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
print("O comportamento do jogador {} e o que mais vence.".format(player_with_more_victory))

sys.stdout.close();
sys.stdout=stdoutOrigin;