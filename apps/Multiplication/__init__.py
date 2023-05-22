import factory

from .app import Multiplication


def initialize() -> None:
    factory.register("multiplication", Multiplication)
