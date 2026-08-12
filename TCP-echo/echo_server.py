import socket

# 1. Define the host and port
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (use an unprivileged port > 1023)

# 2. Create the socket object
# AF_INET = IPv4, SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # 3. Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # 4. Listen for incoming connections
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    # 5. Accept a connection (This line blocks/waits until a client connects)
    conn, addr = s.accept()
    
    with conn:
        print(f"Connected by {addr}")
        while True:
            # 6. Receive data (up to 1024 bytes at a time)
            data = conn.recv(1024)
            if not data:
                break # If no data is received, the client disconnected
            
            print(f"Received: {data.decode()}")
            
            # 7. Echo it back to the client
            conn.sendall(data)