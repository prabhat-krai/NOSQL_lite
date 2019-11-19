import hashlib

salt = '8f3671dc714a45d4afc60ccaec358020'
def hash_key(key):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_key(hashed_key, dictionary):
    if(hashed_key in dictionary):
        return True
    else:
        return False
 

