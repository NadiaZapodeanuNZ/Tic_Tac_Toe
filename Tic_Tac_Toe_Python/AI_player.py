from players import Player
class AI(Player):
    def __init__(self, difficulty):
        super().__init__(2, "red")
        self.difficulty = difficulty

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        