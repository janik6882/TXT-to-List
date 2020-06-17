# -*- coding: utf-8 -*-
__github__ =
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
    get_content("test.txt")
print (res) #Auskommentieren wenn kein output via Print gewünscht
