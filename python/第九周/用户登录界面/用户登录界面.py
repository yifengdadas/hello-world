import tkinter as tk


window=tk.Tk()
window.title("登录")

label_username=tk.Label(window,text="用户名:")
label_username.grid(row=0,column=0)
entry_username=tk.Entry(window)
entry_username.grid(row=0,column=1)

label_password=tk.Label(window,text="密码:")
label_password.grid(row=1,column=0)
entry_password=tk.Entry(window,show="*")
entry_password.grid(row=1,column=1)

def login():
    username=entry_username.get()
    password=entry_password.get()
    print(f"用户名:{username},密码:{password}")
    
login_button=tk.Button(window,text="登录",command=login)    
login_button.grid(row=2,column=1)

window.mainloop()
