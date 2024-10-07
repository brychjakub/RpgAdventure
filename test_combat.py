from characters.hero import Hero
from weapons.weapons import Axe, Spear
from combat.combat import Combat

hero1 = Hero("BOMBAman", power=10, stamina=50, hp=50, dexterity=4)
hero2 = Hero("Dr. Pavelka, Ph.D.", power=8, stamina=50, hp=50, dexterity=6)

hero1.equip_weapon(Axe(level=2))
hero2.equip_weapon(Spear(level=2))

battle = Combat(hero1, hero2)
battle.battle()