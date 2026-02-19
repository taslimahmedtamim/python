import random

print(f"{random.random():.1f}") # generate random float between 0.0 and 1.0

number = random.randint(1, 100) # generate random integer between 1 and 100
print("Random number:", number)

options = ("rock", "paper", "scissors")
choice = random.choice(options) # randomly select an element from the list
print("Random choice:", choice)

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards) # shuffle the list in place
print("Shuffled cards:", cards)