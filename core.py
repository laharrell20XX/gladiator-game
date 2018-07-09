from random import randrange, randint


def new_gladiator(health, rage, damage_low, damage_high):
    return dict(
        health=health,
        rage=rage,
        damage_low=damage_low,
        damage_high=damage_high)


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    crit_chance = randrange(1, 100)
    if crit_chance < attacker['rage']:  #the higher the rage, the bigger chance for a critical hit
        damage_dealt = damage_dealt * 2
        attacker['rage'] = 0
    if defender['health'] < damage_dealt:
        defender['health'] = 0
    else:
        defender['health'] = defender['health'] - damage_dealt
        defender['rage'] += 15


def heal(gladiator):
    if (gladiator['health'] + 5) > 100 and gladiator['health'] < 100:
        gladiator['rage'] -= 10
        gladiator['health'] = 100
    elif (gladiator['health'] + 5) < 100:
        gladiator['rage'] -= 10
        gladiator['health'] += 5
    else:
        pass
