from core import *
from mypy_extensions import TypedDict
from bcca.test import fake_file


@fake_file({'example.txt': 'this text is in example.txt'})
def test_fake_file_test():
    with open('example.txt') as f:
        assert f.read() == 'this text is in example.txt'


def test_new_gladiator():
    assert new_gladiator('Bill', 100, 0, 5, 15, False, 3, 3, '', 15) == {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15,
        'defending': False,
        'defense': 3,
        'stunned_turns': 3,
        'stunned_status': '',
        'miss_chance': 15
    }


def test_attack():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 0,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'miss_chance': 0
    }
    defender = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 0,
        'damage_low': 2,
        'damage_high': 20,
        'defending': False
    }
    attack(attacker, defender)
    assert defender['health'] == 85


def test_attack_low_health():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 0,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'miss_chance': 0
    }
    defender = {
        'gladiator_name': 'Bill',
        'health': 2,
        'rage': 0,
        'damage_low': 2,
        'damage_high': 20,
        'defending': False
    }
    attack(attacker, defender)
    assert defender['health'] == 0


def test_attack_crit():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 100,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'miss_chance': 0
    }
    defender = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 15,
        'damage_low': 2,
        'damage_high': 20,
        'defending': False
    }
    attack(attacker, defender)
    assert defender['health'] == 70
    assert attacker['rage'] == 0


def test_attack_miss():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 100,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'miss_chance': 100
    }
    defender = {
        'gladiator_name': 'Logan',
        'health': 100,
        'rage': 15,
        'damage_low': 2,
        'damage_high': 20,
        'defending': False
    }
    attack(attacker, defender)
    assert defender['health'] == 100
    assert attacker['rage'] == 0


def test_heal():
    gladiator = {
        'gladiator_name': 'Bill',
        'health': 80,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15,
        'defending': False
    }
    heal(gladiator)
    assert gladiator['health'] == 85
    assert gladiator['rage'] == 90


def test_defend():
    attacker = {
        'health': 81,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15,
        'defending': False,
        'defense': 3
    }
    damage_dealt = defend(attacker, 11)
    assert attacker['defending'] == False
    assert damage_dealt == 2.75


def test_defend_low_defense():
    attacker = {
        'health': 81,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15,
        'defending': True,
        'defense': 1
    }
    damage_dealt = defend(attacker, 11)
    assert attacker['defending'] == True
    assert damage_dealt == 8.25


def test_attack_w_defense():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 0,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'defense': 3,
        'miss_chance': 0
    }
    defender = {
        'gladiator_name': 'Bob',
        'health': 100,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15,
        'defending': True,
        'defense': 3
    }
    attack(attacker, defender)
    assert defender['defending'] == True
    assert defender['health'] == 96.25
    assert attacker['rage'] == 0
    assert defender['defense'] == 2


def test_crit_w_low_defense():
    attacker = {
        'gladiator_name': 'Bill',
        'health': 100,
        'rage': 100,
        'damage_low': 15,
        'damage_high': 15,
        'defending': False,
        'defense': 3,
        'miss_chance': 0
    }
    defender = {
        'gladiator_name': 'Bob',
        'health': 100,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15,
        'defending': True,
        'defense': 1
    }
    attack(attacker, defender)
    assert defender['health'] == 77.5
    assert defender['defense'] == -1
    assert attacker['rage'] == 0


def test_defend_counter_full_blocking():
    defender = {'defending': 'blocking', 'defense': 3, 'stunned_turns': 3}
    defend_counter(defender)
    assert defender['defense'] == 3
    assert defender['stunned_turns'] == 3
    assert defender['defending'] == 'blocking'


def test_defend_counter_not_blocking():
    defender = {'defending': '', 'defense': 3, 'stunned_turns': 3}
    defend_counter(defender)
    assert defender['defense'] == 3
    assert defender['stunned_turns'] == 3


def test_defend_counter_overblock():
    defender = {
        'gladiator_name': 'bill',
        'defending': 'blocking',
        'defense': -1,
        'stunned_turns': 3
    }
    defend_counter(defender)
    assert defender['defense'] == -1
    assert defender['defending'] == ''
    assert defender['stunned_status'] == '(stunned)'


def test_defend_counter_overblock_stun_over():
    defender = {'defending': '', 'defense': -2, 'stunned_turns': 0}
    defend_counter(defender)
    assert defender['defending'] == ''
    assert defender['defense'] == 0
    assert defender['stunned_turns'] == 2
