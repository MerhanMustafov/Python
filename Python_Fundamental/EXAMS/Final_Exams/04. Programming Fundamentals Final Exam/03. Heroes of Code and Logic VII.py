n = int(input())
data = {}
for _ in range(n):
    text = input().split()
    hero = text[0]
    hp = int(text[1])
    if hp > 100:
        hp = 100
    mp = int(text[2])
    if mp > 200:
        mp = 200
    data[hero] = {'hp': hp, 'mp': mp}


command = input()
while not command == 'End':
    command = command.split(" - ")
    if command[0] == "CastSpell":
        cur_hero = command[1]
        needed_mp = int(command[2])
        spell_name = command[3]
        if data[cur_hero]['mp'] >= needed_mp:
            data[cur_hero]['mp'] -= needed_mp
            print(f"{cur_hero} has successfully cast {spell_name} and now has {data[cur_hero]['mp']} MP!")
        else:
            print(f"{cur_hero} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        cur_hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        data[cur_hero]['hp'] -= damage
        if data[cur_hero]['hp'] > 0:
            print(f"{cur_hero} was hit for {damage} HP by {attacker} and now has {data[cur_hero]['hp']} HP left!")
        else:
            data.pop(cur_hero)
            print(f"{cur_hero} has been killed by {attacker}!")

    elif command[0] == "Recharge":
        cur_hero = command[1]
        amount = int(command[2])
        if data[cur_hero]['mp'] + amount > 200:
            recharge_amoount = 200 - data[cur_hero]['mp']
            data[cur_hero]['mp'] += recharge_amoount
            print(f"{cur_hero} recharged for {recharge_amoount} MP!")
        else:
            data[cur_hero]['mp'] += amount
            print(f"{cur_hero} recharged for {amount} MP!")

    elif command[0] == "Heal":
        cur_hero = command[1]
        amount = int(command[2])
        if data[cur_hero]['hp'] + amount > 100:
            heal_amount = 100 - data[cur_hero]['hp']
            data[cur_hero]['hp'] += heal_amount
            print(f"{cur_hero} healed for {heal_amount} HP!")
        else:
            data[cur_hero]['hp'] += amount
            print(f"{cur_hero} healed for {amount} HP!")
    command = input()

data = sorted(data.items(), key=lambda kdv: (-kdv[1]['hp'], kdv[0]))
for hero_name, data_dict in data:
    print(f"{hero_name}\n HP: {data_dict['hp']}\n MP: {data_dict['mp']}")
  