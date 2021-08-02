from colorama import Fore as colors
from os import getuid
from crypt import crypt
from spwd import getspnam

from sys import argv

def main():
    if(getuid() != 0):                                                  # $uid == 0 is for ROOT user
        print(colors.YELLOW + "You must be root to run this utility.")
        exit(1)
    
    if(len(argv) <= 1):
        username = input(colors.YELLOW + "What user should we try and crack the password  for?" + colors.RESET)
    else:
        username = argv[1]
        

    print(colors.CYAN + "Cracking UNIX password for user... " + username + colors.RESET)
    
    dict_file = open("passwords.txt")
    encrypted_password = getspnam(username)[1]                           # omiting the indexing gets the full array for shadow file in parts

    print(colors.RED +  "Encrypted password is: " + encrypted_password + "\n")
    
    count = 0 

    for password in dict_file.readlines():
        password = password.rstrip()
        new_password = crypt(password, encrypted_password)

        print(colors.MAGENTA +  "Trying password: " + password + "\n")

        if(encrypted_password == new_password):
            print(colors.GREEN +  "Password found" + "\n")
            print(colors.WHITE + "It took "  + str(count) + " tries to crack the password\n")
            print(colors.RESET +  "The cracked password is: " + colors.GREEN + password)
            exit(0)
        else:
            print(colors.RED +  "Password failed..." + "\n")
            count += 1
    
    exit(1)


if (__name__ == '__main__'):
    main()