from tkinter import *
from tkinter import ttk
import sv_ttk

HEIGHT = 400
WIDTH = 300

class Window:
    window = None;
    
    def __init__(self, title):
        # Configure the initial window.
        self.window = Tk()
        self.window.overrideredirect(True) # This removes the window borders.
        self.window.resizable(False, False)
        self.window.geometry(f"{WIDTH}x{HEIGHT}+0+0")
        self.window.attributes("-topmost", True)   
        self.window.title(title)    
        self.window.configure(bg='gray')
        
        # Draw the window head.
        self._draw_window_head();
        
        # Set the theme.
        sv_ttk.set_theme("dark")
        
        # Start the window.
        self.window.mainloop()  
        
    def func(): pass
    
    def _draw_window_head(self):
        f = Frame(self.window, height=HEIGHT, width=WIDTH, bg='gray')
        f.pack_propagate(0) # don't shrink
        f.place(x=0, y=0, width=WIDTH, height=30)
        
        button = ttk.Button(f, text="Hello world")
        button.pack(fill=BOTH, expand=1)