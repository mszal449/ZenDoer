from customtkinter import CTkFrame


class BaseView(CTkFrame):
    def __init__(self, master=None, width=800, height=600, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.width = width
        self.height = height
