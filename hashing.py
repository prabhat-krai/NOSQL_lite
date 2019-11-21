import hashlib
salt = '8f3671dc714a45d4afc60ccaec358020' #defauting to one salt to show the implementation

def hash_key(key):
    return hashlib.sha256(salt.encode() + key.encode()).hexdigest() #hashing with sha256 algorithm
    
    
 

