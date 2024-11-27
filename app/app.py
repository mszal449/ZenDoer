from typing import Type

import customtkinter

from app.services import TaskService
from app.views import FocusView


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.task_service = TaskService()

        self.title("ZenDoer")
        self.geometry("800x600")
        self.view = None
        self.set_view(FocusView)

    def set_view(self, view: Type[FocusView]):
        # Destroy current view
        if self.view:
            self.view.destroy()

        # Initialize new view
        self.view = view(self)
        self.view.pack(fill="both", expand=True)
        self.resize(self.view.width, self.view.height)

    def resize(self, x, y):
        self.geometry(f"{x}x{y}")
