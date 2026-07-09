marks =float(input ("Enter percentage % In number to calculate your grade : "))

if marks >100 or marks<0:
    print("invalid input") 
    
elif marks >=90:
    print("A+ Grade")

elif marks >=80:
    print("A Grade")

elif marks >=73:
    print("B+ Grade")

elif marks >=66:
    print("B Grade")

elif marks >=60:
    print("C+ Grade")
elif marks >=55:
    print("C Grade")
elif marks >=50:
    print("C- Grade")
else :
    print("F Grade(Fail)")