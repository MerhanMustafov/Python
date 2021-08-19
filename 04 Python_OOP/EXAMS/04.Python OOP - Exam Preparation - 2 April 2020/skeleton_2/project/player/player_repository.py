class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        is_present = [p for p in self.players if p.username == player.username]
        if is_present:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player_name = self.find(player)
        self.players.remove(player_name)
        self.count -= 1
        return

    def find(self, username: str):
        for player in self.players:
            if player.username == username:
                return player
