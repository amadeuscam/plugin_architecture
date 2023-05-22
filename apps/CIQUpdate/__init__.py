import factory

from .app import CIQUpdate


def initialize() -> None:
    factory.register("ciqupdate", CIQUpdate)
