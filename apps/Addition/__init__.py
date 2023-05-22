import factory

from .app import Addition


def initialize() -> None:
    factory.register("addition", Addition)
