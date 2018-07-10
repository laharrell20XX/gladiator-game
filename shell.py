import core


def gladiator1():
    gladiator1 = core.new_gladiator(100, 0, 5, 15)
    return gladiator1


def gladiator2():
    gladiator2 = core.new_gladiator(100, 0, 5, 15)
    return gladiator2


def show_gladiators(gladiator_1, gladiator_2):
    print('''
Gladiator 1: {} HP ||| {} Rage
Gladiator 2: {} HP ||| {} Rage'''
          .format(gladiator_1['health'], gladiator_1['rage'],
                  gladiator_2['health'], gladiator_2['rage']))


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
    gladiator_1 = gladiator1()
    gladiator_2 = gladiator2()
    while True:
        show_gladiators(gladiator_1, gladiator_2)
        gladiator1_move = gladiator_makes_move(gladiator_1, 1)
        if gladiator1_move == 'attack':
            core.attack(gladiator_1, gladiator_2)
        elif gladiator1_move == 'heal':
            if gladiator_1['rage'] < 10:
                print("You try to heal, but you just aren't angry enough")
                continue
            if gladiator_1['health'] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
                )
            else:
                core.heal(gladiator_1)
        elif gladiator1_move == 'quit':
            print('Gladiator 1: Survived!\nGladiator 2: Survived!')
            break
        elif gladiator1_move == 'pass':
            pass
        if core.is_dead(gladiator_2):
            print('Gladiator 2 has died. Funeral procession tommorrow')
            break
        show_gladiators(gladiator_1, gladiator_2)
        gladiator2_move = gladiator_makes_move(gladiator_2, 2)
        if gladiator2_move == 'attack':
            core.attack(gladiator_2, gladiator_1)
        elif gladiator2_move == 'heal':
            if gladiator_2['rage'] < 10:
                print("You try to heal, but you just aren't angry enough")
                continue
            elif gladiator_2['health'] == 100:
                print(
                    "You spend some time searching for wounds to self-treat, but no serious one's are found (Turn used up)"
                )
                continue
            else:
                core.heal(gladiator_2)
        elif gladiator1_move == 'quit':
            print('Gladiator 1: Survived!\nGladiator 2: Survived!')
            break
        elif gladiator1_move == 'pass':
            pass
        if core.is_dead(gladiator_1):
            print('Gladiator 2 has died. Funeral procession tommorrow')
            break


def main():
    gladiator_fight()


if __name__ == '__main__':
    main()
