from typing import List, Optional

from pydantic import BaseModel

from .widgets import *  # pylint: disable=wildcard-import, unused-wildcard-import


class CardHeader(BaseModel):
    """
    https://developers.google.com/chat/api/reference/rest/v1/cards#cardheader
    """

    title: str
    subtitle: Optional[str] = None
    imageUrl: Optional[str] = None
    imageType: Optional[str] = None
    imageAltText: Optional[str] = None


class Section(BaseModel):
    header: str
    widgets: List[Widget]
    collapsible: Optional[bool] = False
    uncollapsibleWidgetsCount: Optional[int] = None


class CardFixedFooter(BaseModel):
    primaryButton: Button
    secondaryButton: Button


class Card(BaseModel):
    header: Optional[CardHeader] = None
    sections: List[Section] = []
    sectionDividerStyle: Optional[DividerStyle] = None
    cardActions: List[Action] = []
    name: Optional[str] = None  # not used by chat apps
    fixedFooter: Optional[CardFixedFooter] = None
    displayStyle: Optional[DisplayStyle] = None
    peekCardHeader: Optional[CardHeader] = None


class CardV2(BaseModel):
    cardId: str
    card: Card
