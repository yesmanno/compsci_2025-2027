#parent 
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def info(self) -> str:
        return f"Animal(name={self.name})"
#sub
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)     
        self.breed = breed          # new attribute 

    def speak(self) -> str:
        return "Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}."

a = Animal("Mystery")
d = Dog("Buddy", "Labrador")

print(a.info())       
print(a.speak())       

print(d.info())        # inherited
print(d.speak())       
print(d.fetch("ball")) # Dog method
print(d.breed)         # Dog attribute
