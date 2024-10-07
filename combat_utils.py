"""
Version 0.1

Author: Vít Pavelka
Date: 2024/10/07
"""
import math
import random


def calculate_hit_chance(attacker, defender):
    """
    Calculates the probability of a successful hit based on dexterity.

    :param attacker (Hero): The attacking Hero.
    :param defender (Hero): The defending Hero.
    :return (float): Probability of a successful hit (0 to 1).
    """
    base_hit_chance = 0.70
    dex_diff = attacker.dexterity - defender.dexterity

    adjustment = dex_diff * (0.03 if dex_diff > 0 else 0.02)
    attacker_hit_chance = base_hit_chance + adjustment

    return min(max(attacker_hit_chance, 0), 1)

def calculate_damage(attacker, attack_type):
    """
    Calculates the damage dealt by an attack based on type and hero attributes.

    :param attacker (Hero): The hero performing the attack.
    :param attack_type (Hero): The type of attack ('basic', 'medium', 'hard' -- should be extended in the future).
    :return (int): The amount of damage dealt (always rounded up).
    """
    base_damage = attacker.weapon.power_bonus

    power_factor = {"basic": 1 / 3, "medium": 2 / 3, "hard": 1.0}.get(attack_type, 1.0)

    stamina_ratio = max(attacker.stamina / 100, 0)
    if stamina_ratio != 0:
        damage_variation = random.uniform(stamina_ratio, 1.0) * attacker.power
    else:
        damage_variation = 0
    total_damage = (base_damage + damage_variation) * power_factor

    return max(math.ceil(total_damage), base_damage)