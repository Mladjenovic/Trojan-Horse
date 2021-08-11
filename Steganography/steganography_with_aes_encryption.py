"""
    This is a steganography example program using least segnificant bit method
    for storing bits of an message into the least segnificant bit od an pixel in an image 
    Further optimizations would include: 
            Encode an entire file of any type in an image.
            Use 2-Least Significant Bits technique to encode more data.
            Encode massive amount of data in videos instead of images (you can do this with OpenCV
            as videos are just sequence of images).
"""

import cv2
import numpy as np
from AES_Cipher import AESCipher


def to_bin(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


def encode(image_name, secret_data):
    # read the image
    image = cv2.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("[*] Maximum bytes to encode:", n_bytes)
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    print("[*] Encoding data...")
    # add stopping criteria
    secret_data += "====="
    data_index = 0
    # convert data to binary
    binary_secret_data = to_bin(secret_data)
    # size of data to hide
    data_len = len(binary_secret_data)
    for row in image:
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = to_bin(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image


def decode(image_name, AESCipher_object):
    print("[+] Decoding...")
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break

    decoded_from_img = decoded_data[:-5]
    decrypted_msg = AESCipher_object.decrypt(str(decoded_from_img) + "=")

    return decrypted_msg


if __name__ == "__main__":
    input_image = input("Enter input image (with file extension): ")

    output_image = input("Enter output image name (with file extension): ")

    secret_data = input("Enter message you want to encode: ")

    aes_kljuc = input("Enter key for aes encryption: ")
    AESCipher_object = AESCipher(str(aes_kljuc))
    aes_key = AESCipher_object.key
    # print("________________AES KEY__________________")
    # print(aes_key)

    encrypted = AESCipher_object.encrypt(secret_data)
    print(f"encrypted secret data is: {encrypted}")


    # encode the data into the image
    encoded_image = encode(image_name=input_image, secret_data=str(encrypted))
    # save the output image (encoded image)
    cv2.imwrite(output_image, encoded_image)
    # decode the secret data from the image
    decoded_data = decode(output_image, AESCipher_object)
    print("[+] Decoded data:", decoded_data)
