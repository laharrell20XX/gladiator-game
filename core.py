from random import randrange, randint


def new_gladiator(gladiator_name, health, rage, damage_low, damage_high,
                  defending, defense, stunned_turns, stunned_status,
                  miss_chance, weapon):
    return dict(
        gladiator_name=gladiator_name,
        health=health,
        rage=rage,
        damage_low=damage_low,
        damage_high=damage_high,
        defending=defending,
        defense=defense,
        stunned_turns=stunned_turns,
        stunned_status='',
        miss_chance=miss_chance,
        weapon=weapon)


def weapon(weapon_name, damage_low, damage_high, miss_chance):
    return dict(
        weapon_name=weapon_name,
        damage_high=damage_high,
        damage_low=damage_low,
        miss_chance=miss_chance)


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    crit_chance, miss_chance = randrange(1, 100), randrange(1, 100)
    if crit_chance < attacker['rage']:  #the higher the rage, the bigger chance for a critical hit
        damage_dealt = damage_dealt * 2
        attacker['rage'] = 0
        if miss_chance < attacker['miss_chance']:  #if the attacker misses
            damage_dealt = 0
            attacker['rage'] = 0
            print(
                "With a mighty swing, {} cleaves an innocent rock at {}'s feet. {} laughs.".
                format(attacker['gladiator_name'], defender['gladiator_name'],
                       defender['gladiator_name']))
        else:
            if defender['defending']:
                if defender['defense'] > 0:  # if defense is high enough to block a crit hit
                    damage_dealt = defend(defender, damage_dealt)
                    print(
                        'Critical hit successfully blocked! {} only received {} damage'.
                        format(defender['gladiator_name'], damage_dealt))
                else:  #if defense is not high enough to block a crit hit
                    print('{} critically hit {} for {} damage!'.format(
                        attacker['gladiator_name'], defender['gladiator_name'],
                        damage_dealt))
                defender['defense'] -= 2
            else:
                print('{} critically hit {} for {} damage!'.format(
                    attacker['gladiator_name'], defender['gladiator_name'],
                    damage_dealt))
    else:  #normal hit condition
        if miss_chance < attacker['miss_chance']:
            damage_dealt = 0
            print(
                "You try to attack your opponent, but you miss and scuff his shoes instead. 'Those were new!' {} exclaims".
                format(defender['gladiator_name']))
            defender['rage'] += 10
        else:
            if defender['defending']:
                if defender['defense'] > 0:  # if defense is high enough to block a normal attack
                    damage_dealt = defend(defender, damage_dealt)
                    print('Hit was blocked! {} only received {} damage'.format(
                        defender['gladiator_name'], damage_dealt))
                    attacker['rage'] = 0
                else:  # if defense is not high enough to block a normal attack
                    attacker['rage'] += 15
                    print('{} hit {} for {} damage'.format(
                        attacker['gladiator_name'], defender['gladiator_name'],
                        damage_dealt))
                defender[
                    'defense'] -= 1  #defense is always decreased if glad is defending
            else:
                attacker['rage'] += 15
                print('{} hit {} for {} damage'.format(
                    attacker['gladiator_name'], defender['gladiator_name'],
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
        if defender['defense'] < 0:
            defender['stunned_status'] = '(stunned)'
            print(
                'Your shield has been broken {}.  Now you are stunned for 2 turns'.
                format(defender['gladiator_name']))
            defender[
                'defending'] = ''  #gladiator no longer defends if their defense is below 0
    else:  #checks if gladiator is not defending
        if defender['defense'] < 0 and not defender['stunned_turns']:
            defender['stunned_turns'] = 2
            defender['stunned_status'] = ''
            defender['defense'] = 0


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
