import random
from datetime import datetime

from ..models import Task
from ..services import TaskService


class FocusController:
    def __init__(self, view):
        self.view = view

        self.tasks = TaskService.get_all_tasks()
        self.active_task = self.tasks[0]

    def done_tasks_percentage(self):
        return len([task for task in self.tasks if task.done]) / len(self.tasks)

    def toggle_countdown(self, task_id: int):
        print(f"Toggled countdown for task: {task_id}")


def get_sample_tasks(sample_size: int):
    tasks = []
    for i in range(sample_size):
        task = Task(
            id=i + 1,
            name=f"Task {i + 1}",
            description=f"This is task {i + 1}.",
            duration_time=3600,
            time_left=1800,
            done=random.choice([True, False]),
            start_time=datetime(2024, 11, 21, 10, 0),
            end_time=datetime(2024, 11, 21, 11, 0),
        )
        tasks.append(task)
    return tasks
