import time

def chache_Decorator(func):
    chache = {}
    def wrapper(*args ):
        if args in chache:
            return chache[args]
        result = func(*args )
        chache[args] = result
        return result
    return wrapper

@chache_Decorator
def sum(a, b):
    time.sleep(3)
    return a+b

print(sum(2,3))
print(sum(2,3))
print(sum(4,5))