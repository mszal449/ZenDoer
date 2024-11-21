from customtkinter import CTkFrame, CTkLabel, CTkProgressBar

from .base_view import BaseView


class FocusView(BaseView):
    def __init__(self, master=None, width=300, height=800, **kw):
        super().__init__(master, width, height, **kw)
        self.max_width = 300
        self.max_height = 800
        self.add_widgets()

    def add_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.add_progress_bar()
        # self.add_task_panel()

    def add_progress_bar(self):
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
        progress_label.grid(row=0, column=1, sticky="e", padx=10)

    def add_timer(self):
        pass

    # def add_task_panel(self):
    #     frame = CTkFrame(self)
    #     frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    #
