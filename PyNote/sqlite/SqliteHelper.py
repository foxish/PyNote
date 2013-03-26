# -*- coding: utf-8 -*-
import sqlite3

class SqliteHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def do_query(self, query, args):
        self.cursor.execute(query)
        
    def create_table(self, args):
        self.cursor.execute("""CREATE TABLE snips
                           (title text, note text) """)
                           
    def insert_stuff(self, args):
        self.cursor.execute("INSERT INTO snips VALUES ('note', '%s')" % args)

        

    
