import requests
import json

def fetch_random_user(url):
    response = requests.get(url)
    data= response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]

        return user_name, user_country
    
    else:
        raise Exception("Failed to fetch user data")


def main():
    url = "https://randomuser.me/api/"
    try :
        name,country = fetch_random_user(url)
        print(f"The username is {name} and their country is {country}")
    except Exception as e:
        print(str(e))
    

if __name__== "__main__":
    main()
