# GChat Card Builder (v2)

Gchat Card Builder is a Python library that assists in the creation and management of chat "cards" for Google Chat responses via API. Supports CardsV2 format.

[![codecov](https://codecov.io/github/pkarl/gchatcardbuilder/graph/badge.svg?token=DQC6S9XHR0)](https://codecov.io/github/pkarl/gchatcardbuilder) [![Python CI with Pytest and Coverage](https://github.com/pkarl/gchatcardbuilder/actions/workflows/python-versions-ci.yml/badge.svg)](https://github.com/pkarl/gchatcardbuilder/actions/workflows/python-versions-ci.yml)

---

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Documentation](#documentation)
5. [Tests](#tests)

---

## Description
Gchat Card Builder provides an easy-to-use interface for creating richly formatted cards compatible with Google Chat. The goal is to stop mucking around with deeply nested structures just to send a slightly rich chat message.

Here's an example of how this could help clean up code:

```python
# broken onto several lines for readability
gchat_response = copy.deepcopy(BIG_OLD_DICT_TEMPLATE)
widgets = gchat_response["cardsV2"][0]["card"]["sections"][0]["widgets"]
button = widgets[0]["buttonList"]["buttons"][0]
button["text"] = "click to get rick rolled"
button["onClick"]["openLink"]["url"] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

becomes this:

```python
builder = CardBuilder.create()
builder.add_section(
    W.ButtonList(
        buttons=[
            W.Button(
                text="click to get rick rolled",
                onClick=W.OnClick(
                    openLink=W.OpenLink(
                        url='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                    )
                )
            )
        ]
    ),
)

gchat_response = builder.build()
```

---

## Installation

### Prerequisites

- Python (versions tested: 3.10, 3.11)
- may support others

### Installation Steps
```bash
pip install gchatcardbuilder
```

---

## Usage

Google Chat Card Builder provides an easy-to-use interface for creating richly formatted cards compatible with Google Chat. Here's how you can quickly start building cards using the factory method:

### Basic Example:

```python
from gchat_card_builder import CardBuilder, CardWidgets as W

# Get builder instance using the factory method
builder = CardBuilder.create()

# Add card details
builder.set_card_id("sample_id")
builder.set_header(W.CardHeader(title="Test Header"))
builder.add_section(W.Section(header="Test Section", widgets=[]))

# Build the card
card = builder.build()
```

---

## Documentation
You're looking at it.

---

## Tests

If you're planning on contributing or wish to run tests to ensure the library functions as expected in your environment:

1. Clone the repository:
```bash
git clone https://github.com/pkarl/gchatcardbuilder
```

2. Navigate to the cloned directory and install the requirements:
```bash
pip install -r requirements.txt
```

3. Run the tests:
```bash
pytest
```

---

If you have any questions, issues, or feedback, feel free to open an issue in the repository. Contributions are always welcome!

---

Maintained by PK2
