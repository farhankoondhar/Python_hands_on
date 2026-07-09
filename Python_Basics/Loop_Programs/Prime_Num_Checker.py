while True:
  try :
    num = int (input("Enter any number to check whether its prime or not : "))
  except ValueError:
    print("Invalid input")
    continue
  if num <=1:
    print(f"{num} is Not prime")
  else:
    istrue = True
    for i in range(2,num):
      if num % i==0:
        print(f"{num} is not a prime")
        istrue = False
        break
    if istrue ==True:
      print ( f"{num} is a Prime ")
  choice = input("Press any key to continue ,or N for exit the program : ").strip().lower()
  if choice =='n':
    break



 
