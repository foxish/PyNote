import hashlib
import os
from sqlite.connections import PyNoteSqlite
from os.path import expanduser
import time


class Storage(object):
    DIR_NAME = ".pynote" # directory to store all notes
    DB_NAME = "pynote.db"
    
    # le constructeur (let us hope this is french)
    def __init__(self):
        self._path = os.path.join(expanduser("~"), Storage.DIR_NAME)
        self._directory_action() # check if directory exists, if not, create it
        self._sqlite = PyNoteSqlite(os.path.join(expanduser("~"), Storage.DIR_NAME, Storage.DB_NAME))
    
    # save the file to the user's home-dir specific folder
    def save_file(self, title, content):
        hashed_title = self._findhash(title)
        file_path = os.path.join(self._path, hashed_title)
        try:
            with open(file_path, 'w') as file_handle:
                file_handle.write(content)
            #successfully written to disk, now write to sqlite database
            self._sqlite.insert_value([title, time.time()])
            return True
        except OSError:
            return False
            
    def retrieve_file(self, title):
        hashed_title = self._findhash(title)
        file_path = os.path.join(self._path, hashed_title)
        try:
            with open(file_path, 'r') as file_handle:
                data = file_handle.read()
            return data
        except OSError:
            raise
    
    def delete_file(self, title):
        hashed_title = self._findhash(title)
        file_path = os.path.join(self._path, hashed_title)
        # remove sqlite entry
        self._sqlite.delete_value(title)
        try:
            os.remove(file_path)
            return True
        except OSError:
            return False
    
    # finding the sha224 hexdigest
    def _findhash(self, string):
        return hashlib.sha224(string).hexdigest()
      
    # deal with directory creation   
    def _directory_action(self):
        path = self._path
        try: 
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise

    def list_notes(self, filtered=False):
        if(filtered):
            return self._sqlite.get_filtered_values(filtered)
        else:
            return self._sqlite.get_all_values()
