from tkinter.constants import RAISED
import xml.etree.ElementTree as ET
#import xmltodict?
from tkinter import *  #Tkinter built in python GUI module     https://docs.python.org/3/library/tk.html

file = "data/catalog.xml"

FONT_SIZE = 13

tree = ET.parse(file)
root = tree.getroot()
found = {}
found = root
def search():
    search = search_box.get("1.0", "end-1c")
    # print(root[0][0])           #Element author at blah blahblah
    # print(root.tag)             #catalog
    # print(root[0].tag)          #book
    # print(root[0].attrib['id']) #bk101 (the id of the book)

    for elem in root:
        split = elem[0].text.split(", ")
        for each in split:
            if search.lower() == each.lower():
                title.configure(text = f"1. {elem[1].text} / by {split[1]} {split[0]}" )
                author.configure(text= elem[0].text)
                genre.configure(text= elem[2].text)
                pub.configure(text= elem[4].text)
                desc.configure(text= elem[5].text)
                format.configure(text= root[0].tag)
                id.configure(text= elem.attrib['id'])
                price.configure(text= elem[3].text)
            # for subelem in elem:
            #     pass
            #     #print(subelem[0]) #or subelem.attrib
            #         # https://stackabuse.com/reading-and-writing-xml-files-in-python/

window = Tk()
window.geometry("1500x850")
window.title("Library")

win_frame = Frame(window, width = 1000, height = 500)
win_frame.grid(row = 0, column = 0, columnspan = 4, rowspan = 6, padx = 30, pady = 20, ipadx= 125)
win_frame.columnconfigure(index = 0, minsize = 50)
win_frame.columnconfigure(index = 1, minsize = 250)
win_frame.columnconfigure(index = 2, minsize = 50)
win_frame.columnconfigure(index = 3, minsize = 250)

search_box = Text(win_frame, font= ("Arial", FONT_SIZE), width= 50, height= 1)
search_box.grid(row= 0, column= 0, columnspan= 4)

Button(win_frame, text= "Search", font= ("Arial", FONT_SIZE), width = 6, height = 1, command = search).grid(row= 0, column= 4)

Label(win_frame, width = 15, text = "Author", justify = "left", font = ("Arial", FONT_SIZE)).grid(row=2, column=0)
Label(win_frame, width = 15, text = "Genre", justify = "left", font = ("Arial", FONT_SIZE)).grid(row=3, column=0)
Label(win_frame, width = 15, text = "Published", justify = "left", font = ("Arial", FONT_SIZE)).grid(row=4, column=0)
Label(win_frame, width = 15, text = "Description", justify = "left", font = ("Arial", FONT_SIZE)).grid(row=5, column=0)

title = Label(win_frame, width= 30, justify = "left", font = ("Arial", 24))
title.grid(row=1, column=1, columnspan= 4)

author = Label(win_frame, width= 10, justify = "left", font = ("Arial", FONT_SIZE))
author.grid(row=2, column=1)

genre = Label(win_frame, width= 10, text = "", justify = "left", font = ("Arial", FONT_SIZE))
genre.grid(row=3, column=1)

pub = Label(win_frame, width= 10, text = "", justify = "left", font = ("Arial", FONT_SIZE))
pub.grid(row=4, column=1)

desc = Label(win_frame, width= 75, text = "", justify = "left", font = ("Arial", FONT_SIZE))
desc.grid(row=5, column=1, columnspan= 3, pady= 5, sticky= W)

Label(win_frame, text = "Format", justify = "right", font = ("Arial", FONT_SIZE)).grid(row=2, column=3, padx=5, pady=30)
Label(win_frame, text = "ID", justify = "right", font = ("Arial", FONT_SIZE)).grid(row=3, column=3, padx=5, pady=30)
Label(win_frame, text = "Price", justify = "right", font = ("Arial", FONT_SIZE)).grid(row=4, column=3, padx=5, pady=30)

format = Label(win_frame, width= 10, text = "", justify = "left", font = ("Arial", FONT_SIZE))
format.grid(row=2, column=4)

id = Label(win_frame, width= 10, text = "", justify = "left", font = ("Arial", FONT_SIZE))
id.grid(row=3, column=4)

price = Label(win_frame, width= 10, text = "", justify = "left", font = ("Arial", FONT_SIZE))
price.grid(row=4, column=4)


window.mainloop()