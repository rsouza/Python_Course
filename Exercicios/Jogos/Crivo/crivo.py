import math
import time, timeit

t0= time.time()
def crivo(n=1000000):
    primos = set(range(2,n+1))
    for i in range(2, math.ceil(n**(1/2))):
        if i in primos:
            primos -= set(range(i,n+1, i)[1:])
    return primos

print(timeit.timeit(lambda: crivo(50), number=10000))
# print("levou {} segundos".format(time.time()-t0))