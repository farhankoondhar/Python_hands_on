def even_odd_number_list(number_list):
    even_number_list = []
    odd_number_list = []

    for num in number_list:
        if num % 2 ==0:
            even_number_list.append(num)
        else:
            odd_number_list.append(num)
    even_number_list.sort()
    odd_number_list.sort()

    print("Sorted Even number list", end=" : [ ")
    for num in even_number_list:
        print(num, end=" ")
    print("]")

    print("Sorted Odd number list", end=" : [")
    for num in odd_number_list:
        print(num, end=" ")
    print("]\n")
    print (f"The total Even numbers is : {len(even_number_list)}")
    print (f"The total Odd numbers is : {len(odd_number_list)}")

    
while True:

    try:
       number_list = list(map(int,input("Enter the list of number separated by the commas (any numbers you want) ").split(",")))
    except ValueError:
       print("Invalid Input — please enter only numbers separated by commas.")
       continue
    even_odd_number_list(number_list)
    while True :
        choice =input("Do you want to continue...(Y/N)").strip().upper()
        if choice == 'Y':
            print("Continuing the program ...")
            break
        elif choice== 'N':
            print("Exiting the program ...")
            exit()
        else:
            print("Invalid Input — please enter only (Y) for continue & (N) for exit ...")

    










