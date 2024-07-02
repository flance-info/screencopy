import socket
from PIL import ImageGrab
from io import BytesIO
import keyboard
import time
import win32clipboard

def send_screenshot():
    # Give some time for the screenshot to be copied to the clipboard
    time.sleep(1)

    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
        win32clipboard.CloseClipboard()

        image = ImageGrab.grabclipboard()
        if image is None:
            print("No image found in clipboard.")
            return

        buffer = BytesIO()
        image.save(buffer, format='PNG')
        image_data = buffer.getvalue()
        buffer.close()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 12345))  # Use localhost IP address for the same PC
        client_socket.sendall(image_data)
        client_socket.close()
        print("Screenshot sent!")
    except Exception as e:
        print(f"Failed to send screenshot: {e}")

if __name__ == "__main__":
    print("Press Alt+PrtSc to send a screenshot of the active window")
    keyboard.add_hotkey('alt+print screen', send_screenshot)  # Use Alt + PrtSc for the active window

    # Keep the script running
    keyboard.wait('esc')  # Press 'Esc' to stop the script
