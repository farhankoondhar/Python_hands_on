try :
    num = int (input ("Enter a positive number to see it's factorial : "))
except ValueError:
    print("Enter a valid integer ")
    exit()
fac= 1
if num<0:
    print("Invalid input")
    exit()
elif num ==0:
    print(f"The factorial of {num} is : {fac}")
else:
    for i in range(num,0,-1):
      fac *=i 
print(f"The factorial of {num} is : {fac}")