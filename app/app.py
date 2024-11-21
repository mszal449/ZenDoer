from typing import Type

from customtkinter import CTk

from .views import FocusView


class App(CTk):
    def __init__(self):

        super().__init__()
        self.title("ZenDoer")
        self.geometry("800x600")
        self.view = None
        self.set_view(FocusView)

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
