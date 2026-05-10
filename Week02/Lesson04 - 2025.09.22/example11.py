"""
Note-taking Application

Let's create a simple note-taking application that:
- Asks the user to input notes.
- Stores those notes in a list.
- Finally, prints out the list of taken notes
"""

print("Note book")
print("To exit write quit")
notes = []
while True:
    new_note = input("Enter your note: ")
    if new_note.lower() == "quit":
        break
    notes.append(new_note)

print("Your notes:")
for note in notes:
    print("-", note)
