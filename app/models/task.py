from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    duration_time = Column(Integer, nullable=False)  # Duration in seconds
    time_left = Column(Integer, nullable=False)  # Time left in seconds
    start_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=False)

    # Relationship to Subtasks
    subtasks = relationship(
        "Subtask",
        back_populates="task",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Task(id={self.id}, name={self.name}, description={self.description}, "
            f"duration_time={self.duration_time}, time_left={self.time_left}, "
            f"start_time={self.start_time}, end_time={self.end_time})>"
        )
