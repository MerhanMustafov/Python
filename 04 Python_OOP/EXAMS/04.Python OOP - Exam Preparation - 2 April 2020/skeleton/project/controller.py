from project.battle_field import BattleField
from project.card.card_repository import CardRepository

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        player = None
        if type == "Advanced":
            player = Advanced(username)
        if type == "Beginner":
            player = Beginner(username)
        self.player_repository.players.append(player)
        return f"Successfully added player of type {type} with username: {username}"
    def add_card(self, type, name):
        card = None
        if type == "Magic":
            card = MagicCard(name)
        elif type == "Trap":
            card = TrapCard(name)
        self.card_repository.cards.append(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.cards.append(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"
    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += p.__str__()
        return result

# controller = Controller()
# print(controller.card_repository.cards)
# print(controller)



# player1 = Beginner("Huan")
# player2 = Advanced("Hachi")
# player3 = Beginner("Momo")
# player4 = Advanced("Bengi")
#
# controller = Controller()
# controller.add_player(type(player1), player1.username)
# controller.add_player(type(player2), player2.username)
# controller.add_player(type(player3), player3.username)
# controller.add_player(type(player4), player4.username)
#
#
#
#
# card1 = MagicCard("Name")
# card2 = MagicCard("Magic")
# card3 = TrapCard("Trap")
# card4 = TrapCard("Mag")
#
# controller.add_card(type(card1), card1.name)
# controller.add_card(type(card2), card2.name)
# controller.add_card(type(card3), card3.name)
# controller.add_card(type(card4), card4.name)
#
# x = controller.card_repository.cards
# y = controller.player_repository.players
# for one in x:
#     print(one.name)
#
# for two in y:
#     print(two.username)
#
#
# print("-"*20)
# controller.add_player_card("Huan", "Magic")
# for one in x:
#     print(one.name)
#
# for two in y:
#     print(two.username)