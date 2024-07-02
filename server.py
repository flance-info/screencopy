import socket
from PIL import Image
from io import BytesIO
import win32clipboard
import threading
import time
import keyboard  # Import the keyboard module

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def receive_screenshot(server_socket):
    while not stop_event.is_set():
        try:
            server_socket.settimeout(1.0)  # Set timeout to allow periodic check of stop_event
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            image_data = b''
            while True:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                image_data += packet

            client_socket.close()

            image = Image.open(BytesIO(image_data))

            # Save image locally with a unique filename
            timestamp = int(time.time())
            filename = f'received_screenshot_{timestamp}.png'
            image.save(filename)
            print(f"Screenshot saved as {filename}")

            output = BytesIO()
            image.convert('RGB').save(output, format='BMP')
            data = output.getvalue()[14:]  # BMP files include a 14-byte header we need to remove
            output.close()

            send_to_clipboard(win32clipboard.CF_DIB, data)
            print("Screenshot copiedee to clipboard!")

        except socket.timeout:
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    stop_event = threading.Event()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all available interfaces
    server_socket.listen(1)
    print("Server is running and waiting for connections...")

    server_thread = threading.Thread(target=receive_screenshot, args=(server_socket,))
    server_thread.start()

    print("Press Esc to stop the server")

    keyboard.wait('esc')
    print("1 Server stopped.")
    stop_event.set()
    server_socket.close()
    server_thread.join()
    print("Server stopped.")
