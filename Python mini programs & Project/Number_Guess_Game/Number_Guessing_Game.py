import random

print ("[ Welcome to Number Guessing Game App! ]\n")

while True:
    print("I'm thinking a number between 1 and 100")
    level = input ("Enter the level of hardness (easy,medium,hard)").strip().upper()
    if level =='EASY':
        attempts = 10
    elif level =='MEDIUM':
        attempts = 7
    elif level =='HARD':
        attempts = 5
    else :
        print("Invalid input \n retry...")
        continue
    secret_number = random.randint(1,100) 

    for attempt in range(attempts):
        print(f"You have {attempts-attempt} attempts left")

        try:
            guessed_number =  int(input("Guess the secret number! ..."))
        except ValueError:
            print("Invalid Input! Retrying ... ")
            continue
        if guessed_number < secret_number:
            print("Too low!, Try again")
        elif guessed_number > secret_number:
            print("Too high!, Try again.")
        else:
            print("You guess the right number , hurrayyyyy! You Win.")
        if (attempt+1)==attempts:
            print(f"No attempts left You loose the game! ...")
        
        if (attempt+1)==attempts or secret_number == guessed_number:
            while True:
                choice = input("Do you want to play one more round (Y) or Quit the game (N) ").strip().upper()
                if choice not in ('N','Y'):
                    print("Invalid Input \n Press only (N/Y)\n Retrying ...")
                    continue
                elif choice == 'N':
                    print("Quiting the Game...")
                    exit()
                elif choice == 'Y':
                    print("Starting One more round!.")
                    break
            break
                    
            
        
        