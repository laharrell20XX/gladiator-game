import core


def gladiator(gladiator_name):
    gladiator = core.new_gladiator(gladiator_name, 100, 0, 5, 15)
    return gladiator


def show_gladiators(gladiator_1, gladiator_2):
    print('''
{}: {} HP ||| {} Rage
{}: {} HP ||| {} Rage'''
          .format(gladiator_1['gladiator_name'], gladiator_1['health'],
                  gladiator_1['rage'], gladiator_2['gladiator_name'],
                  gladiator_2['health'], gladiator_2['rage']))


def gladiator_makes_move(gladiator_name):
    while True:
        move = input('''{}... What would you like to do?
- attack
- pass
- quit
- heal
>>> '''.format(gladiator_name))
        if 'attack' == move:
            return move
        elif 'pass' == move:
            return move
        elif 'quit' == move:
            return move
        elif 'heal' == move:
            return move
        else:
            print('Invalid input')


def gladiator_fight():
    gladiator_1 = gladiator('Gladiator 1')
    gladiator_2 = gladiator('Gladiator 2')

    attacker, defender = gladiator_1, gladiator_2
    # while attacker['health'] and defender['health']:
    while True:
        show_gladiators(attacker, defender)
        gladiator1_move = gladiator_makes_move(attacker['gladiator_name'])
        if gladiator1_move == 'attack':
            core.attack(attacker, defender)
        elif gladiator1_move == 'heal':
            if attacker['rage'] < 10:
                print("You try to heal, but you just aren't angry enough")
                continue
            if attacker['health'] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
                )
            else:
                core.heal(attacker)
        elif gladiator1_move == 'quit':
            print('{}: Survived!\n{}: Survived!'.format(
                defender['gladiator_name'], attacker['gladiator_name']))
            break
        elif gladiator1_move == 'pass':
            pass
        if core.is_dead(defender):
            print(
                '{} has died. Funeral procession tommorrow... {} Wins!'.format(
                    defender['gladiator_name'], attacker['gladiator_name']))
            break
        attacker, defender = defender, attacker  #uses multivariable assignment to switch between attacker and defender at the end of every while loop

        # gladiator2_move = gladiator_makes_move(gladiator_2, 2)
        # if gladiator2_move == 'attack':
        #     core.attack(gladiator_2, gladiator_1)
        # elif gladiator2_move == 'heal':
        #     if gladiator_2['rage'] < 10:
        #         print("You try to heal, but you just aren't angry enough")
        #         continue
        #     elif gladiator_2['health'] == 100:
        #         print(
        #             "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
        #         )
        #         continue
        #     else:
        #         core.heal(gladiator_2)
        # elif gladiator1_move == 'quit':
        #     print('Gladiator 1: Survived!\nGladiator 2: Survived!')
        #     break
        # elif gladiator1_move == 'pass':
        #     pass
        # if core.is_dead(gladiator_1):
        #     print('Gladiator 2 has died. Funeral procession tommorrow')
        #     break


def main():
    gladiator_fight()


if __name__ == '__main__':
    main()
