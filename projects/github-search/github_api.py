import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 404:
        return None

    return response.json()