from core import *


def test_new_gladiator():
    assert new_gladiator(100, 0, 5, 15) == {
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }


def test_attack():
    assert attack({
        'health': 100,
        'rage': 15,
        'damage_low': 5,
        'damage_high': 15
    }, {
        'health': 100,
        'rage': 15,
        'damage_low': 2,
        'damage_high': 20
    }) == None


def test_attack_low_health():
    assert attack({
        'health': 100,
        'rage': 15,
        'damage_low': 5,
        'damage_high': 15
    }, {
        'health': 2,
        'rage': 15,
        'damage_low': 2,
        'damage_high': 20
    }) == None


def test_attack_low_health_crit():
    assert attack({
        'health': 100,
        'rage': 100,
        'damage_low': 5,
        'damage_high': 15
    }, {
        'health': 2,
        'rage': 15,
        'damage_low': 2,
        'damage_high': 20
    }) == None
