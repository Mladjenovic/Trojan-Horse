import time
import crypt
from urllib.request import urlopen


def dictionary_cracker(shadowfull):

    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read())

    attempts = 0
    start = time.time()

    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        shadowGuess = crypt.crypt(guess, shadowfull)
        if shadowGuess == shadowfull:
            end = time.time()
            final_time = end - start
            return (True, guess, attempts, final_time)
        elif shadowGuess != shadowfull:
            attempts += 1

    end = time.time()
    final_time = end - start
    
    return (False, guess, attempts, final_time)

if __name__ == "__main__":
    shadowfull = input("Enter shadowfull> ")

    found, password, tries, timeAmount = dictionary_cracker(shadowfull)

    print("-"*60)
    if found:
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))
    else:
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (tries, timeAmount))
        


