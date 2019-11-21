NoSQL DB that takes json as input. 
==================================

The project has been done using Python 3.5.6 and only inbuilt libraries are used.
No other installations are required.

Access the CLI for NoSQL through main.py

## My implementation:

1) I am storing individual inputs as json files in db folder. 

2) A metadata is maintained for the db to increase query speeds.

3) Two files contain the metadeta.

    a) map_of_db = This contains a hash map that has the names of all the keys in database to increase
                   the speed of searching a file for deletion. This helps us avoid scanning all data 
                   to find the desired key. 

    b) reverse_index = This maps every value that has been passed through inputs to files that they are 
                       stored in. So, when a search query is made for a value. This hash map is searched
                       all the files are extracted from it. These files have the required data and avoids
                       going through all the files which are stored on hard disk and will take linear time
                       to the number of records stored. While the hash map will be O(1) in the best case till
                       collisions start but will still be significantly faster than reading each file to find the queried value.
    
4) When a file is added. It is processed for all the values and they are stored in reverse index and map of db is updated. 

5) The keys are hashed while storing to make them unsearchable by keys in folder structure to show a prototype of security that can be implemented.

6) When key/s is/are given to delete from db. They are checked against map of db for their presence. The reverse index is updated to remove mappings to the file that has been deleted.

7) Search for keys is optimized using reverse index. The value is used to find the map of files to return to user. If the user has given fields that they require then only those fields are returned. 