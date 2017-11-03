#!/bin/python3
input()

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
    print(num + " ", end="")
#import sys
#def reverse_order(n):
#    for i in range(0,n):
#        arr = str(input())
#        print(arr[::-1] , end = "")

#x = int(input().strip())
#reverse_order(x)
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
