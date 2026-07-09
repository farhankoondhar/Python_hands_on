while True:

   try:
      number = int(input("Input a postive integer to see its factorial : "))
   except ValueError:
      print("Invalid input")
      continue
   if number<0:
      print("Input positive integer ")
   elif number == 0:
      print(f"factorial of {number} is 1")
   else:
      num = number
      fac = 1
      while number > 1:
         fac = fac*number   
         number-=1
      print(f"The factorial of {num} is {fac}")
      choice = input("Press any to continue but 'N' to exit the program").upper().strip()
      if choice == 'N':
         print("exiting the program")
         break
       