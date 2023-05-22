# core.py
import importlib
import os
from pathlib import Path

import factory
from app_type import AppTemplate


class MyApplication:

    file_ignore = ['__init__.py', '__pycache__']
    # We are going to receive a list of plugins as parameter

    def __init__(self):
        BASE_DIR = Path(__file__).parent
        STATICFILES_DIRS = os.path.join(BASE_DIR, "apps")
        self._plugins_apps: list[AppTemplate] = []
        my_list = os.listdir(STATICFILES_DIRS)

        self.apps = [dir_name for dir_name in my_list if dir_name not in self.file_ignore]  # noqa
        print(self.apps)

        # register the apps
        for app in self.apps:
            try:
                app = importlib.import_module('apps.' + app)
                app.initialize()
            except AttributeError:
                raise AttributeError(
                    "Comprueba que has creado la classe Plugin")
        # self.apps = []
        if len(self.apps) == 0:
            print("estoy aqui")
            # If no plugin were set we use our default
            app = importlib.import_module('apps.' + "Default")
            app.initialize()

        for app_name, _ in factory.all_apps():
            app = factory.create(app_name)
            self._plugins_apps.append(app)

    def run(self, app_name: str = 'default'):
        print("Starting my application")
        print("-" * 10)
        print("This is my core system")
        print(factory.all_apps())
        # print(factory.get_app("default").__str__())
        app = factory.get_app(app_name)()
        print(app.load_setting())
        # print(self._plugins)
        # We is were magic happens, and all the plugins are going to be printed
        # for plugin in self._plugins_apps:
        #     plugin.load_setting()

        print("-" * 10)
        print("Ending my application")
        print()
