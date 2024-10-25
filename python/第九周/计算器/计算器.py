import tkinter as tk

root = tk.Tk()
root.geometry("300x500")
root.title("计算器")
root.resizable(False, False)


display_area = tk.Frame(root, width=300, height=125)
display_area.pack(fill=tk.X, padx=0, pady=0) 

display_label = tk.Label(
    display_area, text="0", font=("Helvetica", 36, "bold"), anchor="e", justify="right"
)
display_label.pack(
    fill=tk.X, expand=True, padx=10, pady=10
)  

button_frame = tk.Frame(root, width=300, height=375, background="pink")
button_frame.pack(fill=tk.BOTH, padx=0, pady=0)

button_font = ("Helvetica", 18, "bold")
button_width = 10  
button_height = 50  
button_padx = 10  
button_pady = 10  


buttons = [
    ["CE", "C", "\u2190", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
]
button_list = []
row_index = 0
for row in buttons:
    col_index = 0
    for button_text in row:
        button = tk.Button(
            button_frame,
            text=button_text,
            font=button_font,
            width=button_width,
            height=button_height,
            padx=button_padx,
            pady=button_pady,
        )
        button.grid(row=row_index, column=col_index, sticky=tk.W + tk.E + tk.N + tk.S)
        button_list.append(button)
        col_index += 1
    row_index += 1


for i in range(5):  
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):  
    button_frame.grid_columnconfigure(i, weight=1)


root.mainloop()
