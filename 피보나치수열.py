import time
import random
def fibo(x):
    if x==0 or x==1:
        return 1
    return fibo(x-1) + fibo(x-2)


def iter_fibo(x):
    if (x<2):
        return x
    else:
        a = 1
        b = 1
        c = 0
        for i in range (x):
            a = c
            c = b
            b += a
        return b

x=random.randrange(1,100)
t1=time.time()
print(fibo(30))
t1=time.time()-t1
print(t1)
t2=time.time()
print(iter_fibo(30))
t2=time.time()-t2
print(t2)
