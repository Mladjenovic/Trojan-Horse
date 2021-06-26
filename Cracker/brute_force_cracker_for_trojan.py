import itertools
import time
import crypt


def brute_force_cracker(shadow, shadowfull):
    start = time.time()
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            shadowGuess = crypt.crypt(letter, shadow)
            if shadowGuess == shadowfull:
                end = time.time()
                final_time = end - start
                return (letter, attempts, final_time)


if __name__ == "__main__":
    shadow = raw_input("Enter shadow>" )
    shadowfull = raw_input("Enter shadowfull> ")
    # Allowed characters
    password, tries, timeAmount = brute_force_cracker(shadow, shadowfull)
    print("Brute force cracker cracked the password '%s' in %s tries and %s seconds!" % (password, tries, timeAmount))

