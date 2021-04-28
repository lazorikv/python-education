"""Making class calculator"""


class Calculator:
    """A class-container that contains 4 methods: addition, subtraction,
    multiplication, division """

    def __init__(self, first_arg, second_arg):
        """Initialize class variables."""
        self.first_arg = first_arg
        self.second_arg = second_arg

    def add(self, first_arg, second_arg):
        """Takes in two numbers, returns their sum."""
        self.first_arg = first_arg
        self.second_arg = second_arg
        result = self.first_arg + self.second_arg
        return result

    def subtract(self, first_arg, second_arg):
        """Takes in two numbers, returns their subtraction."""
        self.first_arg = first_arg
        self.second_arg = second_arg
        result = self.first_arg - self.second_arg
        return result

    def multiply(self, first_arg, second_arg):
        """Takes in two numbers, returns their multiplication."""
        self.first_arg = first_arg
        self.second_arg = second_arg
        result = self.first_arg * self.second_arg
        return result

    def divide(self, first_arg, second_arg):
        """Takes in two numbers, returns their division."""
        self.first_arg = first_arg
        self.second_arg = second_arg
        if second_arg == 0:
            result = "Divide by zero!"
        else:
            result = self.first_arg / self.second_arg
        return result
