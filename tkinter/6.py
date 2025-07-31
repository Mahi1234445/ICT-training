import tkinter as tk
root=tk.Tk()
root.geometry('300x200')

frame_top=tk.Frame(root)
frame_top.pack(side=tk.TOP,pady=10)
frame_bottom=tk.Frame(root)
frame_bottom.pack(side=tk.TOP,pady=10)

label=tk.Label(frame_top,text='hello, tkinter!')
label.pack()

button=tk.Button(frame_bottom,text='Click Me',command=lambda:label.config(text='Button Clicked'))
button.pack()

root.mainloop()