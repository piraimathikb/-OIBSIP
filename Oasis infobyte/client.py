import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            print("Error receiving message or server disconnected.")
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except:
            print("Error sending message or disconnected.")
            break

def main():
    HOST = '127.0.0.1'  # Replace with server IP if needed
    PORT = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print("[Connected to server]\nStart chatting...\n")
    except:
        print("Unable to connect to server.")
        return

    # Start threads for sending and receiving
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    threading.Thread(target=send_messages, args=(client_socket,), daemon=True).start()

    # Keep main thread alive
    while True:
        pass

if __name__ == "__main__":
    main()
