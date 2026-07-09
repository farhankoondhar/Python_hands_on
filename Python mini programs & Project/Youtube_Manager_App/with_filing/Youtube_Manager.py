import json

def load_data():
    try:
        with open("Youtube_Manager.txt" ,"r") as file:
            return json.load(file)
    except FileNotFoundError: 
        return []
    
def save_data_helper(videos):
    with open("Youtube_Manager.txt" ,"w") as file:
        json.dump(videos,file)

def List_all_videos(videos):

    for i,v in enumerate(videos,start=1):
        print(f"{i}. {v['name']} : {v['time']}")
def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video duration : ")
    videos.append({'name': name, 'time' : time})
    save_data_helper(videos)

def delete_video(videos):
    List_all_videos(videos)
    try:
        index = int (input("Enter the number of which Youtube video you want to delete : "))
    except ValueError:
        print("Invalid input \nTry again!...")
        return
    if 1 <= index >= len(videos):
        deleted =videos.pop(index-1)
        print(f"\nthe deleted video : {deleted['name']} : {deleted['time']}\n")
        print("After deletion our youtube videos \n")
        List_all_videos(videos)
        save_data_helper(videos)
    else:
        print("Invalid index selected \nTry again!...")
        return

def update_details(videos):
    List_all_videos(videos)
    try:
        index = int (input("Enter the index number of a video you want to update details : "))
    except ValueError:
        print("Invalid input \nTry again!...")
        return
    if 1 <= index >= len(videos):
        print(f"\nthe video number : {index} is selected for updating detail\n")
        update_name= input("Enter the updated name of a video : ")
        update_time= input("Enter the updated Time of a video : ")
        videos[index-1]['name']= update_name
        videos[index-1]['time']= update_time
        print("\n After the upgradation the youtube videos are :\n")
        List_all_videos(videos)
        save_data_helper(videos)
    else:
        print("Invalid index selected \nTry again!...")
        return

def total_videos(videos):
    print("The total number of youtube is : ",len(videos))



def main():
    videos =load_data()
    print("Welcome to Youtube video Manager App")
    while True:
       
        print("\n1. List Youtube videos ")
        print("2. add a Youtube videos ")
        print("3. Delete a Youtube video ")
        print("4. Update details of a Youtube video")
        print("5. List the total number of Youtube videos")
        print("6. Quit Youtube video Manager App\n")
        try:
            choice = int(input("choose an option : "))
        except ValueError:
            print("Invalid input \nTry again!...")
            continue
        print("\n")
        match choice:
            case 1 :
                List_all_videos(videos)
            case 2 :
                add_video(videos)
            case 3 :
               delete_video(videos)
            case 4 :
                update_details(videos)
            case 5:
                total_videos(videos)
            case 6 :
                print("ThankYou for using our App\nExiting!... ")
                exit()
            case __:
                print("Invalid option selected \nTry again!...")
                continue




if __name__ == "__main__":
    main()
