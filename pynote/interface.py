# -*- coding: utf-8 -*-
from Tkinter import * 
#from sqlite.sqlitehelper import Sqlitehelper

root = Tk() 
root.title("TkInter")

button1 = Button(root, text="button1", command=Button1) 
button2 = Button(root, text="button2") 
button3 = Button(root, text="button3", command=Button3)  
text = Entry(root) 
listbox = Listbox(root) 
scrollbar = Scrollbar(root, orient=VERTICAL) 
listbox = Listbox(root, yscrollcommand=scrollbar.set) 
scrollbar.configure(command=listbox.yview) 

def main():
    button1.pack()
    button2.pack()
    button3.pack()
    text.pack()
    listbox.pack()
    
    root.mainloop() 

if(__name__ == '__main__'):
    main();
