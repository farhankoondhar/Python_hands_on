wed = input("Is today wednesday : Y for yes ,any key except y NO ").lower()
try:
   age = int(input ("Enter your age : "))
except ValueError:
   print("Invalid input")

if age <=0:
    print("Invalid input")

else:
    price =12 if age>=18 else 8

    if wed == 'y':
     price -=2
     
    print(price)  


