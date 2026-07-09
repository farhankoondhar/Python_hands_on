def get_Two_Numbers():
    try:
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter 2nd number : "))
        return num1, num2
    except ValueError:
        print("Invalid Input \n Input Only numbers \nretrying... ")
        return get_Two_Numbers()

def Add():
    num1 , num2 = get_Two_Numbers()
    print (f"{num1} + {num2} is = ",(num1+num2))

def multiply ():
    num1 , num2 = get_Two_Numbers()
    print (f"{num1} x {num2} is = ",(num1*num2))

def subtract ():
    num1 , num2 = get_Two_Numbers()
    print (f"{num1} - {num2} is = ",(num1-num2))

def division ():
    num1 , num2 = get_Two_Numbers()
    try:
        print (f"{num1} / {num2} is = ",(num1/num2))
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        
    
def remainder():
    num1 , num2 = get_Two_Numbers()
    try:
       print (f"{num1} % {num2} is = ",(num1%num2))
    except ZeroDivisionError:
        print("Division by zero is not allowed")
print("-" * 40)
print("[ Welcome to Calculator App ]")
print("-" * 40)

while True:

    print("\n[ 1. for Addition of Two numbers  ]") 
    print("[ 2. for Difference ]")
    print("[ 3. for Divion ]")
    print("[ 4. for Multiplication of Two numbers ]")
    print("[ 5. for Remainder ]")
    print("[ 6. Exit the program ]")
    try:
       choice = int(input(" Choose any option from the above list "))
    except ValueError:
        print("Invalid input\n Input any number from above option eg, 1 or 2 etc")
        continue
    match choice:
        case 1 :
            Add()
        case 2 :
            subtract()
        case 3 :
            division()
        case 4 :
            multiply()
        case 5 :
            remainder()
        case 6:
            print("Thank you for using the Calculator App. Goodbye!")
            exit()
        case __:
            print("Invalid Input\nRetrying...")
            
    
