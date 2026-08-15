import requests

username = input("Please enter a GitHub username: ")
api_url = f"https://api.github.com/users/{username}"

response = requests.get(api_url) #HTTP GET Request

status = response.status_code

if (status == 200):
    user_data = response.json() #If status OK, the server (api.github.com) will return data in JSON format. 
    print(user_data["name"])
    print(user_data["bio"])
    print(user_data["public_repos"])
    print(user_data["followers"])
elif (status == 404):
    print("Error: That GitHub user does not exist.")

# Asks user for an username, use requests.get() to get the data.
# Use .status_code to get status code
# 404 status (username not found)
# For 200 status, take the response from the server (in JSON format),
# use .json() to "translate" into Python data
# access data using user_data["..."]
# Concepts used: requests library, requests.get(), .status_code, JSON