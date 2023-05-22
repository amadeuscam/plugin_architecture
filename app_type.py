from typing import Protocol


class AppTemplate(Protocol):
    """Representacion basica de una app en pm"""

    def load_setting(self) -> None:
        """load setting data"""
