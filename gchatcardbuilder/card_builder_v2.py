# pylint: disable=invalid-name
from typing import Any, Dict, List

from .card_builder_base import CardBuilderBase
from .utils import models_to_dict
from .versions.v2.root import *  # pylint: disable=wildcard-import, unused-wildcard-import


class CardBuilderV2(CardBuilderBase):
    """
    Builder for version 2 of the Google Chat card format.
    """

    _cardsV2: List[CardV2]
    _cardV2: object
    _cardId: Optional[str]
    _card: Card

    def __init__(self) -> None:
        super().__init__()
        self._cardsV2 = []
        self._cardV2 = {}
        self._cardId = None
        self._card = Card()
        self.reset()

    def reset(self) -> None:
        self._cardsV2 = []
        self._cardV2 = {}
        self._cardId = None
        self._card = Card()

    def set_card_id(self, card_id: str) -> "CardBuilderV2":
        self._cardId = card_id
        return self

    def set_header(
        self,
        header: CardHeader,
    ) -> "CardBuilderV2":
        self._card.header = header
        return self

    def add_section(self, section: Section) -> "CardBuilderV2":
        self._card.sections.append(section)
        return self

    def build(self) -> Dict[str, Any]:
        """Retrieve the built card and reset the builder."""
        self._cardV2["cardId"] = self._cardId
        self._cardV2["card"] = self._card
        self._cardsV2.append(self._cardV2)
        constructed_card = models_to_dict(self._cardsV2)
        self.reset()
        return constructed_card
