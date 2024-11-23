from datetime import timedelta

from customtkinter import CTkButton, CTkFrame, CTkLabel


class TaskCard(CTkFrame):
    text_color = "#b5b5b5"

    def __init__(self, task, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.task = task
        self.configure(corner_radius=10, fg_color="#2b2b2b")
        # self.grid_columnconfigure()
        self.create_widgets()

    def create_widgets(self):
        # Set grid configurations for proper spacing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Task Name
        name_label = CTkLabel(
            self,
            text=f"{self.task.id}  {self.task.name}",
            font=("Arial", 14),
            anchor="w",
            text_color=self.text_color,
        )
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))

        # Task Duration
        duration_label = CTkLabel(
            self,
            text=f"{timedelta(seconds=self.task.duration_time)}",
            font=("Arial", 12),
            anchor="w",
            text_color="#8a8a8a",
        )
        duration_label.grid(row=1, column=0, sticky="w", padx=10, pady=2)

        # Time Left
        time_left_label = CTkLabel(
            self,
            text=f"{timedelta(seconds=self.task.time_left)}",
            font=("Arial", 12),
            anchor="w",
            text_color="#8a8a8a",
        )
        time_left_label.grid(row=1, column=1, sticky="e", padx=10, pady=2)

        # Button or Icon Area
        action_button = CTkButton(
            self,
            text="Start",
            width=80,
            height=30,
            corner_radius=8,
            fg_color="#1f6aa5",
            text_color=self.text_color,
        )
        action_button.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="e")
