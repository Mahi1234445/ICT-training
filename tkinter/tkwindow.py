import tkinter as tk
from tkinter import PhotoImage
root=tk.Tk()
icon = PhotoImage(file="C:/Users/HP/Desktop/ChatGPT Image Jul 2, 2025, 02_27_01 AM.png")

root.title("my tkinter app")
root.iconphoto(True,icon)
root.geometry("500x500")
root.mainloop()
