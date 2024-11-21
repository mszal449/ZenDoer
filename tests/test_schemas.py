from datetime import datetime, timedelta
from enum import Enum

import pytest
from pydantic import ValidationError

from app.schemas import SubtaskSchema, TaskSchema
from app.schemas.subtask import Status


# Test valid TaskSchema creation
def test_valid_task():
    start_time = datetime(2024, 11, 21, 10, 0)
    end_time = datetime(2024, 11, 21, 12, 0)
    task = TaskSchema(
        name="Test Task",
        description="A test task description",
        duration_time=3600,  # 1 hour in seconds
        time_left=1800,  # 30 minutes in seconds
        start_time=start_time,
        end_time=end_time,
        subtasks=[],
    )
    assert task.name == "Test Task"
    assert task.description == "A test task description"
    assert task.duration_time == 3600
    assert task.time_left == 1800
    assert task.start_time == start_time
    assert task.end_time == end_time


# Test invalid end_time (should be after start_time)
def test_end_time_before_start_time():
    start_time = datetime(2024, 11, 21, 10, 0)
    end_time = datetime(2024, 11, 21, 9, 0)  # End time is before start time
    with pytest.raises(ValidationError):
        TaskSchema(
            name="Invalid Task",
            description="Invalid task description",
            duration_time=3600,
            time_left=1800,
            start_time=start_time,
            end_time=end_time,
            subtasks=[],
        )


# Test invalid time_left (greater than duration_time)
def test_time_left_greater_than_duration():
    start_time = datetime(2024, 11, 21, 10, 0)
    end_time = datetime(2024, 11, 21, 12, 0)
    with pytest.raises(ValidationError):
        TaskSchema(
            name="Invalid Task",
            description="Invalid task description",
            duration_time=3600,
            time_left=4000,  # Invalid, more than duration_time
            start_time=start_time,
            end_time=end_time,
            subtasks=[],
        )


# Test valid SubtaskSchema creation
def test_valid_subtask():
    subtask = SubtaskSchema(
        name="Subtask 1",
        description="A subtask description",
        status=Status.NOT_STARTED,
    )
    assert subtask.name == "Subtask 1"
    assert subtask.description == "A subtask description"
    assert subtask.status == Status.NOT_STARTED


# Test that a task can have subtasks
def test_task_with_subtasks():
    start_time = datetime(2024, 11, 21, 10, 0)
    end_time = datetime(2024, 11, 21, 12, 0)
    subtask1 = SubtaskSchema(
        name="Subtask 1",
        description="First subtask",
        status=Status.NOT_STARTED,
    )
    subtask2 = SubtaskSchema(
        name="Subtask 2",
        description="Second subtask",
        status=Status.IN_PROGRESS,
    )
    task = TaskSchema(
        name="Task with Subtasks",
        description="A task with multiple subtasks",
        duration_time=7200,  # 2 hours in seconds
        time_left=3600,  # 1 hour in seconds
        start_time=start_time,
        end_time=end_time,
        subtasks=[subtask1, subtask2],
    )
    assert len(task.subtasks) == 2
    assert task.subtasks[0].name == "Subtask 1"
    assert task.subtasks[1].name == "Subtask 2"


# Test that a task without subtasks is still valid
def test_task_without_subtasks():
    start_time = datetime(2024, 11, 21, 10, 0)
    end_time = datetime(2024, 11, 21, 12, 0)
    task = TaskSchema(
        name="Task without subtasks",
        description="A task without any subtasks",
        duration_time=3600,
        time_left=1800,
        start_time=start_time,
        end_time=end_time,
        subtasks=[],  # No subtasks
    )
    assert len(task.subtasks) == 0
