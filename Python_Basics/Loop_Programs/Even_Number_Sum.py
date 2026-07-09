try :
    nTH_number = int(input("Enter the nTH number of list : "))
except ValueError :
    print("Invalid input")
    exit()
even_Sum=0

for i in range(2,(nTH_number+1),2):
        even_Sum = even_Sum+i
print(f"The sum of the even numbers upto {nTH_number} is {even_Sum}")