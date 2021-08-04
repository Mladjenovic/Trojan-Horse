from dictionary_cracker_for_trojan import dictionary_cracker
from brute_force_cracker_for_trojan import brute_force_cracker
import crypt

#python -c 'import crypt; print crypt.crypt("test", "$6$random_salt")'

def combined_cracker():
    brute_force_cracker


if __name__ == "__main__":
    shadowfull = input("Enter shadowfull> ")

    dict_found, dict_password, dict_tries, dict_timeAmount = dictionary_cracker(shadowfull)

    if not dict_found:
        print("-"*60)
        print("Dictionary cracker failed to crack the password. Tries: %s Time: %s seconds" % (dict_tries, dict_timeAmount))
        
        brute_password, brute_tries, brute_timeAmount = brute_force_cracker(shadowfull)
        print("Brute force cracker cracked the password '%s' in %s tries and %s seconds!" % (brute_password, brute_tries, brute_timeAmount))
    else:
        print("-"*60)
        print("Dictionary cracker cracked the password '%s' in %s tries and %s seconds!" % (dict_password, dict_tries, dict_timeAmount))
