import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import socket
import threading

# 全局变量
clients = {}  # 存储已连接客户端的信息
pending_requests = set()  # 存储已处理的好友请求地址
username = None  # 当前用户的用户名
server_socket = None  # 服务器套接子
HOST = '0.0.0.0'  # 本地监听地址
PORT = 12345  # 通信端口

# 自动与局域网内的其他用户连接
BROADCAST_PORT = 12346  # 广播端口

def login():
    global username
    username = simpledialog.askstring("登录", "请输入您的用户名：")
    if not username:
        messagebox.showerror("错误", "用户名不能为空！")
        root.destroy()

def start_server():
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
    try:
        client_name = client_socket.recv(1024).decode('utf-8')
        if client_name.startswith("FRIEND_REQUEST"):
            handle_friend_request(client_socket, client_address, client_name)
            return
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

def handle_friend_request(client_socket, client_address, client_name):
    if client_address not in pending_requests:
        pending_requests.add(client_address)
        response = messagebox.askyesno("好友请求", f"{client_name.split(':', 1)[1]} 请求添加您为好友，是否同意？")
        if response:
            client_socket.sendall("ACCEPTED".encode('utf-8'))
            clients[client_address] = (client_socket, client_name.split(':', 1)[1])
            update_user_list()
            display_message(f"已接受 {client_address} 的好友请求")
        else:
            client_socket.sendall("DECLINED".encode('utf-8'))
    client_socket.close()

def send_message():
    message = message_input.get()
    if not message.strip():
        return
    for client_socket, _ in clients.values():
        client_socket.sendall(f"{username}: {message}".encode('utf-8'))
    display_message(f"Me: {message}")
    message_input.delete(0, tk.END)

def send_private_message():
    selected = user_list.curselection()
    if not selected:
        messagebox.showerror("错误", "请选择一位好友进行私聊！")
        return
    addr = list(clients.keys())[selected[0]]
    client_socket, _ = clients[addr]
    message = message_input.get()
    if not message.strip():
        return
    client_socket.sendall(f"{username}: {message}".encode('utf-8'))
    display_message(f"私聊({addr}): {message}")
    message_input.delete(0, tk.END)

def display_message(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{message}\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def update_user_list():
    user_list.delete(0, tk.END)
    for addr, (_, name) in clients.items():
        user_list.insert(tk.END, f"{name} ({addr})")

def add_friend():
    ip = simpledialog.askstring("添加好友", "请输入好友的IP地址：")
    port = simpledialog.askinteger("添加好友", "请输入好友的端口：")
    if not ip or not port:
        messagebox.showerror("错误", "IP地址或端口不能为空！")
        return

    try:
        friend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        friend_socket.connect((ip, port))
        friend_socket.sendall(f"FRIEND_REQUEST:{username}".encode('utf-8'))
        response = friend_socket.recv(1024).decode('utf-8')
        if response == "ACCEPTED":
            clients[(ip, port)] = (friend_socket, f"好友({ip})")
            update_user_list()
            display_message(f"成功添加好友：{ip}")
        elif response == "DECLINED":
            display_message(f"好友请求被拒绝：{ip}")
    except Exception as e:
        messagebox.showerror("错误", f"无法连接到好友：{e}")

def discover_users():
    def broadcast():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as broadcast_socket:
            broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            while True:
                broadcast_socket.sendto(f"DISCOVER:{username}".encode('utf-8'), ('<broadcast>', BROADCAST_PORT))
                threading.Event().wait(5)

    def listen_for_broadcast():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listener_socket:
            listener_socket.bind((HOST, BROADCAST_PORT))
            while True:
                data, addr = listener_socket.recvfrom(1024)
                if addr not in clients and addr[0] != socket.gethostbyname(socket.gethostname()):
                    threading.Thread(target=add_friend_from_broadcast, args=(addr[0],)).start()

    threading.Thread(target=broadcast, daemon=True).start()
    threading.Thread(target=listen_for_broadcast, daemon=True).start()

def add_friend_from_broadcast(ip):
    try:
        friend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        friend_socket.connect((ip, PORT))
        friend_socket.sendall(f"FRIEND_REQUEST:{username}".encode('utf-8'))
        response = friend_socket.recv(1024).decode('utf-8')
        if response == "ACCEPTED":
            clients[(ip, PORT)] = (friend_socket, f"好友({ip})")
            update_user_list()
    except Exception:
        pass

# GUI
root = tk.Tk()
root.title("局域网聊天")

chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

message_input = tk.Entry(root)
message_input.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(root, text="群发", command=send_message)
send_button.pack(side=tk.LEFT, padx=5, pady=5)

private_button = tk.Button(root, text="私聊", command=send_private_message)
private_button.pack(side=tk.LEFT, padx=5, pady=5)

user_list = tk.Listbox(root)
user_list.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

root.protocol("WM_DELETE_WINDOW", root.destroy)

login()
start_server()
discover_users()
root.mainloop()