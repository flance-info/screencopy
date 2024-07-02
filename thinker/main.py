import tkinter as tk
import threading
import os

def run_client():
    client_button.config(text="Client Processing...")
    threading.Thread(target=start_client).start()

def run_server():
    server_button.config(text="Server Processing...")
    threading.Thread(target=start_server).start()

def start_client():
    os.system('python client/client.py')
    client_button.config(text="Start Client")

def start_server():
    os.system('python server/main.py')
    server_button.config(text="Start Server")

app = tk.Tk()
app.title("Thinker")
app.geometry("300x200")

client_button = tk.Button(app, text="Start Client", command=run_client)
client_button.pack(pady=20)

server_button = tk.Button(app, text="Start Server", command=run_server)
server_button.pack(pady=20)

app.mainloop()
