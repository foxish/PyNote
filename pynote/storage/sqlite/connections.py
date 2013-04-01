from sqlitehelper import SqliteHelper

class PyNoteSqlite():
    TABLE_NAME = "snips"
    TABLE_QUERY = "CREATE TABLE if not exists %s (title TEXT PRIMARY KEY, time INTEGER)" % TABLE_NAME
    INSERT_QUERY = "INSERT INTO %s VALUES(?, ?)" % TABLE_NAME
    SELECT_QUERY = "SELECT title FROM %s ORDER BY time DESC" % TABLE_NAME
    SELECT_FILTERED_QUERY = "SELECT title FROM %s WHERE title LIKE ? ORDER BY time DESC" % TABLE_NAME
    DELETE_QUERY = "DELETE FROM %s WHERE title = ?" % TABLE_NAME
    
    # create instance of sqlite helper class &  create a table
    def __init__(self, db_path):
        self.sqlite_helper = SqliteHelper(db_path)
        self.sqlite_helper.do_modification(PyNoteSqlite.TABLE_QUERY)
    
    # inserts values supplied into table
    def insert_value(self, args):
        self.sqlite_helper.do_modification(PyNoteSqlite.INSERT_QUERY, args)
    
    # gets values from table
    def get_all_values(self):
        return self.sqlite_helper.do_selection(PyNoteSqlite.SELECT_QUERY)
        
    # gets values from table
    def get_filtered_values(self, arg):
        return self.sqlite_helper.do_selection(PyNoteSqlite.SELECT_FILTERED_QUERY, ["%" + arg + "%"])
        
    # delete a value from the table
    def delete_value(self, arg):
        self.sqlite_helper.do_modification(PyNoteSqlite.DELETE_QUERY, [arg])
