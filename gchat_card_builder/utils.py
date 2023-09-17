from pydantic import BaseModel


def models_to_dict(model) -> dict:
    """Converts a Pydantic model and its nested models into a dictionary."""

    # If the model is already a dictionary, process its values.
    if isinstance(model, dict):
        return {key: models_to_dict(value) for key, value in model.items()}

    # If the model is a list, process its elements.
    if isinstance(model, list):
        return [models_to_dict(item) for item in model]

    # If the model is an instance of BaseModel, convert it to a dictionary and process its fields.
    if isinstance(model, BaseModel):
        return {
            field_name: models_to_dict(value)
            for field_name, value in model.model_dump().items()
        }

    # If the model is none of the above types, return it as is.
    return model
