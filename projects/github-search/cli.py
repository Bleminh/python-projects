import argparse
from github_api import get_user_info

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user info.")
    parser.add_argument("username", help="The GitHub username to search for")

    args = parser.parse_args()

    print(f"Searching for '{args.username}' ...\n")
    user_data = get_user_info(args.username)

    if user_data is None:
        print(f"Error: User '{args.username}' not found")
        return

    print(f"Name:        {user_data.get('name', 'No name provided')}")
    print(f"Bio:         {user_data.get('bio', 'No bio')}")
    print(f"Followers:   {user_data.get('followers')}")
    print(f"Repos:       {user_data.get('public_repos')}")
    print(f"Profile URL: {user_data.get('html_url')}")

if __name__ == "__main__":
    main()