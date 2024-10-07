"""
Version 0.1

Author: Vít Pavelka
Date: 2024/10/07
"""

class Weapon:
    """
    Represents a weapon in the game, affecting the hero's attack capabilities.

    Attributes:
        name (str): The name of the weapon.
        power_bonus (int): The additional power given to the hero's attacks.
        dexterity_bonus (int): Additional dexterity granted to the hero (default is 0).
    """

    def __init__(self, name: str, power_bonus: int, dexterity_bonus: int = 0):
        """
        Initializes a base weapon with bonuses.

        :param name (str): The name of the weapon.
        :param power_bonus (int): Power boost provided by the weapon.
        :param dexterity_bonus (int, optional): Dexterity boost provided by the weapon (default is 0)
        """
        self.name = name
        self.power_bonus = power_bonus
        self.dexterity_bonus = dexterity_bonus

class Axe(Weapon):
    """
    Represents an Axe with level-dependent power bonuses.
    """
    def __init__(self, level: int):
        """
        Initializes an Axe with bonuses based on its level.

        :param level (int): The level of the axe (1-?) affecting power bonus.
        """
        power_bonus = level * 3
        super().__init__(f"Axe (Level {level})", power_bonus)

class Spear(Weapon):
    """
    Represents a Spear with level-dependent power and dexterity bonuses.
    """
    def __init__(self, level: int):
        """
        Initializes a Spear with level-based bonuses.

        :param level (int): The level of the spear (1-?), affecting power and dexterity bonuses.
        """
        power_bonus = level * 1
        dexterity_bonus = level * 2
        super().__init__(f"Spear (Level {level})", power_bonus, dexterity_bonus)

class Sword(Weapon):
    """
    Represents a Sword with level-dependent power bonuses.
    """
    def __init__(self, level: int):
        """
        Initializes a Sword with bonuses based on its level.
        :param level (int):  The level of the sword (1-?), affecting power bonus.
        """
        power_bonus = level * 2
        super().__init__(f"Sword (Level {level})", power_bonus)
