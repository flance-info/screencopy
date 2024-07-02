import socket
import pyautogui
from PIL import Image
from io import BytesIO
import keyboard

def send_screenshot():
    screenshot = pyautogui.screenshot()
    buffer = BytesIO()
    screenshot.save(buffer, format='PNG')
    image_data = buffer.getvalue()
    buffer.close()

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))  # Use localhost IP address for the same PC
        client_socket.sendall(image_data)
        client_socket.close()
        print("Screenshot sent!")
    except ConnectionRefusedError:
        print("Failed to connect to the server. Make sure the server is running.")

if __name__ == "__main__":
    print("Press Ctrl+M to send a screenshot")
    keyboard.add_hotkey('ctrl+m', send_screenshot)

    # Keep the script running
    keyboard.wait('esc')  # Press 'Esc' to stop the script
