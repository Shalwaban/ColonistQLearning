import colonist_ql.patterns as patterns
from colonist_ql.game_structure.players import Player


class Board(metaclass=patterns.Singleton):
    def __init__(self):
        self.player_dict = None
        self.turn_order = None
        self.hex_dict = None

    def __init__(self, players, hexes):
        self.player_dict = {p.name: p for p in players}
        # self.hex_dict = {h.cube_coords: h for h in hexes}

    def get_player(self, player_name):
        return self.player_dict[player_name]

    def setup_game(self, players, hexes):
        self.__init__(players, hexes)

    def set_turn_order(self, turn_oder):
        self.turn_order = turn_oder


players = {"ZacTodd", "Tami#6966", "Oakes#7878", "bambee"}
Board([Player(p, "red", players - {p}) for p in players], None)