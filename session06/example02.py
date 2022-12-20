class MobilePhone:
      def __init__(self, number):
    self.number = number
  
  def turn_on(self):
    return f"Mobile phone {self.number} is turned on"
  
  def turn_off(self):
    return "Mobile phone is turned off"
  
  def call(self, number):
    return f"Calling {number}"

phone1 = MobilePhone("123-456-7890")
phone2 = MobilePhone("098-765-4321")

print(phone1.turn_on())  # Output: "Mobile phone 123-456-7890 is turned on"
print(phone2.turn_on())  # Output: "Mobile phone 098-765-4321 is turned on"

print(phone1.call("456-789-0123"))  # Output: "Calling 456-789-0123"
print(phone2.call("789-012-3456"))  # Output: "Calling 789-012-3456"

print(phone1.turn_off())  # Output: "Mobile phone is turned off"
print(phone2.turn_off())  # Output: "Mobile phone is turned off"
