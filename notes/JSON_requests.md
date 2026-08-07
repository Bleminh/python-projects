# JSON
1. JSON is a way of storing and sending structured data.
* Example:
```
{
    "name": "Alice",
    "age": 20,
    "major": "ETE"
}
```
* Also has data types such as: object, array, string, number, boolean, null,...
2. Nested JSON:
```
{
    "name": "Alice",
    "location": {
        "country": "Vietnam",
        "city": "Hanoi"
    }
}
```
* Python sees this as:
```
person = {
    "name": "Alice",
    "location": {
        "country": "Vietnam",
        "city": "Hanoi"
    }
}
```
* To access it:
```
person["location"]["country"]
```
3. .json() converts the JSON into normal Python objects
4. Reading JSON from a file
```
{
    "theme": "dark",
    "font": 16
}
```
* Python:
```
import json

with open("settings.json") as file:
    settings = json.load(file)

print(settings["theme"])
```
5. Saving JSON:
* Python:
```
import json

todo = {
    "tasks": [
        "Study",
        "Sleep"
    ]
}

with open("todo.json", "w") as file:
    json.dump(todo, file, indent=4)
```
# Requests Library
```
import requests

response = requests.get("https://api.github.com/users/octocat")
```

Your Python Program
        │
        │ requests.get(...)
        ▼
Internet
        │
        ▼
GitHub Server
        │
        │ looks up the user
        ▼
Returns JSON
        │
        ▼
requests receives it
        │
        ▼
response object
1. Import the library:
```
import requests
```
2. Send a GET request:
```
response = requests.get(url)
```
3. Check status:
```
response.status_code
```
* 200 -> Success
* 404 -> Not found
* 500 -> Server error
4. Convert JSON:
```
data = response.json()
```
5. Access the data:
```
data["followers"]
```
6. Handle errors:
```
if response.status_code == 200:
    ...
else:
    ...
```
