from datetime import datetime

from customtkinter import CTkFrame, CTkLabel, CTkProgressBar

from ..models import Task
from .base_view import BaseView
from .widgets import TaskCard


class FocusView(BaseView):
    text_color = "#b5b5b5"

    def __init__(self, master=None, width=250, height=800, **kw):
        super().__init__(master, width, height, **kw)
        self.max_width = 300
        self.max_height = 800
        self.add_widgets()

    def add_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.add_progress_bar(row=0)
        self.add_task_panel(row=1)

    def add_progress_bar(self, row=0):
        frame = CTkFrame(self)
        frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        frame.grid_columnconfigure(0, weight=1)

        task_progress_bar = CTkProgressBar(
            frame,
            orientation="horizontal",
            progress_color="#25d3a2",
            corner_radius=10,
        )
        task_progress_bar.grid(row=0, column=0, sticky="ew")
        task_progress_bar.set(0.66)

        progress_label = CTkLabel(frame, text="2/3 Done")
        progress_label.grid(row=row, column=1, sticky="e", padx=10)

    def add_timer(self):
        pass

    def add_task_panel(self, row=1):
        frame = CTkFrame(self)
        frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        frame.grid_columnconfigure(0, weight=1)

        label = CTkLabel(frame, text="Tasks", font=("Arial", 16), text_color=self.text_color)
        label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        tasks = get_sample_tasks(4)

        for i, task in enumerate(tasks):
            task_widget = TaskCard(task, master=frame)
            task_widget.grid(row=i + 1, column=0, sticky="ew", padx=5, pady=(0, 5))


def get_sample_tasks(sample_size: int):
    tasks = []
    for i in range(sample_size):
        task = Task(
            id=i + 1,
            name=f"Task {i + 1}",
            description=f"This is task {i + 1}.",
            duration_time=3600,
            time_left=1800,
            start_time=datetime(2024, 11, 21, 10, 0),
            end_time=datetime(2024, 11, 21, 11, 0),
        )
        tasks.append(task)
    return tasks
