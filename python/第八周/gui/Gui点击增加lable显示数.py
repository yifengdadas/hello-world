import tkinter as tk


root = tk.Tk()

label_one = tk.Label(root, text="0")
def buttonOnClick():
    newText = str(int(label_one.cget("text")) + 1)
    label_one.config(text=newText)

butto_one = tk.Button(master=root, command=buttonOnClick, text="点击计数")
label_one.pack()
butto_one.pack()
root.mainloop()
