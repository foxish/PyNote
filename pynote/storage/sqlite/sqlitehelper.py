# -*- coding: utf-8 -*-
import sqlite3

class SqliteHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    # handles selection
    def do_selection(self, query):
         self.cursor.execute(query)
         rows = self.cursor.fetchall()
         return rows
    
    # handles modification
    def do_modification(self, query, args):
        self.cursor.execute(query, args) if not args is None else self.cursor.execute(query)
        self.conn.commit()

    
