while True:
    try :
        num = int(input("Enter any number except the numbers B/W the 1 and 10 : "))
    except ValueError:
        print("Invalid input ")
        continue
    if    1<num<10:
           
        print("Number is between 1 and 10. Exiting...")
        break
    else:
        print(f"You entered {num}, which is acceptable.")
    
    while True:
        choice = input ("Do you want to continue (Y/N) ...").strip().upper()
    
        if choice == 'Y':
           print("Continueing the program :")
        elif choice =='N':
           print("Exiting the program :")
           exit()
        else:
           print("Invalid Input ,Please enter 'Y' for yes or 'N' for no. ")