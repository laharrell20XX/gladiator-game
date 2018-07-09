from random import randrange, randint


def new_gladiator(health, rage, damage_low, damage_high):
    #gladiator = {}
    #gladiator[health] = health
    #gladiator[rage] = rage
    #gladiator[damage_low] = damage_low
    #gladiator[damage_high] = damage_high
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
