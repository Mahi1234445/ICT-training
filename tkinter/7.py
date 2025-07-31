import tkinter as tk
root=tk.Tk()
root.geometry('600x400')



label1=tk.Label(text='this is Label',background='skyblue')
label1.place(x=10 , y=10)
button=tk.Button(text='Click Me',command=lambda:label1.config(text='Button Clicked'))
button.place(x=520 , y=10)

entry=tk.Entry(width=94)
entry.place(x=10,y=50)

entry2=tk.Entry(width =94)
entry2.place(x=10,y=80,height= 100)

rad1=tk.Radiobutton(root,text='option1' ,value=1)
rad1.grid(row=5,column=3,padx=10,pady=10,sticky='e')

opt1=tk.Checkbutton()
opt1.place(x=450,y=200)
label2=tk.Label(text='Option 1')
label2.place(x=500 , y=200)

opt2=tk.Checkbutton()
opt2.place(x=450,y=230)
label3=tk.Label(text='Option 2')
label3.place(x=500 , y=230)

root.mainloop()