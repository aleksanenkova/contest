# -*- coding: utf-8 -*-
import string
count = int(input())
err_count = 0
a = []
while (count > 0):

    Zapros, err = input().split()
    Zapros= int(Zapros)
    err = int(err)
    err_ = Zapros*(err/100)
    a.append(err_)
    err_count = err_count+err_
    count -=1
 
i = 0
while i < len(a):
        ver =a[i]/err_count
        ver = round(ver, 12)
        print(ver)
        i += 1


