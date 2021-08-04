from urllib.request import urlopen, hashlib
import time


def dictionary_cracker(sha256hash):

    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read(), 'utf-8')

    attempts = 0
    start = time.time()

    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == sha256hash:
            end = time.time()
            final_time = end - start
            return (True, guess, attempts, final_time)
        elif hashedGuess != sha256hash:
            attempts += 1

    end = time.time()
    final_time = end - start
    
    return (False, guess, attempts, final_time)

if __name__ == "__main__":
    sha256hash = input("Please input the hash to crack.\n>")

    found, password, tries, timeAmount = dictionary_cracker(sha256hash)

    print("-"*60)
    if found:
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))
    else:
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (tries, timeAmount))
        


