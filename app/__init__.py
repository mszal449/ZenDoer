from app.db import get_connection
from app.models.subtask import Subtask
from app.models.task import Task

from .app import App


def initialize_db():
    conn = get_connection()
    Task.create_table(conn)
    Subtask.create_table(conn)
    conn.close()


initialize_db()


__all__ = ["App"]
