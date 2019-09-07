from googlesearch import search
import webbrowser
from random import randint
import urllib.request
import urllib.parse
import re

def parse_images(source):
    links = []
    t = str(source).split('<img src="')
    for i in t:
        r = str(i).split('"')
        links.append(r[0])
    return links

def download(links):
    name = 0
    for i in links:
        try:
            v = urllib.request.urlopen(i)
            f = open(str(name)+".png","wb")
            f.write(v.read())
            f.close()
            name += 1
        except:
            pass

def load_source(website):
    s = urllib.request.urlopen(website)
    v = s.read()
    return v

def  pesquisa(tema_da_pesquisa,stop):
     for url in search(tema_da_pesquisa, stop = stop):
          #print (url)
          return url
          #webbrowser.open(url)


def hentai():
    source = pesquisa(input("tema:"),1)
    input("start:")
    links = parse_images(source)
    download(links)
