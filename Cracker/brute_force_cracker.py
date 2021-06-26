import itertools
from urllib.request import  hashlib
import time


def brute_force_cracker(sha256hash):
    start = time.time()
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            hashedGuess = hashlib.sha256(bytes(letter, 'utf-8')).hexdigest()
            if hashedGuess == sha256hash:
                end = time.time()
                final_time = end - start
                return (letter, attempts, final_time)


if __name__ == "__main__":
    sha256hash = input("Enter SHA256 hash >")
    # Allowed characters
    password, tries, timeAmount = brute_force_cracker(sha256hash)
    print("Brute force cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))

