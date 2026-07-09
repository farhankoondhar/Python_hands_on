try:
    num = int(input("Enter any number to see its multiplication upto 10 ,except 5th one : "))
except ValueError:
    print("Invalid input")
    exit()
upto = 11

for i in range(1,upto):
    if i ==5:
        continue
    print(f"{num} x {i} = {(num*i)}")