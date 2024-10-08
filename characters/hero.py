"""
Version 0.1

Author: Vít Pavelka
Date: 2024/10/07
"""

import random

class Hero:
    """
    Represents a hero character in the game with core attributes and abilities.

    Attributes:
        name (str): The name of the Hero.
        power (int): The strength of the hero which affects attack damage.
        stamina (int): The Hero's energy for attacks; regenerates after combat.
        max_stamina (int): The maximum possible stamina the Hero can have.
        hp (int): Current health points of the hero.
        max_hp (int): Maximum possible health points.
        dexterity (int): Determines agility and influences hit/miss chance.
        weapon (Weapon): The weapon the hero is currently equipped with.
    """
    def __init__(self, name: str, power: int, stamina: int, hp: int, dexterity: int):
        """
        Initializes a new hero with base attributes.

        :param name (str): Name of the Hero.
        :param power (int): The power attribute which affects damage dealt.
        :param stamina (int): Initial stamina points for combat.
        :param hp (int): Health points indicating hero's health state.
        :param dexterity (int): Dexterity level affecting hit/miss probabilities.
        """
        self.name = name
        self.power = power
        self.stamina = stamina
        self.max_stamina = stamina
        self.hp = hp
        self.max_hp = hp
        self.dexterity = dexterity
        self.weapon = None

    def equip_weapon(self, weapon):
        """
        Assigns a weapon to the Hero.

        :param weapon (Weapon): The weapon to be equipped.
        """
        self.weapon = weapon

    def attack_cost(self, attack_type: str):
        """
        Calculates the stamina cost for a given type of attack.

        :param attack_type (str): The type of attack ('basic', 'medium', 'hard' -- should be extended in the future)
        :return (int): The stamina cost associated with the attack type.
        """
        attack_cost = {
            'basic': 5,
            'medium': 10,
            'hard': 15
        }
        return attack_cost.get(attack_type, 0)

    def perform_attack(self, attack_type: str):
        """
        Executes an attack, deducting stamina based on attack type.

        :param attack_type (str): The type of attack being performed.
        :return (int): The stamina cost used for the attack.
        """
        stamina_cost = self.attack_cost(attack_type)
        self.stamina -= stamina_cost
        return stamina_cost