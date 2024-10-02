from general import actions
from general import stats
import tkinter as tk
from tkinter import ttk

class GameApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Adventure Time")
        self.window.geometry('800x500')
        self.window.config(bg='lightblue')
        # Left Frame
        self.secondary_frame = tk.Frame(self.window, bg="orange", width=200)
        self.secondary_frame.grid(row=0, column=0, sticky="ns")  # Fill vertically

        # Main Frame
        self.main_frame = tk.Frame(self.window, bg="lightblue")
        self.main_frame.grid(row=0, column=1, sticky="nsew")  # Fill both horizontally and vertically

        # Configure grid weights
        self.window.grid_columnconfigure(1, weight=1)  # Allow the main frame to expand
        self.window.grid_rowconfigure(0, weight=1)

        actions.input_to_play(self.main_frame, self.secondary_frame)  # Use main_frame for actions

    def process_input(self):
        actions.what_to_do(self.window, self.secondary_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
