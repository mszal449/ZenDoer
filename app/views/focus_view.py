from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkProgressBar, CTkScrollableFrame

from .base_view import BaseView
from .focus_controller import FocusController
from .widgets import TaskCard


class FocusView(BaseView):
    text_color = "#d4d2d2"

    def __init__(self, master=None, width=250, height=800, **kw):
        super().__init__(master, width, height, **kw)
        self.max_width = 300
        self.max_height = 800

        self.controller = FocusController(self)

        self.add_widgets()

    def add_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.add_progress_bar(row=0)
        self.add_active_task_panel(row=1)
        self.add_task_panel(row=2)

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
        task_progress_bar.set(self.controller.done_tasks_percentage())

        progress_label = CTkLabel(frame, text=f"{self.controller.done_tasks_percentage()}")
        progress_label.grid(row=row, column=1, sticky="e", padx=10)

    def add_active_task_panel(self, row=1):
        frame = CTkFrame(self)
        frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        frame.grid_columnconfigure(0, weight=1)

        task_widget = TaskCard(
            self.controller.active_task,
            master=frame,
            button_action=self.controller.toggle_countdown,
        )
        task_widget.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    def add_task_panel(self, row=1):
        frame = CTkFrame(self)
        frame.grid(row=row, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        label = CTkLabel(frame, text="Tasks", font=("Arial", 16), text_color=self.text_color)
        label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        scrollable_frame = CTkScrollableFrame(frame)
        scrollable_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=(0, 5))
        scrollable_frame.grid_columnconfigure(0, weight=1)

        for i, task in enumerate(self.controller.tasks):
            task_widget = TaskCard(task, master=scrollable_frame)
            task_widget.grid(row=i, column=0, sticky="ew", pady=2)

        create_task_button = CTkButton(
            frame,
            text="Add Task",
            # command=self.create_task,
            text_color="black",
            fg_color="#25d3a2",
            hover_color="#9de8ca",
            cursor="hand2",
            corner_radius=5,
        )

        create_task_button.grid(row=len(self.controller.tasks) + 1, column=0, sticky="ew", padx=5, pady=(0, 10))

        # Ensure the parent container expands
        self.grid_rowconfigure(row, weight=1)

    def add_done_task_panel(self, row=3):
        frame = CTkFrame(self)
        frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        frame.grid_columnconfigure(0, weight=1)

        label = CTkLabel(frame, text="Done", font=("Arial", 16), text_color=self.text_color)
        label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        for i, task in enumerate([task for task in self.controller.tasks if task.done]):
            task_widget = TaskCard(task, master=frame)
            task_widget.grid(row=i + 1, column=0, sticky="ew", padx=5, pady=(0, 5))
