# -*- coding: utf-8 -*-
__github__ = "https://github.com/janik6882/TXT-to-List"
__author__ = "Janik Klauenberg"
__version__ = 1.2
from io import open
#Hier drunter befinden sich alle Variablen

def get_content(filename):
    f = open(filename, "r", encoding='utf-8')
    x = f.read()
    f.close()
    res = []
    for i in x:
        res.append(i)
    return res

if __name__ == '__main__':
    x = get_content("test.txt")
    for i in x:
        print i
    print ([i for i in x]) #Auskommentieren wenn kein output via Print gewünscht
