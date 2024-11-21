import customtkinter
from customtkinter import *
from db import init_db

from app import App

init_db()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


app = App()
app.mainloop()
