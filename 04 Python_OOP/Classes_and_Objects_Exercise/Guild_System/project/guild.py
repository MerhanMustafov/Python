from project.player import Player
from typing import List

class Guild:
    all_guild_players = []
    def __init__(self, name):
        self.name = name
        self.players:  List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player in self.all_guild_players:
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            self.all_guild_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                self.all_guild_players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"\

        for player in self.players:
            result += player.player_info() + "\n"
        return result[:-1]


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())



# # from project.player import Player
# # from typing import List
# #
# #
# # class Guild:
# #     def __init__(self, name: str) -> None:
# #         self.name = name
# #         self.players: List[Player] = []
# #
# #     def assign_player(self, player: Player) -> str:
# #         if player in self.players:
# #             return f'Player {player.name} is already in the guild.'
# #
# #         if player.guild != 'Unaffiliated':
# #             return f'Player {player.name} is in another guild.'
# #
# #         self.players.append(player)
# #         player.guild = self.name
# #         return f'Welcome player {player.name} to the guild {self.name}'
# #
# #     def kick_player(self, player_name: str) -> str:
# #         for i, player in enumerate(self.players):
# #             if player.name == player_name:
# #                 self.players.pop(i)
# #                 return f'Player {player_name} has been removed from the guild.'
# #         return f'Player {player_name} is not in the guild.'
# #
# #     def guild_info(self):
# #         message = []
# #         nl = '\n'
# #
# #         message.append(f'Guild: {self.name}')
# #         for player in self.players:
# #             message.append(player.player_info())
# #
# #         return nl.join(message)
# #
# #
# #
