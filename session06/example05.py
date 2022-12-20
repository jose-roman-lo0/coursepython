class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
  
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name, species="Dog")
    self.breed = breed
  
  def make_sound(self):
    print("Woof!")

dog1 = Dog("Fido", "Labrador")
print(dog1.name)  # Output: "Fido"
print(dog1.species)  # Output: "Dog"
print(dog1.breed)  # Output: "Labrador"
dog1.make_sound()  # Output: "Woof!"
