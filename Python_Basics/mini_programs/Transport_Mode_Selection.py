try:
    distance = float(input("Input how much you want to travel (distance in Km):\n"))
except ValueError:
    print("Invalid Input")
    exit()

if distance <= 0:
    print("Input correct distance")
elif distance <= 1.5:
    print(f"You can cover this {distance}Km by feet")
elif distance <= 20:
    print(f"You can use a bike to cover {distance}Km distance")
elif distance < 500:
    print(f"Prefer to use a car or bus to cover {distance}Km distance")
else:
    print("Taking a flight or train would be a better option")
