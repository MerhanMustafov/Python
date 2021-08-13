class BattleField:

    @staticmethod
    def fight(attacker, enemy):
        if enemy.is_dead or attacker.is_dead:
            raise ValueError("Player is dead!")
        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for c in attacker.card_repository.cards:
                c.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for c in enemy.card_repository.cards:
                c.damage_points += 30

        bonus_attacker = sum([c.health_points for c in attacker.card_repository.cards])
        bonus_enemy = sum([c.health_points for c in enemy.card_repository.cards])

        attacker.health += bonus_attacker
        enemy.health += bonus_enemy

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)
            if enemy.is_dead:
                return

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
            if attacker.is_dead:
                return



