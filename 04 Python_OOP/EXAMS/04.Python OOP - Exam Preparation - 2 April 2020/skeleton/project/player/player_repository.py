class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        for p in self.players:
            if p.username == player.username:
                raise ValueError(f"Player {p.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        self.players.remove(self.find(player))
        self.count -= 1

    def find(self, username: str):
        for p in self.players:
            if p.username == username:
                return p