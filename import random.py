import random

class RandomNumber:
    def __init__(self, Roll_Numbers):
        self.Roll_Numbers = Roll_Numbers
        self.roll_numbers = self.read_roll_numbers()

    def read_roll_numbers(self):
        """Reads roll numbers from the specified file and returns a list of them."""
        try:
            with open(self.Roll_Numbers, 'r') as file:
                roll_numbers = [line.strip() for line in file if line.strip().isdigit()]
            return roll_numbers
        except FileNotFoundError:
            print(f"Error: The file '{self.Roll_Numbers}' was not found.")
            return []

    def generate_random_roll_numbers(self, count=10):
        """Generates a specified number of unique random roll numbers from the list."""
        if count > len(self.roll_numbers):
            print("Error: Requested number of roll numbers exceeds available data.")
            return []
        return random.sample(self.roll_numbers, count)

# Usage
selector = RandomNumber("roll_numbers.txt")
random_roll_numbers = selector.generate_random_roll_numbers()
print("Random Roll Numbers:", random_roll_numbers)
