# Exercise 9-10
class Resturant:
    """A simple attempt to model a dog."""

    def __init__(self, name, type, number_served):
        """Initialize name and age attributes."""
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_resturant(self):
        """Simulate a dog sitting in response to a command."""
        print(f"Welcome to {self.name} we serve {self.type}.")

    def open_resturant(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now open")

    def set_number_served(self, served):
        self.number_served += served


class Icecreamstand(Resturant):

    def __init__(self, flavors):
        """Initialize name and age attributes."""
        self.flavors = flavors

    def print_flavors(self):
        """prints flavors"""
        print(self.flavors)