# deafult.py
import json
import os


# Define our default class
class Default:

    def __init__(self) -> None:
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
       
    # Define static method, so no self parameter

    def process(self, num1, num2):
        # Some prints to identify which plugin is been used
        print("This is my default plugin")
        print(f"Numbers are {num1} and {num2}")
    
    def load_setting(self) -> None:
        """load setting data"""
        print("Default - load_setting")
        path_file = os.path.join(self.BASE_DIR, 'config/settings.json')
        self.process(12,23)
        print(path_file)
        with open(path_file) as file:
            data = json.load(file)
            print(data)

    @staticmethod
    def __str__() -> str:
        return "Default Baby"
