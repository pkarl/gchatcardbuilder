# pylint: disable=protected-access, C1803

import pytest  # pylint: disable=unused-import

from gchatcardbuilder.card_builder_v2 import CardBuilderV2
from gchatcardbuilder.versions.v2.root import *  # pylint: disable=unused-wildcard-import, wildcard-import

# Sample instances for testing
sample_header = CardHeader(
    title="Test Header",
)
sample_section = Section(header="Test Section", widgets=[])


def test_reset():
    builder = CardBuilderV2()
    builder.set_card_id("sample_id")

    builder.reset()

    assert builder._cardsV2 == []
    assert builder._cardId is None
    assert builder._card is not None


def test_set_card_id():
    builder = CardBuilderV2()
    builder.set_card_id("sample_id")

    assert builder._cardId == "sample_id"


def test_set_header():
    builder = CardBuilderV2()
    builder.set_header(sample_header)

    assert builder._card.header == sample_header


def test_add_section():
    builder = CardBuilderV2()
    builder.add_section(sample_section)

    assert sample_section in builder._card.sections


def test_build():
    builder = CardBuilderV2()
    builder.set_card_id("sample_id")
    builder.set_header(sample_header)
    builder.add_section(sample_section)

    cardsv2 = builder.build()

    # Simple assertion, assuming models_to_dict function
    # returns dictionary representation of the object
    assert isinstance(cardsv2, list)
    assert isinstance(cardsv2[0], dict)
    assert isinstance(cardsv2[0].get("card").get("sections")[0], dict)

    # Checking the built card has been reset
    assert builder._cardsV2 == []
    assert builder._cardId is None
    assert builder._card.header is None
