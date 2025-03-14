from random import choice

answers = [
    "Undoubtedly",
    "Foregone conclusion",
    "No doubts",
    "Definitely yes",
    "You can be sure of it",
    "It seems to me – yes",
    "Most likely",
    "Good prospects",
    "The signs say – yes",
    "Yes",
    "Unclear for now, try again",
    "Ask later",
    "Better not to tell",
    "Cannot predict now",
    "Focus and ask again",
    "Don't even think about it",
    "My answer is no",
    "According to my data – no",
    "Prospects are not very good",
    "Very doubtful",
]

print(
    "Hello, World! I am a magic ball, and I know the answer to any of your questions."
)
name = input("What's your name? ")
print(f"Hello, {name}.")

game = "yes"
while game == "yes":
    print("What do you want to ask?")
    input()
    print(choice(answers))
    print()
    game = input('If you want to ask a question, just say "yes": ')

print()
print("Come back if you have any questions!")
print()
