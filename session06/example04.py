class Dog:
    species = "Canis familiaris"  # Class variable
  
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable
  
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

dog1 = Dog("Fido", "Labrador")
dog2 = Dog("Buddy", "Poodle")

print(Dog.species)  # Output: "Canis familiaris"
print(dog1.species)  # Output: "Canis familiaris"
print(dog2.species)  # Output: "Canis familiaris"

dog1.species = "Canis lupus"  # Modify class variable
print(Dog.species)  # Output: "Canis familiaris" (not modified)
print(dog1.species)  # Output: "Canis lupus" (modified for this instance only)
print(dog2.species)  # Output: "Canis familiaris" (not modified)
