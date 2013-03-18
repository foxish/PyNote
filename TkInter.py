# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:17:07 2013

@author: DarkCthulhu
"""

from Tkinter import * 

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

def Button1(): 	
    listbox.insert(END, "button1 pressed") 

def Button3(): 	
    text_contents = text.get() 	
    listbox.insert(END, text_contents) 	
    text.delete(0,END) 

if(__name__ == '__main__'):
    main();