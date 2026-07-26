from datetime import datetime

def journal():
    journaling = input("What did you learn today?\n")
    current_time = datetime.now()
    with open("journal.txt", "a") as file:
        file.write(f"{current_time}\n")
        file.write(f"{journaling}\n")

journal()
