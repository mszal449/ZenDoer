from __future__ import annotations

import sqlite3
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from .subtask import Subtask


@dataclass
class Task:
    id: int | None
    name: str
    description: str
    done: bool = False
    duration_time: int = 0
    time_left: int = 0
    start_time: datetime = field(default_factory=datetime.now)
    end_time: datetime = field(default_factory=datetime.now)
    subtasks: list[Subtask] = field(default_factory=list)

    @staticmethod
    def create_table(conn: sqlite3.Connection):
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                done BOOLEAN NOT NULL DEFAULT 0,
                duration_time INTEGER NOT NULL,
                time_left INTEGER NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL
            )
        """,
        )
        conn.commit()

    def save(self, conn: sqlite3.Connection):
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (name, description, done, duration_time, time_left, start_time, end_time)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                self.name,
                self.description,
                int(self.done),
                self.duration_time,
                self.time_left,
                self.start_time.isoformat(),
                self.end_time.isoformat(),
            ),
        )
        self.id = cursor.lastrowid
        conn.commit()

    @staticmethod
    def get_all(conn: sqlite3.Connection) -> list[Task]:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(
                Task(
                    id=row[0],
                    name=row[1],
                    description=row[2],
                    done=bool(row[3]),
                    duration_time=row[4],
                    time_left=row[5],
                    start_time=datetime.fromisoformat(row[6]),
                    end_time=datetime.fromisoformat(row[7]),
                ),
            )
        return tasks
