from dictionary_cracker import dictionary_cracker
from brute_force_cracker import brute_force_cracker

def combined_cracker():
    brute_force_cracker


if __name__ == "__main__":
    sha256hash = input("Please input the hash to crack.\n>")

    dict_found, dict_password, dict_tries, dict_timeAmount = dictionary_cracker(sha256hash)

    if not dict_found:
        print("-"*60)
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (dict_tries, dict_timeAmount))
        
        brute_password, brute_tries, brute_timeAmount = brute_force_cracker(sha256hash)
        print("Brute force cracker cracked the password '%s' in %s tries and %s seconds!" % (brute_password, brute_tries, brute_timeAmount))
    else:
        print("-"*60)
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (dict_password, dict_tries, dict_timeAmount))
