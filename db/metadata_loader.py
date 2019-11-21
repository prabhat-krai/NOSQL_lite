from .index_of_db import load_index

#loads at the start and takes the data from json files that keep the 
#info of data stored
#This provides the data for DB to function after restarts too. 

map_of_db = load_index("map_of_db")
reverse_index = load_index("reverse_index")

