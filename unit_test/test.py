import Player

j1 = Player.Player(1, 300, 0, 250, 0);

j4 = Player.Player(1, 300, 5, 5, 0)

j2 = Player.Player(2, 300, 0, j4.vitorias, 0)

j2.addVitorias(j4.vitorias)

print("AAA: {}".format(j2.vitorias))