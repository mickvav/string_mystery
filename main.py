#!/usr/bin/env python3

import timeit
import time

def generateString(n: int) -> str:
    res = ""
    b = ""
    for i in range(n):
        b += "12"
    for c in res:
        if c == "1":
            res += c
    return res

for i in range(1,7):
    iterations = 10**i
    n=time.time()
    generateString(iterations)
    print(iterations, time.time() - n)
    #print(iterations, timeit.timeit("generateString("+str(iterations)+")",number=1, globals=globals()))
