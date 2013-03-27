from sqlitehelper import SqliteHelper

def main():
    TABLE_QUERY = "CREATE TABLE snips (title text, note text)"
    INSERT_QUERY = "INSERT INTO snips VALUES(?, ?)"
    
    sqlite_helper = SqliteHelper("test.db")
    sqlite_helper.do_query(TABLE_QUERY, None)
    sqlite_helper.do_query(INSERT_QUERY, ["val1", "val2"])
    
if __name__ == '__main__':
    main()
