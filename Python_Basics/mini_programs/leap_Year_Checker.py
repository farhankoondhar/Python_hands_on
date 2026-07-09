try:
    year = int(input("Enter any year to check whether its a leap year or not : "))
except ValueError:
    print("Invalid Input")
    exit()
    
if (year % 400 == 0) or(year % 4 ==0 and year % 100 !=0):
    leap_year = "Leap Year"
else:
    leap_year = "Not a Leap Year"
print(leap_year)
