import random

def play():
    print("r > s, p > r, s > p")
    user = input("""\
What's your choice:
"r" for rock, "p" for paper and "s" for scissors
-> """)

    computer = random.choice(["r","p","s"])
    print("Computer chose "+computer)
    if user == computer:
        return "It's a tie"

    if conditions(user,computer):
        return "You've won!"

    return "You've lost"
    
def conditions(user,computer):
     # r > s, p > r, s > p
    if (user == "r" and computer == "s") or (user == "p" and computer == "r") \
    or (user == "s" and computer == "p"):
        return True
    
print(play())