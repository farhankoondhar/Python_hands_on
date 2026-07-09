def func():
    try:
        num = int(input("Enter any number to see it's Sqr : ") )
    except ValueError:
        print("Invalid input")
        exit()
    sqr_Num = num*num
    return sqr_Num
print("The Sqr of number you entered is = ",func())
