from tkinter import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
####
url = "https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona"

def content_format(content):
    x = len(content) // 100
    formatted = ""
    y = 0
    if len(content) % 100 == 0:
        while y < x:
            formatted = formatted + "\n" + content[y*100:(y+1)*100]
            y += 1
    else:
        while y < x:
            formatted = formatted + "\n" + content[y*100:(y+1)*100]
            y += 1
        formatted = formatted + "\n" + content[y*100:]
    return formatted


def get_raw():
    client = urlopen(url)
    page_html = client.read()
    client.close()
    return BeautifulSoup(page_html, "html.parser")

def get_content_dict(raw_soup):
    title = raw_soup.find("h1", {"class" : "firstHeading"}).text
    #test = raw_soup.find("div", {"class" : "mw-content-ltr"}).text.strip()
    content_raw = raw_soup.findAll("p")
    content = ""
    for i in content_raw:
        content = content + "\n" + i.text.strip()

    return title,content_format(content)

def get_content():
    title, content = get_content_dict(get_raw())

    print(title)
    print(content)

initial_title, initial_content = get_content_dict(get_raw())

root = Tk()

def get_random(event):
    title_label["text"], content_label["text"] = get_content_dict(get_raw())

title_frame = Frame(root)
title_frame.pack(side="top")

content_frame = Frame(root)
content_frame.pack()

random_frame = Frame(root)
random_frame.pack(side="bottom")

title_label = Label(title_frame, text=initial_title)
title_label.pack()

content_label = Label(content_frame, text=initial_content)
content_label.pack()

random_button = Button(random_frame, text="Random", bg="green")
random_button.bind("<Button-1>", get_random)
random_button.pack(fill="x")

root.mainloop()
###