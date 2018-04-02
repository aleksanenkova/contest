# -*- coding: utf-8 -*-
import string

k, m, d = input().split()
k = int(k)
m = int(m)
d = int(d)
total = m
count = 0
i = 1
for e in range(i):

    while ((total-i) >= 0):
        if d !=6 and d != 7:
            total =total+k
            count+=1
            total=total-i
            i += 1
            d = d+1
            if d >7:
                d = 1
        else:
        
            count+=1
            total=total-i
            i += 1
            d = d+1
            if d >7:
                d = 1

    else:

            if (d !=6 and d != 7) and total+k-i>=0:
                total=total+k
                total=total-i
                i+=1
                count+=1
                d = d+1
                if d >7:
                    d = 1

else:
    while (d !=6 and d != 7) and total+k-i>=0:
        total=total+k
        total=total-i
        i+=1
        count+=1
        d = d+1
        if d >7:
            d = 1
print(count)

#
#count_let = 0
##a = []
#len_text = len(text)
#S=text.split(' ')
#S_len = len(S)
#press = len_text-S_len+1
#    for i in range(text):
#
#
#print (text.count(str, 0, 10))
#
##array_d = {}.fromkeys(S, 0)
##for a in S:
##    array_d[a] += 1
##print (len(S[1]))
#
##for i in range(len(S)):
##    if S[i] == S[i-1]:
##        i-=1
##        print(S[i])
##        press = press - (len(S[i])-1)
##    else:
##        i-=1
#
##print()
#print (S_len)
#print (press)

