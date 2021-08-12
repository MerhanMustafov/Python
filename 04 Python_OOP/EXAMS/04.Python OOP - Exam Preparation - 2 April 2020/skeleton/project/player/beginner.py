from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super().__init__(username, 50)

# beginner = Beginner("NVP")
# print(beginner.username)
# print(beginner.health)
