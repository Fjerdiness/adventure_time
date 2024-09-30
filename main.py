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
        

        actions.input_to_play(self.window)

    def process_input(self):
        actions.what_to_do(self.window)
        
        # self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
