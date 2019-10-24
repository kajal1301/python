
#function caching in python

import time
from functools import lru_cache
@lru_cache(maxsize=3)       #this saves the latest 3 calls
def some_work(n):
#some tasks taking n seconds
    time.sleep(n)
    return n

if __name__== '__main__':
    print("now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("done")
    some_work(3)
    print("called again")
    