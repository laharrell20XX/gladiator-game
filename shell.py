import core
from random import randint, choice


def gladiator(gladiator_name):
    gladiator = core.new_gladiator(gladiator_name, 100, 0, randint(0, 5),
                                   randint(6, 15), False)
    return gladiator


def show_gladiators(gladiator_1, gladiator_2):
    print('''
{}: {} HP ||| {} Rage
{}: {} HP ||| {} Rage'''
          .format(gladiator_1['gladiator_name'], gladiator_1['health'],
                  gladiator_1['rage'], gladiator_2['gladiator_name'],
                  gladiator_2['health'], gladiator_2['rage']))


def gladiator_makes_move(attacker, defender):
    while True:
        move = input('''{}... What would you like to do? {}
- attack
- pass
- quit
- heal
>>> '''.format(attacker['gladiator_name'], attacker['defending']))
        if 'attack' == move:
            return move
        elif 'pass' == move:
            return move
        elif 'quit' == move:
            print('{}: Survived!\n{}: Survived!'.format(
                defender['gladiator_name'], attacker['gladiator_name']))
            quit()
        elif 'heal' == move:
            return move
        elif 'defend' == move:
            return move
        elif 'supah kick' == move:  #Used to test death condititon
            return move
        elif 'angery' == move:  #Used to test critical hits
            return move
        else:
            print('Invalid input')


def gladiator_fight():  #add defend counter
    gladiator_1 = gladiator('Gladiator 1')
    gladiator_2 = gladiator('Gladiator 2')

    attacker, defender = gladiator_1, gladiator_2
    # while attacker['health'] and defender['health']:
    while True:
        show_gladiators(attacker, defender)
        gladiator_move = gladiator_makes_move(attacker, defender)
        if gladiator_move == 'attack':
            attacker['defending'] = False
            core.attack(attacker, defender)
        elif gladiator_move == 'defend':
            attacker['defending'] = True
        elif gladiator_move == 'supah kick':  #negative  health test
            defender['health'] -= 99
        elif gladiator_move == 'angery':  #crit hit test
            attacker['rage'] += 100
            continue
        elif gladiator_move == 'heal':
            attacker['defending'] = False
            if attacker['rage'] < 10:
                print("You try to heal, but you just aren't angry enough")
            if attacker['health'] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
                )
            else:
                core.heal(attacker)
        elif gladiator_move == 'pass':
            pass
        if core.is_dead(defender):
            print(
                '{} has died. Funeral procession tommorrow... {} Wins!'.format(
                    defender['gladiator_name'], attacker['gladiator_name']))
            break
        attacker, defender = defender, attacker  #uses multivariable assignment to switch between attacker and defender at the end of every while loop


def main():
    gladiator_fight()


if __name__ == '__main__':
    main()
