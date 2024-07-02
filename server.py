import socket
from PIL import Image
from io import BytesIO
import win32clipboard

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def receive_screenshot():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Bind to all available interfaces
    server_socket.listen(1)
    print("Server is running and waiting for connections...")

    while True:
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

        # Save image locally to verify it's received correctly (optional)
        image.save('received_screenshot.png')

        output = BytesIO()
        image.convert('RGB').save(output, format='BMP')
        data = output.getvalue()[14:]  # BMP files include a 14-byte header we need to remove
        output.close()

        send_to_clipboard(win32clipboard.CF_DIB, data)
        print("Screenshot copied to clipboard!")

if __name__ == "__main__":
    receive_screenshot()
