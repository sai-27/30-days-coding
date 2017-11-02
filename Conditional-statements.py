#!/bin/python3

import sys
def check(N):
    a = N % 2
    if a == 0:
        if N in range(2,5):
            print("Not Weird")
        elif N in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

P = int(input().strip())
check(P)
