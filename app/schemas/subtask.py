from enum import Enum

from .base import BaseSchema


class Status(str, Enum):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class SubtaskSchema(BaseSchema):
    name: str
    description: str
    status: Status = Status.NOT_STARTED
