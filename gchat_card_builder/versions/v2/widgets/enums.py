from enum import Enum


class ImageCropType(str, Enum):
    IMAGE_CROP_TYPE_UNSPECIFIED = "IMAGE_CROP_TYPE_UNSPECIFIED"
    SQUARE = "SQUARE"
    CIRCLE = "CIRCLE"
    RECTANGLE_CUSTOM = "RECTANGLE_CUSTOM"
    RECTANGLE_4_3 = "RECTANGLE_4_3"


class BorderType(str, Enum):
    BORDER_TYPE_UNSPECIFIED = "BORDER_TYPE_UNSPECIFIED"
    NO_BORDER = "NO_BORDER"
    STROKE = "STROKE"


class HorizontalSizeStyle(str, Enum):
    HORIZONTAL_SIZE_STYLE_UNSPECIFIED = "HORIZONTAL_SIZE_STYLE_UNSPECIFIED"
    FILL_AVAILABLE_SPACE = "FILL_AVAILABLE_SPACE"
    FILL_MINIMUM_SPACE = "FILL_MINIMUM_SPACE"


class HorizontalAlignment(str, Enum):
    HORIZONTAL_ALIGNMENT_UNSPECIFIED = "HORIZONTAL_ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"


class VerticalAlignment(str, Enum):
    VERTICAL_ALIGNMENT_UNSPECIFIED = "VERTICAL_ALIGNMENT_UNSPECIFIED"
    CENTER = "CENTER"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


class SelectionType(str, Enum):
    CHECK_BOX = "CHECK_BOX"
    RADIO_BUTTON = "RADIO_BUTTON"
    SWITCH = "SWITCH"
    DROPDOWN = "DROPDOWN"
    MULTI_SELECT = "MULTI_SELECT"


class DateTimePickerType(str, Enum):
    DATE_AND_TIME = "DATE_AND_TIME"
    DATE_ONLY = "DATE_ONLY"
    TIME_ONLY = "TIME_ONLY"


class TextInputType(Enum):
    SINGLE_LINE = "SINGLE_LINE"
    MULTIPLE_LINE = "MULTIPLE_LINE"


class DividerStyle(str, Enum):
    DIVIDER_STYLE_UNSPECIFIED = "DIVIDER_STYLE_UNSPECIFIED"
    SOLID_DIVIDER = "SOLID_DIVIDER"
    NO_DIVIDER = "NO_DIVIDER"


class DisplayStyle(str, Enum):
    DISPLAY_STYLE_UNSPECIFIED = "DISPLAY_STYLE_UNSPECIFIED"
    PEEK = "PEEK"
    REPLACE = "REPLACE"


class GridItemLayout(str, Enum):
    GRID_ITEM_LAYOUT_UNSPECIFIED = "GRID_ITEM_LAYOUT_UNSPECIFIED"
    TEXT_BELOW = "TEXT_BELOW"
    TEXT_ABOVE = "TEXT_ABOVE"


class LoadIndicator(Enum):
    SPINNER = "SPINNER"
    NONE = "NONE"


class Interaction(Enum):
    INTERACTION_UNSPECIFIED = "INTERACTION_UNSPECIFIED"
    OPEN_DIALOG = "OPEN_DIALOG"
