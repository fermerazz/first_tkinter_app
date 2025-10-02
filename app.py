import tkinter as tk 
from tkinter import ttk 

root = tk.Tk() #Window object
ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack() #Passing the parent

root.mainloop()#Code to run the window object