import core


def gladiator1():
    gladiator1 = new_gladiator(100, 0, 5, 15)
    return gladiator1


def gladiator2():
    gladiator2 = new_gladiator(100, 0, 5, 15)
    return gladiator2


def show_gladiators(gladiator1, gladiator2):
    print('''
Gladiator 1: {} HP ||| {} Rage
Gladiator 2: {} HP ||| {} Rage'''
          .format(gladiator1['health'], gladiator1['rage'],
                  gladiator2['health'], gladiator2['rage']))


def gladiator_makes_move(gladiator, number):
    while True:
        move = input('''Gladiator {}... What would you like to do?
- attack
- pass
- quit
- heal
>>> '''.format(number))
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
    gladiator1 = gladiator1()
    gladiator2 = gladiator2()
    while True:
        show_gladiators(gladiator1, gladiator2)
        gladiator1_move = gladiator_makes_move(gladiator1, 1)
        if gladiator1_move == 'attack':
            attack(gladiator1, gladiator2)
        elif gladiator1_move == 'heal':
            if gladiator1[rage] < 10:
                print('Not enough rage to heal.')
                continue
            elif gladiator1[health] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
                )
                continue
            else:
                heal(gladiator1)
        elif gladiator1_move == 'quit':
            break
        elif gladiator1_move == 'pass':
            pass
