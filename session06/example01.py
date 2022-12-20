class Dog:
      def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  
  def bark(self):
    print("Woof!")

dog1 = Dog("Rulo", "Labrador")
dog2 = Dog("Otelo", "Poodle")

print(dog1.name)  # Output: "Rulo"
print(dog2.breed)  # Output: "Poodle"

dog1.bark()  # Output: "Woof!"
