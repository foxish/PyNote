from SqliteHelper import *

def main():
    sqlite_helper = SqliteHelper("test.db")
    #sqlite_helper.create_table("")
    sqlite_helper.insert_stuff("fox")
    
if __name__ == '__main__':
    main()
