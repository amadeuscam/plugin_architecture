from __future__ import annotations

from typing import Callable

from app_type import AppTemplate

app_creation_funcs: dict[str, Callable[..., AppTemplate]] = {}


def register(app_name: str, creation_funcs: Callable[..., AppTemplate]):
    """Registra una nueva app"""
    app_creation_funcs[app_name] = creation_funcs


def unregister(app_name: str):
    app_creation_funcs.pop(app_name, None)

def all_apps():
    return app_creation_funcs.items()

def get_app(name:str):
    return app_creation_funcs.get(name,None)



def create(app_name: str):
    try:
        creation_func = app_creation_funcs[app_name]
        return creation_func()
    except KeyError:
        raise ValueError("se desconoce esta app")
