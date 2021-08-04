import time
from crypt import crypt
from colorama import Fore as colors


def dictionary_cracker(shadowfull):


    LIST_OF_COMMON_PASSWORDS = open("passwords.txt")

    attempts = 0
    start = time.time()

    for guess in LIST_OF_COMMON_PASSWORDS.readlines():
        guess = guess.rstrip()
        shadowGuess = crypt(guess, shadowfull)
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
    shadowfull = input(colors.YELLOW +  "Enter shadowfull> ")

    found, password, tries, timeAmount = dictionary_cracker(shadowfull)

    print(colors.CYAN + "-" * 60 + colors.RESET)
    if found:
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))
    else:
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (tries, timeAmount))
        






