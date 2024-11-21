from datetime import datetime
from typing import List

from pydantic import Field, field_validator, validator

from .base import BaseSchema
from .subtask import SubtaskSchema


class TaskSchema(BaseSchema):
    name: str
    description: str
    duration_time: int = Field(..., gt=0, description="Duration in seconds")
    time_left: int = Field(..., ge=0, description="Time left in seconds")
    start_time: datetime
    end_time: datetime

    subtasks: List[SubtaskSchema]

    @field_validator("end_time")
    def end_time_after_start_time(cls, end_time, values):
        start_time = values.get("start_time")
        if start_time and end_time <= start_time:
            raise ValueError("end_time must be after start_time")
        return end_time

    @field_validator("time_left")
    def time_left_less_than_duration_time(cls, time_left, values):
        duration_time = values.get("duration_time")
        if duration_time and time_left > duration_time:
            raise ValueError("time_left must be less than or equal to duration_time")
        return time_left
