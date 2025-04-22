import tkinter as tk
from tkinter import ttk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = 400
root_height = 300
middle_x_screen = (screen_width - root_width) // 2
middle_y_screen = (screen_height - root_height) // 2

root.title("Converter - Farenheit to Celsius")
root.geometry(f"{root_width}x{root_height}+{middle_x_screen}+{middle_y_screen}")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

root.mainloop()