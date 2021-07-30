from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"
    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"\
                f"Pokemon count {len(self.pokemons)}\n"
        for pok in self.pokemons:
            result +=  f"- {pok.pokemon_details()}"
        return result



# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())






























# from typing import List
# from project.pokemon import Pokemon
# class Trainer:
#     name: str
#     pokemon: List[Pokemon]
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.pokemon = []
#
#     def add_pokemon(self, pokemon: Pokemon) -> str:
#         if pokemon in self.pokemon:
#             return "This pokemon is already caught"
#         self.pokemon.append(pokemon)
#         return f'Caught {pokemon.pokemon_details()}'
#
#     def release_pokemon(self, pokemon_name: str) -> str:
#         # pokemon_names = [p.name for p in self.pokemon]
#         # if pokemon_name not in pokemon_names:
#         #     return 'Pokemon is not caught'
#         for pok in range(len(self.pokemon)):
#             if pokemon_name in self.pokemon[pok].name:
#                 self.pokemon.remove(pok)
#                 return f"You have released {pokemon_name}"
#         return 'Pokemon is not caught'
#         # del self.pokemon[pokemon_name.index(pokemon_name)]
#         # return f"You have released {pokemon_name}"
#
#     def trainer_data(self):
#         trainer_info = [
#             f'Pokemon Trainer {self.name}' ,
#             f'Pokemon count {len(self.pokemon)}' ,
#         ]
#         pokemon_info = [f"- {p.pokemon_details()}" for p in self.pokemon]
#
#         return '\n'.join(trainer_info + pokemon_info) + '\n'