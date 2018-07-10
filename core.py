from random import randrange, randint


def new_gladiator(gladiator_name, health, rage, damage_low, damage_high):
    return dict(
        gladiator_name=gladiator_name,
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
        print('{} critical hit {} for {} damage!'.format(
            attacker['gladiator_name'], defender['gladiator_name'],
            damage_dealt))
        defender['health'] -= damage_dealt
    else:
        defender['health'] = defender['health'] - damage_dealt
        defender['rage'] += 15
        print('{} hit {} for {} damage'.format(attacker['gladiator_name'],
                                               defender['gladiator_name'],
                                               damage_dealt))
    if defender['health'] < 0:
        print('{} has been fatally wounded by {}'.format(
            defender['gladiator_name'], attacker['gladiator_name']))
        defender['health'] = 0


def heal(gladiator):
    if (gladiator['health'] + 5) > 100 and gladiator['health'] < 100:
        gladiator['rage'] -= 10
        gladiator['health'] = 100
    elif (gladiator['health'] + 5) < 100:
        gladiator['rage'] -= 10
        gladiator['health'] += 5
    else:
        pass


def is_dead(gladiator):
    return not gladiator['health']
