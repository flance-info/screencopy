import tkinter as tk
import threading
import os
import subprocess

client_process = None
server_process = None

def run_client():
    global client_process
    client_button.config(text="Client Processing...")
    client_process = subprocess.Popen(['python', 'client/client.py'])
    stop_client_button.config(state=tk.NORMAL)
    stop_all_button.config(state=tk.NORMAL)

def run_server():
    global server_process
    server_button.config(text="Server Processing...")
    server_process = subprocess.Popen(['python', 'server/main.py'])
    stop_server_button.config(state=tk.NORMAL)
    stop_all_button.config(state=tk.NORMAL)

def stop_client():
    global client_process
    if client_process:
        client_process.terminate()
        client_process = None
        client_button.config(text="Start Client")
        stop_client_button.config(state=tk.DISABLED)
        if server_process is None:
            stop_all_button.config(state=tk.DISABLED)

def stop_server():
    global server_process
    if server_process:
        server_process.terminate()
        server_process = None
        server_button.config(text="Start Server")
        stop_server_button.config(state=tk.DISABLED)
        if client_process is None:
            stop_all_button.config(state=tk.DISABLED)

def stop_all():
    stop_client()
    stop_server()

app = tk.Tk()
app.title("Thinker")
app.geometry("300x300")

# Frame for client buttons
client_frame = tk.Frame(app)
client_frame.pack(pady=10)

client_button = tk.Button(client_frame, text="Start Client", command=run_client)
client_button.grid(row=0, column=0, padx=5)

stop_client_button = tk.Button(client_frame, text="Stop Client", command=stop_client, state=tk.DISABLED)
stop_client_button.grid(row=0, column=1, padx=5)

# Frame for server buttons
server_frame = tk.Frame(app)
server_frame.pack(pady=10)

server_button = tk.Button(server_frame, text="Start Server", command=run_server)
server_button.grid(row=0, column=0, padx=5)

stop_server_button = tk.Button(server_frame, text="Stop Server", command=stop_server, state=tk.DISABLED)
stop_server_button.grid(row=0, column=1, padx=5)

stop_all_button = tk.Button(app, text="Stop All", command=stop_all, state=tk.DISABLED)
stop_all_button.pack(pady=20)

app.mainloop()
