import hashlib
from index_of_db import check_for_record

salt = '8f3671dc714a45d4afc60ccaec358020' 

def hash_key(key):
    return hashlib.sha256(salt.encode() + key.encode()).hexdigest()
    
def check_key(hashed_key):
    presence_in_db = check_for_record(hashed_key)
    return presence_in_db
 

