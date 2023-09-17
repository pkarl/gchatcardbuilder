from abc import ABC, abstractmethod
from typing import Dict, Any


class CardBuilderBase(ABC):
    """
    The base builder class... this is the interface that all builders must
    implement. 🤷‍♂️
    """

    def __init__(self) -> None:
        """Initialize a new instance of the builder."""

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the current building process and initialize a new card.
        """

    @abstractmethod
    def build(self) -> Dict[str, Any]:
        """Retrieve the built card and reset the builder."""
