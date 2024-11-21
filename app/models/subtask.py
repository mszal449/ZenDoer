import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Status(enum.Enum):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class Subtask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status: Column[Status] = Column(Enum(Status), default=Status.NOT_STARTED, nullable=False)

    # Relationship back to Task
    task = relationship("Task", back_populates="subtasks")

    def __repr__(self):
        return (
            f"<Subtask(id={self.id}, task_id={self.task_id}, name={self.name}, "
            f"description={self.description}, status={self.status})>"
        )
