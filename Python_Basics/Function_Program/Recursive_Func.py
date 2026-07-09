def factorial(num):
    if num < 0:
        print("Invalid number input")
        exit()
    elif num == 0 or num == 1 :
        return 1
    else:
        return num * factorial(num-1)
while True:
    try :
        num = int (input("Enter any whole number to see its factorial : "))
    except ValueError:
        print("Invalid input")
        continue

    print(f"The factorial of {num} =",factorial(num))
    choice = (input("Do you want to continue? Press 0 to exit, any other key to continue: "))
    if choice =='0':
        break
