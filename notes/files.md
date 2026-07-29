- Python's built-in datetime module: from datetime import datetime
- To get the exact date and time at the moment, use now() method: datetime.now()
- f = open("filename", "mode", encoding=None)
- mode: "r" = read, "w" = write (replace the old file), "a" = appending (any data will be added to the end), "r+" = read + write. Mode is optional, default is "r". 
- with Keyword:
with open("filename", "mode") as file:
    # Everything indented here happens while the file is open
    # The file automatically closes when you stop indenting!
file.write("This is my journal entry.\n")