# -*- coding: utf-8 -*-

def my_power(n):
    if n == 1:
        return 1
    else:
        return n * my_power(n-1)

print (my_power(4))

print ('END')
