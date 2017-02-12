# -*- coding: utf-8 -*-

def my_power(a,b):
    i = b
    res = 1
    while i > 0:
        res = res * a
        i = i - 1
    return res

print (my_power(6,4))

print ('END')
