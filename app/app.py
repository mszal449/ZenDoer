from typing import Type

import customtkinter

from app.db import init_db
from app.views import FocusView


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.title("ZenDoer")
        self.geometry("800x600")
        self.view = None
        self.set_view(FocusView)

    """
        This method starts main loop of application and initializes db connection.

    """

    def start(self):
        init_db()

        self.mainloop()

    """
        This method sets the current view of the application.
        The size of the window is adjusted to fit the view.

        Parameters:
        view (BaseView): The view to set as the current view.

    """

    def set_view(self, view: Type[FocusView]):
        # Destroy current view
        if self.view:
            self.view.destroy()

        # Initialize new view
        self.view = view(self)
        self.view.pack(fill="both", expand=True)
        self.resize(self.view.width, self.view.height)

    """
        This method resizes the application window to the specified width and height.

        Parameters:
        x (int): The width to resize the window to.
        y (int): The height to resize the window to.
    """

    def resize(self, x, y):
        self.geometry(f"{x}x{y}")
