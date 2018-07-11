import core
from random import randint, choice


def gladiator(gladiator_name):
    gladiator = core.new_gladiator(gladiator_name, 100, 0, randint(0, 5),
                                   randint(6, 15), False, 3, 3)
    return gladiator


def show_gladiators(gladiator_1, gladiator_2):
    print('''
{}: {} HP ||| {} Rage {} defense
{}: {} HP ||| {} Rage {} defense'''
          .format(gladiator_1['gladiator_name'], gladiator_1['health'],
                  gladiator_1['rage'], gladiator_1['defense'],
                  gladiator_2['gladiator_name'], gladiator_2['health'],
                  gladiator_2['rage'], gladiator_2['defense']))


def gladiator_makes_move(attacker, defender):
    while True:
        move = input('''{}... What would you like to do?
- attack
- pass
- quit
- heal
- defend
>>> '''.format(attacker['gladiator_name']))
        if 'attack' == move:
            attacker['defending'] = False
            return move
        elif 'pass' == move:
            return move
        elif 'quit' == move:
            print('{}: Survived!\n{}: Survived!'.format(
                defender['gladiator_name'], attacker['gladiator_name']))
            quit()
        elif 'heal' == move:
            attacker['defending'] = False
            return move
        elif 'defend' == move:
            attacker['defending'] = True
            return move
        elif 'supah kick' == move:  #Used to test death condititon
            return move
        elif 'angery' == move:  #Used to test critical hits
            return move
        else:
            print('Invalid input')


def gladiator_fight():  #add defend counter
    gladiator_1 = gladiator(input('Player 1... What is your name?'))
    gladiator_2 = gladiator(input('Player 2... What is your name?'))
    attacker, defender = gladiator_1, gladiator_2
    while True:
        show_gladiators(attacker, defender)
        gladiator_move = gladiator_makes_move(attacker, defender)
        core.defend_counter(attacker)
        if (attacker['defense'] - 1 < 0
                and not attacker['defending']) and attacker['stun_counter']:
            print(
                "All that defending's got you mighty tired.  (stunned for {} turns)".
                format(attacker['stun_counter']))
            attacker['stun_counter'] -= 1
            continue
        if gladiator_move == 'attack':
            core.attack(attacker, defender)
        elif gladiator_move == 'supah kick':  #negative  health test
            defender['health'] -= 99
        elif gladiator_move == 'angery':  #crit hit test
            attacker['rage'] += 100
            continue
        elif gladiator_move == 'heal':
            if attacker['rage'] < 10:
                print("You try to heal, but you just aren't angry enough")
            if attacker['health'] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious ones are found."
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
