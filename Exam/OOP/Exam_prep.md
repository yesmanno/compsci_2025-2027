## Python naming rules

Use these consistently:

```python
class Character:        # Class = PascalCase
def take_damage(self):  # Methods/functions = snake_case
basic_attack = 10       # Variables/attributes = snake_case
```

# Core OOP ideas you need

## Class

A blueprint for making objects.

```python
class Character:
    pass
```

## Object / instance

An object created from a class.

```python
hero = Character()
```

## Attributes

Variables stored inside an object.

```python
self.__name = name
self.__health = health
self.__basic_attack = basic_attack
```

## State

The current values of an object’s attributes.

Example:

* name = `"Batman"`
* health = `50`
* basic_attack = `8`

That is the object’s **state**.



# Encapsulation in Python

Your task says **private attributes**.

In Python, private attributes are usually written with **double underscore**:

```python
self.__name
self.__health
self.__basic_attack
```

This is what your teacher likely wants for “private”.

### Why use getters/setters?

Because object data should be controlled through methods.



# SL SECTION

## Character class template

```python
class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack
```



## Getters

Getters return private attributes.

```python
    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_basic_attack(self):
        return self.__basic_attack
```

### Why needed?

Because `__name`, `__health`, etc. are private, so outside code should use methods to access them.



## Setter for health

Only health changes during gameplay.

```python
    def set_health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health
```

### Important exam point

Health must **never go below 0**.



## take_damage(damage_amount)

Subtract damage from health.

```python
    def take_damage(self, damage_amount):
        self.set_health(self.__health - damage_amount)
```

### Why this is good

It uses the setter, so health is still protected from going negative.



## is_alive()

Returns `True` if health > 0, otherwise `False`.

```python
    def is_alive(self):
        return self.__health > 0
```



## Full SL Character class

```python
class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_basic_attack(self):
        return self.__basic_attack

    def set_health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    def take_damage(self, damage_amount):
        self.set_health(self.__health - damage_amount)

    def is_alive(self):
        return self.__health > 0
```



# Instantiation

Create objects from the class.

```python
hero = Character("Batman", 50, 8)
monster = Character("Joker", 40, 6)
```



# Main battle loop

This is the **instantiation + main loop** part.

```python
hero = Character("Batman", 50, 8)
monster = Character("Joker", 40, 6)

turn = 1

while hero.is_alive() and monster.is_alive():
    print(f" Turn {turn} ")

    monster.take_damage(hero.get_basic_attack())
    print(monster.get_name(), "health:", monster.get_health())

    if monster.is_alive():
        hero.take_damage(monster.get_basic_attack())
        print(hero.get_name(), "health:", hero.get_health())

    turn += 1

if hero.is_alive():
    print(hero.get_name(), "wins!")
else:
    print(monster.get_name(), "wins!")
```

### What this shows

* objects created correctly
* methods used properly
* object state updated each turn
* loop stops when one dies



# SL comments you can use

Use comments where logic needs explaining.

```python
# Set health to 0 if damage would make it negative
# Continue battle while both characters are alive
# Monster only attacks back if still alive
```

Do not over-comment obvious lines.



# HL SECTION

HL includes everything above plus:

* inheritance
* polymorphism
* aggregation



# Inheritance

## Mage subclass

Mage inherits from Character.

```python
class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana
```

### Why use `super()`?

It reuses the constructor from `Character`.



## Warrior subclass

```python
class Warrior(Character):
    def __init__(self, name, health, basic_attack, armour):
        super().__init__(name, health, basic_attack)
        self.__armour = armour
```



# Add special_attack() to Character

Base version just deals regular damage.

```python
    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())
```

Add this inside `Character`.



# Full HL-ready Character class

```python
class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_basic_attack(self):
        return self.__basic_attack

    def set_health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    def take_damage(self, damage_amount):
        self.set_health(self.__health - damage_amount)

    def is_alive(self):
        return self.__health > 0

    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())
```



# Polymorphism

Same method name, different behavior.

All classes have:

```python
special_attack(target)
```

But each class behaves differently.



## Mage special_attack()

Rules:

* deal **double damage**
* costs **10 mana**
* if not enough mana, do regular damage

```python
class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if mana < 0:
            self.__mana = 0
        else:
            self.__mana = mana

    def special_attack(self, target):
        if self.__mana >= 10:
            target.take_damage(self.get_basic_attack() * 2)
            self.set_mana(self.__mana - 10)
        else:
            target.take_damage(self.get_basic_attack())
```



## Warrior special_attack()

Rules:

* deal regular damage
* gain +5 armour

```python
class Warrior(Character):
    def __init__(self, name, health, basic_attack, armour):
        super().__init__(name, health, basic_attack)
        self.__armour = armour

    def get_armour(self):
        return self.__armour

    def set_armour(self, armour):
        if armour < 0:
            self.__armour = 0
        else:
            self.__armour = armour

    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())
        self.set_armour(self.__armour + 5)
```



# Important note about armour

Your task only says:

> add 5 armour on cast

It does **not** say armour reduces damage.
So unless your teacher tells you otherwise, armour is just tracked as state.



# Aggregation: Party class

A `Party` contains character objects.

That is **aggregation** because the characters can exist without the party.

## Party class

```python
class Party:
    def __init__(self):
        self.__members = []

    def add_member(self, character):
        self.__members.append(character)

    def party_stats(self):
        for member in self.__members:
            print(member.get_name(), "-", member.get_health())
```



# Why this is aggregation

Because the `Character`, `Mage`, and `Warrior` objects are created independently and then added to the party.



# Instantiate Party and test it

```python
party = Party()

c1 = Character("Knight", 40, 7)
c2 = Mage("Merlin", 35, 6, 30)
c3 = Warrior("Conan", 50, 8, 10)

party.add_member(c1)
party.add_member(c2)
party.add_member(c3)

party.party_stats()
```



# Full HL example in one place

This is the kind of structure you should be able to write in the test.

```python
class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_basic_attack(self):
        return self.__basic_attack

    def set_health(self, health):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health

    def take_damage(self, damage_amount):
        self.set_health(self.__health - damage_amount)

    def is_alive(self):
        return self.__health > 0

    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())


class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        if mana < 0:
            self.__mana = 0
        else:
            self.__mana = mana

    def special_attack(self, target):
        if self.__mana >= 10:
            target.take_damage(self.get_basic_attack() * 2)
            self.set_mana(self.__mana - 10)
        else:
            target.take_damage(self.get_basic_attack())


class Warrior(Character):
    def __init__(self, name, health, basic_attack, armour):
        super().__init__(name, health, basic_attack)
        self.__armour = armour

    def get_armour(self):
        return self.__armour

    def set_armour(self, armour):
        if armour < 0:
            self.__armour = 0
        else:
            self.__armour = armour

    def special_attack(self, target):
        target.take_damage(self.get_basic_attack())
        self.set_armour(self.__armour + 5)


class Party:
    def __init__(self):
        self.__members = []

    def add_member(self, character):
        self.__members.append(character)

    def party_stats(self):
        for member in self.__members:
            print(member.get_name(), "-", member.get_health())
```



# Battle loop with subclasses

You may also be asked to use special attacks.

```python
hero = Mage("Gandalf", 40, 7, 20)
enemy = Warrior("Orc", 50, 6, 5)

turn = 1

while hero.is_alive() and enemy.is_alive():
    print(f" Turn {turn} ")

    hero.special_attack(enemy)
    print(enemy.get_name(), "health:", enemy.get_health())

    if enemy.is_alive():
        enemy.special_attack(hero)
        print(hero.get_name(), "health:", hero.get_health())

    turn += 1

if hero.is_alive():
    print(hero.get_name(), "wins!")
else:
    print(enemy.get_name(), "wins!")
```



# Exam definitions you can memorize

## Encapsulation

Keeping attributes private and using methods to access/change them.

## Inheritance

A subclass reuses the attributes and methods of a parent class.

## Polymorphism

Different classes use the same method name but perform different actions.

## Aggregation

A class stores objects that can also exist independently.



# Very likely mistakes to avoid

## 1. Forgetting `self`

Wrong:

```python
def get_name():
    return __name
```

Correct:

```python
def get_name(self):
    return self.__name
```



## 2. Accessing private attributes directly outside the class

Wrong:

```python
print(hero.__health)
```

Correct:

```python
print(hero.get_health())
```



## 3. Letting health go below 0

Wrong:

```python
self.__health -= damage_amount
```

Better:

```python
self.set_health(self.__health - damage_amount)
```



## 4. Forgetting `super().__init__()` in subclasses

Wrong:

```python
class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        self.__mana = mana
```

Correct:

```python
class Mage(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana
```



## 5. Mixing up `party_stats()` and `party_status()`

Your task says both:

* `party_stats()`
* `party_status()`

That looks like a typo in the task sheet.
Use **one consistent method name**, probably `party_stats()` since that is the one actually defined earlier.



# Best comment placements

Use comments like this:

```python
# Reduce health but never below 0
# Mage uses 10 mana to deal double damage
# Keep battling while both characters are alive
```



# 1-minute cram version

## SL

* Make `Character` class
* Private attrs: `__name`, `__health`, `__basic_attack`
* Getters for all
* Setter only for health
* `take_damage()` reduces health
* `is_alive()` returns `True` if health > 0
* Instantiate 2 objects
* Use a battle loop
* Print winner

## HL

* `Mage(Character)` with `__mana`
* `Warrior(Character)` with `__armour`
* Add `special_attack(target)` in `Character`
* Override it in subclasses
* Mage: double damage, costs 10 mana
* Warrior: regular damage + 5 armour
* `Party` class with `__members`
* `add_member(character)`
* `party_stats()`


# Sentence starters for written explanations

* “The object state is stored in private attributes.”
* “Encapsulation is shown by using getters and a setter to control access to data.”
* “Inheritance is used because Mage and Warrior extend Character.”
* “Polymorphism is shown by overriding `special_attack()` in different subclasses.”
* “Party uses aggregation because it stores Character objects that can exist independently.”



