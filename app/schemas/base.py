from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Shared base schema with common configurations.
    """

    class Config:
        orm_mode = True
