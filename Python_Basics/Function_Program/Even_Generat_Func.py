def even_Generator(limit):
    for i in range(2,(limit+1) ,2):
        yield i

    
for num in even_Generator(10):
    print(num)    
