import hashlib

def sha256_fun(password:str):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha256(setpass)
    guess_pw = hash_object.hexdigest()
    return guess_pw

if __name__ == "__main__":
    guess_pw = sha256_fun("321")
    print(f"SHA256: {guess_pw}")
    


