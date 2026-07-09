try:
   age = int(input("what's your age "))
except ValueError:
   print("Invalid input entered")
if age<0:
    print ("input the correct age")
elif age<13:
    print ("you are a child")
elif age<=18:
    print ("you are teenager")
elif age <35:
    print("you are adult ")
else :
    print("you are a senior in age")
