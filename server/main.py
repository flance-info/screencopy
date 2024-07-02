import threading
from .broadcast import broadcast_ip
from .receive import receive_screenshot

if __name__ == "__main__":
    threading.Thread(target=broadcast_ip, daemon=True).start()
    receive_screenshot()
