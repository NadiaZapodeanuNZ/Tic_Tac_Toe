class Player:
    def __init__(self, id_player, color):
        self.id_player = id_player
        self.color = color
        self.score = 0


    def increase_score(self):
        self.score += 1
        print(f"Score updated: {self.score}")
    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

 
    def get_id(self):
        return self.id_player

    def get_color(self):
        return self.color

