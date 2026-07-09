try :
    fruit = input("Enter the fruit name :").strip().upper()
    color = input("Now fruit's color :").strip().upper()
except ValueError:
    print("Invalid input ")
    exit()

if fruit =="BANANA" :
    if color=="GREEN":
        print("Unriped")
    elif color=="YELLOW":
        print("Riped")
    elif color=="BROWN":
        print("Overriped")

elif fruit =="APPLE":
    if color=="GREEN":
        print("Unriped")
    elif color=="RED":
        print("Riped")
    elif color=="BROWN":
        print("Overriped")
else:
    print("Right now there no imformation about "+fruit)