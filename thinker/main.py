import tkinter as tk
import threading
import os

def run_client():
    os.system('python client/client.py')

def run_server():
    os.system('python server/main.py')

app = tk.Tk()
app.title("Thinker")
app.geometry("300x200")

client_button = tk.Button(app, text="Start Client", command=lambda: threading.Thread(target=run_client).start())
client_button.pack(pady=20)

server_button = tk.Button(app, text="Start Server", command=lambda: threading.Thread(target=run_server).start())
server_button.pack(pady=20)

app.mainloop()
