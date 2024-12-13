import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import socket
import threading

# 全局变量
clients = {}  # 存储已连接客户端的信息
username = None  # 当前用户的用户名
server_socket = None  # 服务器套接子
HOST = '0.0.0.0'  # 本地监听地址
PORT = 12345  # 通信端口

# 自动与局域网内的其他用户连接
BROADCAST_PORT = 12346  # 广播端口

def login():
    """
    登录功能：用户输入用户名
    """
    global username
    username = simpledialog.askstring("登录", "请输入您的用户名：")
    if not username:
        messagebox.showerror("错误", "用户名不能为空！")
        root.destroy()

def start_server():
    """
    启动服务器线程，监听新连接
    """
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    def accept_connections():
        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

    threading.Thread(target=accept_connections, daemon=True).start()

def handle_client(client_socket, client_address):
    """
    处理客户端消息接收
    """
    try:
        client_name = client_socket.recv(1024).decode('utf-8')  # 接收用户名
        clients[client_address] = (client_socket, client_name)
        update_user_list()
        display_message(f"{client_name} ({client_address}) 已加入聊天")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            display_message(f"{client_name}: {message}")
    except ConnectionResetError:
        pass
    finally:
        if client_address in clients:
            display_message(f"{clients[client_address][1]} ({client_address}) 已退出")
            del clients[client_address]
        update_user_list()
        client_socket.close()

def send_message():
    """
    发送消息给所有已连接客户端
    """
    message = message_input.get()
    if not message.strip():
        return
    for client_socket, _ in clients.values():
        client_socket.sendall(f"{username}: {message}".encode('utf-8'))
    display_message(f"Me: {message}")
    message_input.delete(0, tk.END)

def display_message(message):
    """
    在消息框中显示消息
    """
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def update_user_list():
    """
    更新已连接用户列表
    """
    user_list.delete(0, tk.END)
    for addr, (_, name) in clients.items():
        user_list.insert(tk.END, f"{name} ({addr})")

def add_friend():
    """
    通过IP和端口添加好友
    """
    ip = simpledialog.askstring("添加好友", "请输入好友的IP地址：")
    port = simpledialog.askinteger("添加好友", "请输入好友的端口：")
    if not ip or not port:
        messagebox.showerror("错误", "IP地址或端口不能为空！")
        return

    try:
        friend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        friend_socket.connect((ip, port))
        friend_socket.sendall(username.encode('utf-8'))  # 发送用户名
        clients[(ip, port)] = (friend_socket, f"好友({ip})")
        update_user_list()

        def receive_friend_messages():
            while True:
                try:
                    message = friend_socket.recv(1024).decode('utf-8')
                    display_message(f"{ip}: {message}")
                except ConnectionResetError:
                    break

        threading.Thread(target=receive_friend_messages, daemon=True).start()
    except Exception as e:
        messagebox.showerror("错误", f"无法连接到好友：{e}")

def discover_users():
    """
    实现局域网内自动连接其他用户
    """
    def broadcast():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as broadcast_socket:
            broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            while True:
                broadcast_socket.sendto(username.encode('utf-8'), ('<broadcast>', BROADCAST_PORT))
                threading.Event().wait(5)  # 每5秒广播一次

    def listen_for_broadcast():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener_socket:
            listener_socket.bind((HOST, BROADCAST_PORT))
            while True:
                data, addr = listener_socket.recvfrom(1024)
                if addr not in clients and addr[0] != socket.gethostbyname(socket.gethostname()):
                    threading.Thread(target=add_friend_from_broadcast, args=(addr[0],)).start()

    def add_friend_from_broadcast(ip):
        try:
            friend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            friend_socket.connect((ip, PORT))
            friend_socket.sendall(username.encode('utf-8'))
            clients[(ip, PORT)] = (friend_socket, f"好友({ip})")
            update_user_list()

            def receive_friend_messages():
                while True:
                    try:
                        message = friend_socket.recv(1024).decode('utf-8')
                        display_message(f"{ip}: {message}")
                    except ConnectionResetError:
                        break

            threading.Thread(target=receive_friend_messages, daemon=True).start()
        except Exception as e:
            print(f"无法连接到用户 {ip}: {e}")

    threading.Thread(target=broadcast, daemon=True).start()
    threading.Thread(target=listen_for_broadcast, daemon=True).start()

# GUI
# GUI
root = tk.Tk()
root.title("局域网聊天程序")
root.geometry("600x400")

# 消息显示框
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_window.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# 消息输入框和发送按钮
message_frame = tk.Frame(root)
message_frame.pack(padx=10, pady=5, fill=tk.X)

message_input = tk.Entry(message_frame)
message_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_button = tk.Button(message_frame, text="发送", command=send_message)
send_button.pack(side=tk.RIGHT)

# 用户列表框
user_list_frame = tk.Frame(root)
user_list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

user_list_label = tk.Label(user_list_frame, text="已连接用户")
user_list_label.pack(anchor=tk.W)

user_list = tk.Listbox(user_list_frame)
user_list.pack(fill=tk.BOTH, expand=True)

# 功能按钮
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=5, fill=tk.X)

add_friend_button = tk.Button(button_frame, text="添加好友", command=add_friend)
add_friend_button.pack(side=tk.LEFT, padx=(0, 5))

# 登录和启动服务器
login()
start_server()
discover_users()

# 启动主循环
root.mainloop()
