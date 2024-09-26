import sys
import os
import tkinter as tk
from view.gui import App

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.tokenize_button.config(command=app.parse_input)
    root.mainloop()
