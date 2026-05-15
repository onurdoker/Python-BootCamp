from datetime import datetime

entry = input("Daily note: ")
date = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("daily_notes.txt", "a", encoding="UTF-8") as file:
    file.write(f"[{date}] {entry}\n")
