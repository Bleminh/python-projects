import requests

username = input("Please enter a GitHub username: ")
api_url = f"https://api.github.com/users/{username}"

response = requests.get(api_url)

status = response.status_code

if (status == 200):
    user_data = response.json()
    print(user_data["name"])
    print(user_data["bio"])
    print(user_data["public_repos"])
    print(user_data["followers"])
elif (status == 404):
    print("Error: That GitHub user does not exist.")