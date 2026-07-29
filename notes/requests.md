- Similar to Homebrew manages software for macOS, Python has its own package manager called pip.
- For advanced web requests, "requests" library is usually used.
- Making a GET request: response = requests.get(url)

- Checking the Status Code: response.status_code (This will be an integer like 200 or 404, exactly like what you saw in your curl experiments).

- Extracting the Body: If you know the server is sending JSON data, you can instantly turn that data into a Python dictionary by calling data = response.json().
- Use data.get("bio") for safety.
- 