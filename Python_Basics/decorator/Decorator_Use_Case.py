# import time
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("The total time of execution is : ",(end-start))
#     return wrapper


# @decorator
# def hello():
#     print("Hello ,Im new here...!")
# hello()

import time 
def timer (func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        func_Args = ", ".join(str(arg) for arg in args)
        func_Kwargs = ','.join(f"{k} : {v}"for k , v in kwargs.items() )
        print(f"Calling the Function : {func.__name__}, its args are : {func_Args} and Kwargs : {func_Kwargs}")
        func(*args,**kwargs)
        end = time.time()
        print(f"Function {func.__name__} Executed in {(end-start)} Time : ")
    return wrapper

@timer
def greet (name = 'User',greet='Hello'):
    print(f"{greet} : {name}")
greet( 'farhan' ,'assalam walikum')
