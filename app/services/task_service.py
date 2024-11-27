from datetime import datetime
from typing import List, Optional

from app.db import get_connection
from app.models.subtask import Subtask
from app.models.task import Task


class TaskService:
    @staticmethod
    def create_task(name: str, description: str, duration_time: int) -> Task:
        task = Task(
            id=None,
            name=name,
            description=description,
            done=False,
            duration_time=duration_time,
            time_left=duration_time,
            start_time=datetime.now(),
            end_time=datetime.now(),
        )
        conn = get_connection()
        task.save(conn)
        conn.close()
        return task

    @staticmethod
    def get_all_tasks() -> List[Task]:
        conn = get_connection()
        tasks = Task.get_all(conn)
        for task in tasks:
            if task.id is not None:
                task.subtasks = Subtask.get_by_task(conn, task.id)
            else:
                task.subtasks = []
        conn.close()
        return tasks

    @staticmethod
    def get_task_by_id(task_id: int) -> Optional[Task]:
        conn = get_connection()
        tasks = Task.get_all(conn)
        for task in tasks:
            if task.id == task_id:
                if task.id is not None:
                    task.subtasks = Subtask.get_by_task(conn, task.id)
                else:
                    task.subtasks = []
                conn.close()
                return task
        conn.close()
        return None

    @staticmethod
    def update_task(task_id: int, **kwargs) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(task_id)
        query = f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, tuple(values))
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    @staticmethod
    def delete_task(task_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        cursor.execute("DELETE FROM subtasks WHERE task_id = ?", (task_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted

    @staticmethod
    def add_subtask(task_id: int, name: str, description: str, status: str = "not started") -> Subtask:
        subtask = Subtask(
            id=None,
            task_id=task_id,
            name=name,
            description=description,
            status=status,
        )
        conn = get_connection()
        subtask.save(conn)
        conn.close()
        return subtask

    @staticmethod
    def update_subtask(subtask_id: int, **kwargs) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        fields = []
        values = []
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(subtask_id)
        query = f"UPDATE su btasks SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(query, tuple(values))
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    @staticmethod
    def delete_subtask(subtask_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM subtasks WHERE id = ?", (subtask_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted
