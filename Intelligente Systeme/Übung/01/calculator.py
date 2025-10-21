import sys

class Calculator:
    def __init__(self):
        pass
 
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
 


if __name__ == "__main__":
    args = sys.argv[1:]  # Get command line arguments (excluding script name)
    calc = Calculator()
    match args:
        case ["add", x, y]:
            result = calc.add(int(x), int(y))
            print(f"Result: {result}")
        case ["subtract", x, y]:
            result = calc.subtract(int(x), int(y))
            print(f"Result: {result}")
        case ["multiply", x, y]:
            result = calc.multiply(int(x), int(y))
            print(f"Result: {result}")
        case ["divide", x, y]:
            try:
                result = calc.divide(int(x), int(y))
                print(f"Result: {result}")
            except ValueError as e:
                print(e)
        case ["power", x, y]:
            result = calc.power(int(x), int(y))
            print(f"Result: {result}")
        case _:
            print("Invalid command")