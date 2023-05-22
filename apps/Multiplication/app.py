# deafult.py
import factory


# Define our default class
class Multiplication:
    # Define static method, so no self parameter
    def process(self, num1, num2):
        # Some prints to identify which plugin is been used
        print("This is my default plugin")
        print(f"Numbers are {num1} and {num2}")

    def load_setting(self) -> None:
        """load setting data"""
        print("Multiplication - load_setting")


def initialize()-> None:
    factory.register("multiplication",Multiplication)
