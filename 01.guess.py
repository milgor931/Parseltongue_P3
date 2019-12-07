import random

arr = ["puppy", "kuber", "apple", "purse", "dance", "fuzzy"]

word = arr[int(random.random() * (len(arr) -1))]
print("First Letter of the Word: ", word[0:1])
guesses = 10
guess = input("GUESS: ")


while guess != word and guesses != 0:
    if guess == "":
        print("You wasted a guess =P")
        print("You have ", guesses, " guesses left!")
        guesses -= 1
    elif guess[0:1] != word[0:1]:
        x = 0
        Str = ""
        for i in range(26):
            Str = Str + str(chr(65 + x)) + " "
            x += 1
        print(Str)
        print("You have ", guesses, " guesses left!")
    elif len(guess) != 5:
        print("0, 1, 2, 3, 4 that’s how we count to five!")
        print("You have ", guesses, " guesses left!")
        guesses -= 1
    if len(guess) == 5 and guess != word:
        print("You have ", guesses, " guesses left!")
        guesses -= 1
    guess = input("GUESS: ")
if guess == word:
    print("Good job! You are one with the Source.")