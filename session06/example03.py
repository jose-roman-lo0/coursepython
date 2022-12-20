class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
  
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

dog1 = Dog("Fido", "Labrador")
dog2 = Dog("Buddy", "Poodle")

dog1.bark()  # Output: "Fido the Labrador says Woof!"
dog2.bark()  # Output: "Buddy the Poodle says Woof!"
