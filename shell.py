import core
from random import randint, choice


def gladiator(gladiator_name, weapon):
    gladiator = core.new_gladiator(gladiator_name, 100, 0,
                                   weapon['damage_low'], weapon['damage_high'],
                                   '', 3, 2, '', 15, weapon['weapon_name'])
    return gladiator


def weapon_inventory():
    sword = core.weapon('sword', 4, 15, 20)
    bow_staff = core.weapon('bo staff', 2, 11, 10)
    war_hammer = core.weapon('war_hammer', 3, 18, 30)
    mace = core.weapon('mace', 3, 14, 15)
    bat = core.weapon('bat', 2, 13, 13)
    return sword, bow_staff, war_hammer, mace, bat


def show_weapons(weapons):
    for weapon in weapons:
        print(
            '\n{}: lowest damage {}, highest damage {}, miss chance {}'.format(
                weapon['weapon_name'].capitalize(), weapon['damage_low'],
                weapon['damage_high'], weapon['miss_chance']))


def choose_weapon(weapons):
    while True:
        show_weapons(weapons)
        weapon_choice = input('\nGladiator, choose your weapon...')
        for weapon in weapons:
            if weapon['weapon_name'] == weapon_choice:
                return weapon_choice
        print('That weapon is currently not in stock')


def greeting(player):
    gladiator_name = input('Greetings {}, what is your name?'.format(player))
    return gladiator_name


def show_gladiators(gladiator_1, gladiator_2):
    print('''
{}: {} HP ||| {} Rage ||| {} shield durability {} {}

{}: {} HP ||| {} Rage ||| {} shield durability {} {}'''.format(
        gladiator_1['gladiator_name'],
        gladiator_1['health'], gladiator_1['rage'],
        max(gladiator_1['defense'], 0), gladiator_1['defending'],
        gladiator_1['stunned_status'], gladiator_2['gladiator_name'],
        gladiator_2['health'], gladiator_2['rage'],
        max(gladiator_2['defense'],
            0), gladiator_2['defending'], gladiator_2['stunned_status']))


def gladiator_makes_move(attacker, defender):
    while True:
        move = input('''{}... What would you like to do?
- [a]ttack
- [p]ass
- [q]uit
- [h]eal
- [d]efend
>>> '''.format(attacker['gladiator_name'])).lower()
        if 'a' == move:
            attacker['defending'] = ''
            return move
        elif 'p' == move:
            return move
        elif 'q' == move:
            print('{}: Survived!\n{}: Survived!'.format(
                defender['gladiator_name'], attacker['gladiator_name']))
            quit()
        elif 'h' == move:
            attacker['defending'] = ''
            return move
        elif 'd' == move:
            attacker['defending'] = 'blocking'
            return move
        elif 'supah kick' == move:  #Used to test death condititon
            return move
        elif 'angery' == move:  #Used to test critical hits
            return move
        else:
            print('Invalid input')


def gladiator_turn(attacker, defender):
    while True:
        core.defend_counter(attacker)
        if attacker['stunned_status']:
            if attacker['stunned_turns'] == 0:
                show_gladiators(attacker, defender)
                attacker['stunned_status'] = ''
                continue
            else:
                print("{} is stunned for {} turns)".format(
                    attacker['gladiator_name'], attacker['stunned_turns']))
                attacker['stunned_turns'] -= 1
                pass
        else:
            show_gladiators(attacker, defender)
            gladiator_move = gladiator_makes_move(attacker, defender)
            if gladiator_move == 'a':
                core.attack(attacker, defender)
            elif gladiator_move == 'supah kick':  #negative  health test
                defender['health'] -= 99
            elif gladiator_move == 'angery':  #crit hit test
                attacker['rage'] += 100
                continue
            elif gladiator_move == 'h':
                if attacker['rage'] < 10:
                    print("You try to heal, but you just aren't angry enough")
                elif attacker['health'] == 100:
                    print(
                        "You spend some time searching for wounds to self-treat, but no serious ones are found."
                    )
                else:
                    core.heal(attacker)
            elif gladiator_move == 'p':
                pass
            if core.is_dead(defender):
                print('{} has died. Funeral procession tommorrow... {} Wins!'.
                      format(defender['gladiator_name'],
                             attacker['gladiator_name']))
                break
        defender, attacker = attacker, defender


def gladiator_fight():  #add defend counter
    available_weapons = weapon_inventory()
    gladiator_1_name = greeting('Player 1')
    gladiator_1_weapon = choose_weapon(available_weapons)
    gladiator_1 = gladiator(gladiator_1_name, gladiator_1_weapon)
    gladiator_2_name = greeting('Player 2')
    gladiator_2_weapon = choose_weapon(available)
    gladiator_2 = (gladiator_2_name, gladiator_2_weapon)
    attacker, defender = gladiator_1, gladiator_2
    available_weapons = weapon_inventory()
    gladiator_turn(attacker, defender)


def main():
    gladiator_fight()


if __name__ == '__main__':
    main()
