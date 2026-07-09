try :
   order_Size = str(input("Choose Coffee order size eg: Small ,Medium ,Large : ").strip().upper())
except ValueError:
    print("Invalid input ")
    exit()

if order_Size not in ['SMALL', 'MEDIUM', 'LARGE']:
    print("Invalid input")

else:
    choose = input ("Do you want an extra shot of espresso(Y/N)").strip().upper()
    if choose == 'Y':
        print(f"You have ordered {order_Size } size with extra shot of espresso")
    elif choose == 'N':
        print(f"You have ordered {order_Size } size ")
    else :
        print("Invalid input")