import tkinter as tk 

def scale_changed(value):
    label.config(text=f"Value: {value}")  # Update label when scale moves

root = tk.Tk()
root.title("Scale Widget Example")
root.geometry("400x200")

# Frame to hold widgets
frame = tk.Frame(root)
frame.pack(pady=20)

# Scale widget
scale = tk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=scale_changed)
scale.pack(pady=10)

# Label to show scale value
label = tk.Label(frame, text="Value: 0", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()
