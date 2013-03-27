from sqlitehelper import SqliteHelper

class PyNoteSqlite():
    DB_NAME = "test.db"
    TABLE_NAME = "snips"
    TABLE_QUERY = "CREATE TABLE if not exists %s (title text, note text)" % TABLE_NAME
    INSERT_QUERY = "INSERT INTO %s VALUES(?, ?)" % TABLE_NAME
    SELECT_QUERY = "SELECT title, note FROM %s" % TABLE_NAME
    DELETE_QUERY = "DELETE FROM %s WHERE note = ?" % TABLE_NAME
    
    # create instance of sqlite helper class &  create a table
    def __init__(self):
        self.sqlite_helper = SqliteHelper(PyNoteSqlite.DB_NAME)
        self.sqlite_helper.do_modification(PyNoteSqlite.TABLE_QUERY, None)
    
    # inserts values supplied into table
    def insert_value(self, args):
        self.sqlite_helper.do_modification(PyNoteSqlite.INSERT_QUERY, args)
    
    # gets values from table
    def get_all_values(self):
        return self.sqlite_helper.do_selection(PyNoteSqlite.SELECT_QUERY)
        
    # delete a value from the table
    def delete_value(self, arg):
        self.sqlite_helper.do_modification(PyNoteSqlite.DELETE_QUERY, [arg])
