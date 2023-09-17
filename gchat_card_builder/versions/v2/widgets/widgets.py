"""
This module contains the models for the widgets used in the cards.

By and large, the contents of this module are generated from the
docs here: https://developers.google.com/chat/api/reference/rest/v1/cards

via ChatGPT4, converted into Pydantic classes
"""
from typing import List, Optional, Union

from pydantic import (
    BaseModel,
    # FieldValidationInfo,
    field_validator,
    # Annotated,
    Field,
    ValidationError,
    model_validator,
)

from typing_extensions import Annotated


from .enums import (
    BorderType,
    DateTimePickerType,
    GridItemLayout,
    HorizontalAlignment,
    HorizontalSizeStyle,
    ImageCropType,
    SelectionType,
    TextInputType,
    VerticalAlignment,
    LoadIndicator,
    Interaction,
)


# Models
class Color(BaseModel):
    red: int
    green: int
    blue: int


class ImageCropStyle(BaseModel):
    type: ImageCropType
    aspectRatio: float = Field(..., ge=0)  # greater than or equal to 0


class BorderStyle(BaseModel):
    type: BorderType
    strokeColor: Color
    cornerRadius: int


class ImageComponent(BaseModel):
    imageUri: str
    altText: str
    cropStyle: ImageCropStyle
    borderStyle: BorderStyle


class Column(BaseModel):
    horizontalSizeStyle: HorizontalSizeStyle
    horizontalAlignment: HorizontalAlignment
    verticalAlignment: VerticalAlignment
    widgets: List["Widget"]  # Quotation marks used for forward declaration


class Columns(BaseModel):
    columnItems: List[Column]


class SuggestionItem(BaseModel):
    text: str


class Suggestions(BaseModel):
    items: List[SuggestionItem]


class SelectionItem(BaseModel):
    text: str
    value: str
    selected: bool
    startIconUri: str
    bottomText: str


class SelectionInput(BaseModel):
    name: str
    label: str
    type: SelectionType
    items: List[SelectionItem]
    onChangeAction: "Action"
    # multiSelectMaxSelectedItems: int
    # multiSelectMinQueryLength: int
    # multi_select_data_source: Union["Action", "PlatformDataSource"]


class DateTimePicker(BaseModel):
    name: str
    label: str
    type: DateTimePickerType
    valueMsEpoch: str
    timezoneOffsetDate: int
    onChangeAction: "Action"


class Divider(BaseModel):
    pass  # No fields for Divider


class GridItem(BaseModel):
    id: str
    image: ImageComponent
    title: str
    subtitle: str
    layout: GridItemLayout


class Grid(BaseModel):
    title: str
    items: List[GridItem]
    borderStyle: BorderStyle
    columnCount: int
    onClick: "OnClick"


class Icon(BaseModel):
    altText: str
    imageType: str
    icons: Union[str, str]


class Button(BaseModel):
    text: str
    icon: Icon
    color: Color
    onClick: "OnClick"
    disabled: bool
    altText: str


class SwitchControl(BaseModel):
    name: str
    value: str
    selected: bool
    onChangeAction: "Action"
    controlType: SelectionType


class DecoratedText(BaseModel):
    icon: Optional[Icon]
    startIcon: Optional[Icon]
    topLabel: Optional[str]
    text: str
    wrapText: bool
    bottomLabel: Optional[str]
    onClick: Optional["OnClick"]
    button: Optional[Button]
    switchControl: Optional[SwitchControl]
    endIcon: Optional[Icon]

    @model_validator(mode="after")
    def check_union_fields(self, values):
        union_fields = ["button", "switchControl", "endIcon"]
        set_fields = [field for field in union_fields if values.get(field)]
        if len(set_fields) > 1:
            raise ValidationError(
                f"Only one of {union_fields} can be set, but got {set_fields}"
            )
        return values


class ActionParameter(BaseModel):
    key: str
    value: str


class Action(BaseModel):
    function: str
    parameters: List[ActionParameter]
    loadIndicator: LoadIndicator
    persistValues: bool
    interaction: Interaction


class OpenLink(BaseModel):
    url: str
    openAs: str
    onClose: str


class OnClick(BaseModel):
    openLink: Optional[OpenLink]
    action: Optional[Action]


class Image(BaseModel):
    imageUrl: str
    onClick: OnClick
    altText: str


class ButtonList(BaseModel):
    buttons: List[Button]


class TextInput(BaseModel):
    name: str
    label: str
    hintText: str
    value: str
    input_type: Annotated[
        TextInputType, Field(alias="type")
    ]  # , field_validator("type")
    onChangeAction: Action
    initialSuggestions: Optional["Suggestions"]
    autoCompleteAction: Action
    placeholderText: str

    # @field_validator("type")
    # def check_initial_suggestions(self, v):  # pylint: disable=invalid-name
    #     if self.initialSuggestions:
    #         return TextInputType.SINGLE_LINE.value
    #     return v


class TextParagraph(BaseModel):
    text: str


class CardAction(BaseModel):
    actionLabel: str
    onClick: OnClick


class Widget(BaseModel):
    textParagraph: Optional[TextParagraph]
    image: Optional[Image]
    decoratedText: Optional[DecoratedText]
    buttonList: Optional[ButtonList]
    textInput: Optional[TextInput]
    selectionInput: Optional[SelectionInput]
    dateTimePicker: Optional[DateTimePicker]

    @property
    def data(self):
        fields = [
            "textParagraph",
            "image",
            "decoratedText",
            "buttonList",
            "textInput",
            "selectionInput",
            "dateTimePicker",
        ]
        set_fields = [field for field in fields if getattr(self, field)]

        if len(set_fields) != 1:
            raise ValidationError("A widget may only have one type")
        return set_fields[0]


# Later in the code:
Widget.model_rebuild()
