import socket
from AES_Cipher import AESCipher
from steganography_with_aes_encryption import encode, decode


def image_server():

    HOST = 'localhost'
    PORT = 1002

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IP, SOCK_STREAM = TCP
    server.bind((HOST, PORT)) #127.0.0.1
    server.listen()

    print("IMAGE Server: Waiting for connection")

    client_socket, client_address = server.accept()

    shadow_image_name = 'serveer_image.png'
    file = open(shadow_image_name, "wb")

    image_chunk = client_socket.recv(2048)

    while image_chunk:
        file.write(image_chunk)
        image_chunk = client_socket.recv(2048)

    file.close()
    client_socket.close()

    aes_kljuc = '123'
    AESCipher_object = AESCipher(str(aes_kljuc))
    aes_key = AESCipher_object.key


    decoded_data = decode(shadow_image_name, AESCipher_object)
    print("[+] Decoded data:", decoded_data)


if __name__ == '__main__':

    image_server()

