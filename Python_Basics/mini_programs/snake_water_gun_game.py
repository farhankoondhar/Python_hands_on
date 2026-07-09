import random 
def game_logic():
    print('''
||  WELCOM TO SNAKE ,WATER ,GUN GAME ||

        :: Game Rules ::
1. Snake drinks Water -> Snake wins

2. Gun shoots Snake -> Gun wins

3. Water damages Gun (rusts it) -> Water wins

4. If both players choose the same option -> Draw ''')
    
    choice_list = ['Water', 'Snake', 'Gun']
    result = ''
    counter =0
    user_choise = input(f"\nEnter your choice {choice_list} : ").strip().lower()
    if user_choise not in ['water', 'snake', 'gun']:
        print("Invalid input \nTry in another round now!")
        return 0
    computer_choice = random.choice(choice_list).lower()
    if user_choice == computer_choice:
        result = "Draw"

    elif (user_choise == 'snake' and computer_choice == 'water') or \
            (user_choice == 'gun' and computer_choice == 'snake') or \
            (user_choice == 'water' and computer_choice == 'gun'):
                result ='Win'
                counter+= 1

    else:
        result="Lose"
        counter+= -1
        
    print(f"you choose {user_choice}\nThe AI choose {computer_choice} \nSo you {result} the game!")
    return counter

def main ():
    score = 0
    while True :
        counter = game_logic()
        score += counter
        print("Your score : ",score)
        while True:
            try:
                choice = int(input("Do you want to play one more round (1. ->(Yes) || 2. ->(no) ) :"))
            except ValueError:
                print("invalid input \nTry again")
                continue
            if choice == 1:
                print("Starting one more round")
                break
            elif choice == 2:
                print("Exiting from the game!...")
                exit()
            else:
                print("invalid input \nTry again")

 
if __name__ == "__main__":
    main()