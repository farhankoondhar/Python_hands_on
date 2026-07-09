import sqlite3

conn = sqlite3.connect("YouTube_videos.db")

cur = conn.cursor()

cur.execute(''' 
            CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            ) 

''')
def list_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    if not rows:
        print("The list of youtube video is empty!...")
    else:
        for row in rows:
            print(row)

def add_video(name , time):
    cur.execute("INSERT INTO videos(name,time) VALUES (?,?)",(name,time,))
    conn.commit()

def  delete_video(ID):
    cur.execute("DELETE FROM videos WHERE id =?",(ID,))
    conn.commit()

def update_details(name,time , ID):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?",(name,time , ID))
    conn.commit()

def total_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    print("The number of total YouTube videos",len(rows))

def main():
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
                list_videos()
            case 2 :
                name = input("Enter video name : ").strip()
                time  = input("Enter video time : ").strip()
                if not name or not time:
                    print("Name or time can't be empty!..")
                    continue
                add_video(name,time)
            case 3 :
               print("The list of video : \n")
               list_videos()
               try:
                   ID = int(input("\nEnter the Id  of a video you want to delete "))
               except ValueError:
                   print("Invalid input \nTry again!...")
               delete_video(ID)
            case 4 :
                print("The list of video : \n")
                list_videos()
                try:
                    ID = int(input("\nEnter the Id of a video you want to update : "))
                except ValueError:
                    print("Invalid input \nTry again!...")
                name = input("Enter video name : ").strip()
                time  = input("Enter video time : ").strip()
                if not name or not time:
                    print("Name or time can't be empty!..")
                    continue
                update_details(name,time ,ID)
            case 5:
                total_videos()

            case 6 :
                print("ThankYou for using our App\nExiting!... ")
                conn.close()
                break
            case __:
                print("Invalid option selected \nTry again!...")
                continue



if __name__ == '__main__':
    main()