import time
import crypt
from urllib import urlopen


def dictionary_cracker(shadow, shadowfull):

    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt').read())

    attempts = 0
    start = time.time()

    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        shadowGuess = crypt.crypt(guess, shadow)
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
    shadow = raw_input("Enter shadow>")
    shadowfull = raw_input("Enter shadowfull>")

    found, password, tries, timeAmount = dictionary_cracker(shadow, shadowfull)

    print("-"*60)
    if found:
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))
    else:
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (tries, timeAmount))
        


