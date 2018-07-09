import core


def gladiators():
    gladiator1 = new_gladiator(100, 0, 5, 15)
    gladiator2 = new_gladiator(100, 0, 5, 15)


def show_gladiators(gladiator1, gladiator2):
    print('''
Gladiator 1: {} HP ||| {} Rage
Gladiator 2: {} HP ||| {} Rage'''
          .format(gladiator1['health'], gladiator1['rage'],
                  gladiator2['health'], gladiator2['rage']))
