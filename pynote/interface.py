# -*- coding: utf-8 -*-
from Tkinter import * 
import tkMessageBox
from sqlite.connections import PyNoteSqlite

def main():
    #global variables to manipulate the interface
    global root, button1, scrollbar, listbox, text
    
    #global variable to deal with sqlite
    global database_handle
    database_handle = PyNoteSqlite()
    
    # interface setup
    root = Tk() 
    root.title("TkInter")
    button_ins = Button(root, text="Insert", command=insert_callback) 
    button_del = Button(root, text="Delete", command=delete_callback) 
    text = Entry(root) 
    listbox = Listbox(root) 
    scrollbar = Scrollbar(root, orient=VERTICAL) 
    listbox = Listbox(root, yscrollcommand=scrollbar.set) 
    scrollbar.configure(command=listbox.yview) 
     
    button_ins.pack()
    button_del.pack()
    text.pack()
    listbox.pack()
    
    # call to populate existing notes from database 
    populateNotes()
    
    root.mainloop() 
    
# Event handler for insert button
def insert_callback():
    listbox.insert(END, text.get())
    database_handle.insert_value(["hit", text.get()])
    text.delete(0, END)
    #tkMessageBox.showinfo("Hit", "Bit")
    
# Event handler for delete button
def delete_callback():
    print listbox.get(listbox.curselection()),
    database_handle.delete_value(listbox.get(listbox.curselection()))
    listbox.delete(listbox.curselection())
    
def populateNotes():
    rows = database_handle.get_all_values()
    for row in rows:
        listbox.insert(END, row[1])

if(__name__ == '__main__'):
    main()
