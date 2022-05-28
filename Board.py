import random
from tracemalloc import start

class Board:
    def __init__(self, arr_casas, n_propriedades, arr_valor_casa, arr_valor_aluguel , arr_comprados):
        self.arr_casas = arr_casas;
        self.n_propriedades = n_propriedades;
        self.arr_valor_casa = arr_valor_casa;
        self.arr_valor_aluguel = arr_valor_aluguel;
        self.arr_comprados = arr_comprados;
    
    def setPropriedades(self):
        self.n_propriedades = 20;
        # 0 = vazia, 1 = propriedade para compra, 2 = propriedade comprada;
        self.arr_casas = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
                          0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
                          0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
                          1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
                          0, 1, 0, 0, 1, 0];

        # 0 = ninguem comprou, 1 = J1 comprou, 2 = J2 comprou, 3 = J3 comprou, 4 = J4 comprou;
        self.arr_comprados = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
                              0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
                              0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
                              1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
                              0, 1, 0, 0, 1, 0];
        start = 0
        end = 61
        while start < end:
            valorCasa = random.randint(15,75);
            self.arr_valor_casa.insert(start+2, valorCasa);
            start+=1;


        start = 0
        while start < end:
            valorAluguel = random.randint(15,75);
            self.arr_valor_aluguel.insert(start+2, valorAluguel);
            start+=1;
        


    
    def buyPropriedade(self, numJogador, prop_index):
        self.arr_casas[prop_index] = 2;
        self.arr_comprados[prop_index] = numJogador;