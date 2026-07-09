def Decorator(func):
    def wrapper (*args,**kwargs):
        print(f"[log] running Fuction : ",func.__name__)
        return func(*args,**kwargs)
    return wrapper



@Decorator
def greet(name,greet= "Hello!"):
    print(f"{greet} to {name}")

greet("Farhan Ali", "Assalam-u-Allaikum")