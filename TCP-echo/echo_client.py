import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# 1. Create the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # 2. Connect to the server
    s.connect((HOST, PORT))
    
    # 3. Get input from the user
    message = input("Enter a message to send: ")
    
    # 4. Send the message (Notice we use .encode() to turn the string into bytes)
    s.sendall(message.encode())
    
    # 5. Receive the server's response
    data = s.recv(1024)

print(f"Received back from server: {data.decode()}")