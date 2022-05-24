class Board:
    def __init__(self, arr_casas, n_propriedades,n_prop_compradas, arr_comprados):
        self.arr_casas = arr_casas;
        self.n_propriedades = n_propriedades;
        self.n_prop_compradas = n_prop_compradas;
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
     
        self.n_prop_compradas = 0;
    
    def buyPropriedade(self, numJogador, prop_index):
        self.arr_casas[prop_index] = 2;
        self.arr_comprados[prop_index] = numJogador;