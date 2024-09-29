from general import actions
from general import stats
import tkinter as tk
from tkinter import ttk

class GameApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Adventure Time")
        self.window.geometry('800x500')
        actions.input_to_play(self.window)
        # stats.set_character_stats(self.window)
        # stats.show_stats()
        
        # self.label = tk.Label(root, text="What would you like to do?")
        # self.label.pack()
        
        # self.entry = tk.Entry(root)
        # self.entry.pack()
        
        # self.submit_button = tk.Button(root, text="Submit", command=self.process_input)
        # self.submit_button.pack()

    def process_input(self):
        user_input = self.entry.get()
        where_to = actions.what_to_do(user_input)
        actions.process_user_input(where_to)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
