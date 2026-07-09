pet_Name = input("Your pet name eg: Dog ,Cat ,etc : ").strip().lower()

try:
    pet_age = int(input("also input it's age "))
except ValueError:
    print("Invalid Input ")
    exit()

if pet_Name == "dog":
    if pet_age <0:
        pet_food ="Invalid age input"
    elif pet_age <=2:
        pet_food ="Puppy Food"
    else:
        pet_food ="Senior dog food"
elif pet_Name == "cat":
    if pet_age <0:
        pet_food ="Invalid age input"
    elif pet_age <=1:
        pet_food ="kitten Food"
    else:
        pet_food ="Senior cat food"
else:
    pet_food = (f"Not any information is provided about this {pet_Name} ")
    print(pet_food)
    exit()
print(f"AI recommends you {pet_food} for your {pet_Name}")