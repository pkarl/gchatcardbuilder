from .card_builder_base import CardBuilderBase

from .card_builder_v2 import CardBuilderV2


class CardBuilder:
    """
    Factory class for creating specific version builders.
    """

    @staticmethod
    def create(version: str = "2") -> CardBuilderBase:
        """
        Create and return the appropriate builder based on the provided version.

        Args:
            version (str): Google card version to use. Default is "2".

        Returns:
            CardBuilder: Instance of the appropriate card builder.
        """
        if version == "2":
            return CardBuilderV2()
        # elif version == "3":
        #     return CardBuilderV3() # future
        else:
            raise ValueError(f"Unsupported version: {version}")
