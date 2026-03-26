# SL SECTION

## 1. OOP class design and managing object state

A **class** is a blueprint for objects.
An **object** is an instance of a class.
**State** = the data stored in the object through attributes/fields.

### Good class design

A class should:

* represent one clear thing
* store relevant state
* provide methods to work with that state

### Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

### State example

For `BankAccount`, the object state is:

* `owner`
* `balance`

### Managing object state

You change state through methods:

```python
def deposit(self, amount):
    self.balance += amount
```

### Key idea

State belongs to the object, not to the whole program.



## 2. Encapsulation

**Encapsulation** means keeping data and behavior together inside the class, and controlling access to the data.

Instead of changing attributes directly everywhere:

```python
account.balance = -500
```

Use methods:

```python
def withdraw(self, amount):
    if amount <= self.balance:
        self.balance -= amount
```

### Why it matters

* protects object state
* prevents invalid values
* makes code easier to maintain

### Typical exam point

“Encapsulation” usually means:

* attributes are stored in the object
* methods control changes to those attributes



## 3. Methods

A **method** is a function inside a class.

### Types of methods

**Accessor / getter**
Returns information without changing state.

```python
def get_balance(self):
    return self.balance
```

**Mutator / setter**
Changes state.

```python
def set_owner(self, new_owner):
    self.owner = new_owner
```

**Action method**
Performs an action.

```python
def deposit(self, amount):
    self.balance += amount
```

### Important rule

Methods usually use `self` to access the current object’s data.



## 4. Instantiation

**Instantiation** = creating an object from a class.

```python
account1 = BankAccount("Ali", 1000)
```

* `BankAccount` = class
* `account1` = object / instance



## 5. Constructor

The constructor initializes the object’s starting state.

```python
def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
```

### Constructor purpose

* sets initial values
* ensures the object starts valid



## 6. Main loop

A **main loop** usually:

* creates objects
* shows a menu
* gets user input
* calls methods on objects

### Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)


account = BankAccount("Ali", 1000)

running = True
while running:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display()

    elif choice == "4":
        running = False

    else:
        print("Invalid option")
```

### What examiners look for

* object created correctly
* loop works
* method calls are used
* state changes properly



## 7. Naming conventions

Use clear, consistent names.

### Common conventions

**Classes:** PascalCase

```python
BankAccount
StudentRecord
GameCharacter
```

**Variables and functions/methods:** snake_case

```python
total_score
deposit_money()
get_balance()
```

### Good names

* `student_name`
* `current_balance`
* `calculate_total()`

### Bad names

* `x`
* `stuff`
* `doThing()`



## 8. Comments

Comments should explain **why** or clarify logic, not repeat obvious code.

### Good

```python
# Prevent balance from going below zero
if amount <= self.balance:
```

### Bad

```python
# Add amount to balance
self.balance += amount
```

### Best practice

Use comments:

* before tricky logic
* for sections of program
* for menu/main loop steps



# HL SECTION

HL includes all SL topics plus these:

## 9. Inheritance

**Inheritance** lets one class reuse another class’s attributes and methods.

### Parent/superclass

General class.

### Child/subclass

More specific class.

### Example

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

### Key idea

`Dog` inherits from `Animal`.

Benefits:

* code reuse
* better organization
* models “is-a” relationships

`Dog` **is an** `Animal`



## 10. Polymorphism

**Polymorphism** means different classes can respond to the same method name in different ways.

### Example

```python
class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Woof")
```

Now:

```python
animals = [Cat("Milo"), Dog("Max")]

for a in animals:
    a.speak()
```

Output differs depending on object type.

### Key idea

Same method call:

```python
a.speak()
```

Different behavior for different objects.



## 11. Aggregation and composition

These describe “has-a” relationships.



### Aggregation

One object uses another object, but they can exist separately.

Example:
A `Team` has `Player` objects, but players can exist without the team.

```python
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)
```

### Key idea

`Team` has `Player` objects.



### Composition

A stronger relationship: one object owns another object, and the contained object usually does not exist independently.

Example:
A `House` has `Room` objects.

```python
class Room:
    def __init__(self, room_name):
        self.room_name = room_name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom")]
```

### Key idea

The rooms are created as part of the house.



# Fast definitions you can memorize

## Class

Blueprint for creating objects.

## Object

An instance of a class.

## Attribute / field

A variable stored in an object.

## State

The current values of an object’s attributes.

## Method

A function inside a class.

## Constructor

A special method that initializes object state.

## Encapsulation

Keeping data and methods together and controlling access to data.

## Inheritance

A subclass gets properties and methods from a parent class.

## Polymorphism

Different classes use the same method name with different behavior.

## Aggregation

A class contains references to other existing objects.

## Composition

A class owns and creates other objects as part of itself.



# Common exam sentence starters

These are useful in written answers:

* “This class models…”
* “The object state is stored in the attributes…”
* “Encapsulation is achieved by using methods to control access to attributes…”
* “This method mutates the object state by changing…”
* “An object is instantiated when…”
* “Inheritance allows the subclass to reuse…”
* “Polymorphism occurs because the same method call produces different behavior…”
* “This is aggregation because the contained objects can exist independently.”
* “This is composition because the contained objects are created and owned by the parent object.”



# Mini templates

## Basic class template

```python
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method_name(self):
        pass
```

## Encapsulated class template

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score

    def get_score(self):
        return self.score
```

## Inheritance template

```python
class Parent:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("Parent action")


class Child(Parent):
    def action(self):
        print("Child action")
```

## Aggregation template

```python
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
```



# What to check before submitting code

Make sure your program has:

* at least one well-designed class
* meaningful attributes for object state
* methods that use and update the state correctly
* proper object instantiation
* a working main loop if required
* good variable, method, and class names
* comments in sensible places
* for HL: inheritance, polymorphism, and aggregation/composition used correctly



# Very common mistakes

Avoid these:

* forgetting `self`
* changing attributes without using methods when encapsulation is expected
* poor class names like `myclass`
* putting all logic in the main loop instead of the class
* inheritance without actually reusing behavior
* saying aggregation when it is really composition
* comments that just repeat code
* not validating input before changing object state



**SL**

* Class = blueprint
* Object = instance
* State = attributes
* Methods work on state
* Encapsulation = controlled access through methods
* Instantiation = create object
* Main loop = menu + method calls
* Use good names and sensible comments

**HL**

* Inheritance = subclass gets features from parent
* Polymorphism = same method, different behavior
* Aggregation/composition = one object contains others
