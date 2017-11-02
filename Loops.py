#!/bin/python3

import sys
def multiply_value(a):
    for i in range(1,11):
        print(a , 'x' , i , '=' , a*i)

n = int(input().strip())
multiply_value(n)
