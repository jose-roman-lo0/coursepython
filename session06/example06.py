class Calculator:
    def add(self, x, y=None):
        if y is None:
            return x
        else:
            return x + y

calculator = Calculator()

print(calculator.add(5))  # Output: 5
print(calculator.add(5, 10))  # Output: 15
print(calculator.add(5, 10, 15))  # Output: TypeError (too many arguments)
