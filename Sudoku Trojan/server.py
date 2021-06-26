import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432

def connection():
    while True:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            print('Server open on '+HOST + ':'+str(PORT)+' and listening!')
            conn, addr = s.accept()
           
            while True:
                try:
                    print(conn.recv(2048).decode('utf-8'))
                    data = input('Enter command: ')
                    conn.send(data.encode('utf-8'))
                    if data == 'exit':
                        return
                    
                except:
                    break

if __name__ == "__main__":
    connection()