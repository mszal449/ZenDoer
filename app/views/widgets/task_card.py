from datetime import timedelta

from customtkinter import CTkButton, CTkFrame, CTkImage, CTkLabel
from PIL import Image


class TaskCard(CTkFrame):
    text_color = "#d4d2d2"

    def __init__(self, task, master=None, button_action=None, **kwargs):
        super().__init__(master, **kwargs)
        self.task = task
        self.configure(corner_radius=5, fg_color="#3b3b3b")
        self.create_widgets()
        self.button_action = button_action

    def create_widgets(self):
        # Set grid configurations for proper spacing
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # Task Name
        name_label = CTkLabel(
            self,
            text=f"{self.task.name}",
            font=("Arial", 16),
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

        img = CTkImage(Image.open("app/static/start_button.png"))

        action_button = CTkButton(
            self,
            image=img,
            text="",
            width=20,
            height=20,
            fg_color="#25d3a2",
            hover_color="#9de8ca",
            cursor="hand2",
            command=lambda: self.button_action(self.task.id) if self.button_action else None,
        )
        action_button.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="e")
