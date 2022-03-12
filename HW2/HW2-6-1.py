import time 
start = time.time()


def ones(n):
    x=0
    p=0
    i=0
    while True:
        x += 10**i % n 
        p += 10**i
        if x%n == 0 : 
            print(i+1)
            print(time.time()-start)
            break
        else :
            i += 1

ones(9949)