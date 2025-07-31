# f  to c
import tkinter as tk
root=tk.Tk()


def convert():
    f = float(entry.get())  # Get the Fahrenheit value from input
    c = (f - 32) * 5/9      # Convert to Celsius
    result.config(text=f"{c:.2f} °C")
root.geometry('600x400')
label1=tk.Label(text='this is Label',background='skyblue')
label1.place(x=10, y=10)

entry=tk.Entry(width=50)
entry.place(x=10,y=50)

result= tk.Label(root, text="", font=("Arial", 14))
result.pack(pady=10)

button1=tk.Button(text="covert",command=convert)
button1.place(x=200,y=7)

root.mainloop()