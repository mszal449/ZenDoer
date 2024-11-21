from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Shared base schema with common configurations.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
