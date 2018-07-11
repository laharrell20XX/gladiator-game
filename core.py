from random import randrange, randint


def new_gladiator(gladiator_name, health, rage, damage_low, damage_high,
                  defending, defense, stunned_turns):
    return dict(
        gladiator_name=gladiator_name,
        health=health,
        rage=rage,
        damage_low=damage_low,
        damage_high=damage_high,
        defending=defending,
        defense=defense,
        stunned_turns=stunned_turns)


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    crit_chance = randrange(1, 100)
    if crit_chance < attacker['rage']:  #the higher the rage, the bigger chance for a critical hit
        damage_dealt = damage_dealt * 2
        attacker['rage'] = 0
        if defender['defending']:
            damage_dealt = defend(defender, damage_dealt)
            print(
                'Critical hit successfully blocked! {} only received {} damage'.
                format(defender['gladiator_name'], damage_dealt))
        else:
            print('{} critically hit {} for {} damage!'.format(
                attacker['gladiator_name'], defender['gladiator_name'],
                damage_dealt))
        defender['health'] -= damage_dealt
    else:
        if defender['defending']:
            damage_dealt = defend(defender, damage_dealt)
            print('Hit was blocked! {} only received {} damage'.format(
                defender['gladiator_name'], damage_dealt))
            attacker['rage'] = 0
        else:
            attacker['rage'] += 15
            print('{} hit {} for {} damage'.format(attacker['gladiator_name'],
                                                   defender['gladiator_name'],
                                                   damage_dealt))
        defender['health'] -= damage_dealt

    if defender['health'] < 0:
        print('{} has been fatally wounded by {}'.format(
            defender['gladiator_name'], attacker['gladiator_name']))
        defender['health'] = 0


def defend(defender,
           damage_dealt):  #should reduce the damage of the next hit by 50%
    damage_dealt = damage_dealt - (damage_dealt * defender['defense'] / 4)
    return damage_dealt


def defend_counter(defender):
    if defender['defending']:  #checks if gladiator is defending
        if defender['defense'] - 1 < 0:  #gladiator no longer defends if their defense is below 0
            defender['defending'] = False
        else:
            gladiator[
                'defense'] -= 1  #for every turn a gladiator defends, their defense goes down by 1
    else:  #checks if gladiator is not defending
        if defender['defense'] - 1 < 0 and not defender['stunned_turns']:
            defender['stunned_turns'] = 3
            defender[
                'defense'] = 3  #if gladiator is no longer stunned, defense regenerates


def heal(gladiator):
    if gladiator['health'] + 5 > 100:
        gladiator['health'] = min((gladiator['health'] + 5), 100)
        gladiator['rage'] -= 10
        gladiator['defense'] = 3
        #when gladiator is healed, their defense is refilled
    else:
        gladiator['rage'] -= 10
        gladiator['health'] += 5
        gladiator['defense'] = 3


def is_dead(gladiator):
    return not gladiator['health']
