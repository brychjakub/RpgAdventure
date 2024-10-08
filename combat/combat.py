"""
Version 0.1

Author: Vít Pavelka
Date: 2024/10/07
"""
import random
from characters.hero import Hero
from utils.combat_utils import calculate_hit_chance, calculate_damage

class Combat:
    """
    Represents a combat encounter between two heroes.

    Attributes:
        player1 (Hero): The first participant in the combat.
        player2 (Hero): The second participant in the combat.
    """

    def __init__(self, player1, player2):
        """
        Initializes a combat encounter between two heroes.

        :param player1 (Hero): The first participant.
        :param player2 (Hero): The second participant.
        """
        self.player1 = player1
        self.player2 = player2

    def determine_initiative(self):
        """
        Randomly (for now) selects which hero will start the combat.
        :return (Hero): The hero who starts the combat.
        """
        return random.choice([self.player1, self.player2])

    def conduct_turn(self, attacker, defender, attack_type: str):
        """
        Executes a turn of combat between attacker and defender.

        :param attacker (Hero): The hero attacking in this turn.
        :param defender (Hero): The hero defending in this turn.
        :param attack_type (str): The type of attack being executed.
        :return (str): A description of the outcome of the attack.
        """
        stamina_cost = attacker.attack_cost(attack_type)

        hit_chance = calculate_hit_chance(attacker, defender)
        if random.random() <= hit_chance:
            damage = calculate_damage(attacker, attack_type)
            defender.hp -= damage
            attacker.stamina -= stamina_cost
            attacker.stamina = max(attacker.stamina, 0)
            return f"{attacker.name} ({attacker.hp}hp, {attacker.stamina}sp) successfully hits {defender.name} with {attack_type} strike for {damage} damage!"
        else:
            attacker.stamina -= stamina_cost
            attacker.stamina = max(attacker.stamina, 0)
            return f"{attacker.name}'s ({attacker.hp}hp, {attacker.stamina}sp) attack missed!"

    def battle(self):
        """
        Manages the full combat sequence until one hero loses all HP (dies).
        """
        current_attacker = self.determine_initiative()
        current_defender = self.player2 if current_attacker == self.player1 else self.player1

        while self.player1.hp > 0 and self.player2.hp > 0:
            if isinstance(current_attacker, Hero) and current_attacker == self.player1:
                print("\n" + 10 * '--')
                print(f"{current_attacker.name}'s turn! Choose your attack!")
                print("1. Basic (5 stamina)")
                print("2. Medium (10 stamina)")
                print("3. Hard (15 stamina)")

                choice = input("\nChoose your attack [1, 2, or 3]: ").strip()
                while choice not in ["1", "2", "3"]:
                    print("Invalid choice! Please enter 1, 2, or 3.")
                    choice = input("Choose your attack [1, 2, or 3]: ").strip()

                attack_type = {"1": "basic", "2": "medium", "3": "hard"}[choice]

            else:
                print("\n" + 10 * '--')
                print(f"{current_attacker.name}'s turn! Choose your attack!")
                print("1. Basic (5 stamina)")
                print("2. Medium (10 stamina)")
                print("3. Hard (15 stamina)")

                choice = input("\nChoose your attack [1, 2, or 3]: ").strip()
                while choice not in ["1", "2", "3"]:
                    print("Invalid choice! Please enter 1, 2, or 3.")
                    choice = input("Choose your attack [1, 2, or 3]: ").strip()

                attack_type = {"1": "basic", "2": "medium", "3": "hard"}[choice]
                # AI decision (random so far)
                # attack_type = random.choice(["basic", "medium", "hard"])
                #

            print(self.conduct_turn(current_attacker, current_defender, attack_type))

            # Switch turns
            current_attacker, current_defender = current_defender, current_attacker

        if self.player1.hp <= 0:
            print(f"{self.player2.name} wins with {self.player2.hp} hp left!")
        else:
            print(f"{self.player1.name} wins with {self.player1.hp} hp left!")
