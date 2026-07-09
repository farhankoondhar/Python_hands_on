

password = input("Enter your password to check its strength : ")
char_count = len(password)
strength_Metrix = 0
if char_count>=8:
    strength_Metrix +=1

if any(p.isupper() for p in password):
    strength_Metrix +=1

if any(p.islower() for p in password):
    strength_Metrix +=1

if strength_Metrix in [0,1]:
    print("Weak password")
elif strength_Metrix == 2:
    print("Medium strength password ")
else:
    print("Strong password ")

