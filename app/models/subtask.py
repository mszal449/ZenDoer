import sqlite3
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Subtask:
    id: Optional[int]
    task_id: int
    name: str
    description: str
    status: str = "not started"

    @staticmethod
    def create_table(conn: sqlite3.Connection):
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS subtasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY(task_id) REFERENCES tasks(id)
            )
        """,
        )
        conn.commit()

    def save(self, conn: sqlite3.Connection):
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO subtasks (task_id, name, description, status)
            VALUES (?, ?, ?, ?)
        """,
            (
                self.task_id,
                self.name,
                self.description,
                self.status,
            ),
        )
        self.id = cursor.lastrowid
        conn.commit()

    @staticmethod
    def get_by_task(conn: sqlite3.Connection, task_id: int) -> List["Subtask"]:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subtasks WHERE task_id = ?", (task_id,))
        rows = cursor.fetchall()
        subtasks = []
        for row in rows:
            subtasks.append(
                Subtask(
                    id=row[0],
                    task_id=row[1],
                    name=row[2],
                    description=row[3],
                    status=row[4],
                ),
            )
        return subtasks
