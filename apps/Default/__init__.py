import factory

from .app import Default


def initialize() -> None:
    factory.register("default", Default)
