class Character:
    def __init__(self, name, health, basic_attack):
        # Private attri character state
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack

    # Getters
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_basic_attack(self):
        return self.__basic_attack

    # Setter for health only
    def set_health(self, health):
        # Health should never go below 0
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    # Reduce health by the damage amount
    def take_damage(self, damage_amount):
        self.set_health(self.__health - damage_amount)

    # Returns True if the character is still alive
    def is_alive(self):
        return self.__health > 0

    # Regular damage
    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())


class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana

    # Getter for mana
    def get_mana(self):
        return self.__mana

    # Setter for mana
    def set_mana(self, mana):
        if mana < 0:
            self.__mana = 0
        else:
            self.__mana = mana

    # Mage special attack: double damage for 10 mana
    # If not enough mana, deal regular damage
    def special_attack(self, target):
        if self.__mana >= 10:
            damage = self.get_basic_attack() * 2
            self.set_mana(self.__mana - 10)
            print(f"{self.get_name()} uses a magic blast for {damage} damage!")
        else:
            damage = self.get_basic_attack()
            print(f"{self.get_name()} nahh we dont have enough mana smh")
        target.take_damage(damage)


class Warrior(Character):
    def __init__(self, name, health, basic_attack, armour):
        super().__init__(name, health, basic_attack)
        self.__armour = armour

    # Getter for armour
    def get_armour(self):
        return self.__armour

    # Setter for armour
    def set_armour(self, armour):
        if armour < 0:
            self.__armour = 0
        else:
            self.__armour = armour

    # Warrior special attack: regular damage + 5 armour
    def special_attack(self, target):
        damage = self.get_basic_attack()
        target.take_damage(damage)
        self.set_armour(self.__armour + 5)
        print(f"{self.get_name()} uses strike for {damage} damage gains 5 armour!")


class Party:
    def __init__(self):
        # Private list for aggregated members
        self.__members = []

    # Add a Character object to the party
    def add_member(self, character):
        self.__members.append(character)

    def party_stats(self):
        print("\nParty Stats:")
        for member in self.__members:
            print(f"{member.get_name()} - Health: {member.get_health()}")

    def party_status(self):
        self.party_stats()


# Main program / test section

hero = Character("Batman", 50, 8)
monster = Character("Joker", 40, 6)

turn = 1

# Continue until one character is no longer alive
while hero.is_alive() and monster.is_alive():
    print(f"\nTurn {turn}")

    # Hero attacks first
    print(f"{hero.get_name()} attacks {monster.get_name()} for {hero.get_basic_attack()} damage.")
    monster.take_damage(hero.get_basic_attack())
    print(f"{monster.get_name()} health: {monster.get_health()}")

    # Monster attacks back only if still alive
    if monster.is_alive():
        print(f"{monster.get_name()} attacks {hero.get_name()} for {monster.get_basic_attack()} damage.")
        hero.take_damage(monster.get_basic_attack())
        print(f"{hero.get_name()} health: {hero.get_health()}")

    turn += 1

# Winner winner chicken dinner
if hero.is_alive():
    print(f"\nWinner: {hero.get_name()}")
else:
    print(f"\nWinner: {monster.get_name()}")


# polymorphism test 
mage = Mage("Merlin", 35, 7, 20)
warrior = Warrior("Conan", 45, 9, 10)

mage.special_attack(warrior)
print(f"{warrior.get_name()} health: {warrior.get_health()}")
print(f"{mage.get_name()} mana: {mage.get_mana()}")

warrior.special_attack(mage)
print(f"{mage.get_name()} health: {mage.get_health()}")
print(f"{warrior.get_name()} armour: {warrior.get_armour()}")


# HL aggregation test 
party = Party()

c1 = Character("Knight", 40, 6)
c2 = Mage("Gandalf", 30, 8, 25)
c3 = Warrior("Thor", 55, 10, 12)
c4 = Character("Archer", 28, 7)

party.add_member(c1)
party.add_member(c2)
party.add_member(c3)
party.add_member(c4)

party.party_stats()
