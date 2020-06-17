# -*- coding: utf-8 -*-
__github__ =
from io import open
#Hier drunter befinden sich alle Variablen
filename = "test.txt"

f = open(filename, "r", encoding='utf-8')
x = f.read()
f.close()
res = []
for i in x:
    res.append(i)

print (res) #Auskommentieren wenn kein output via Print gewünscht
