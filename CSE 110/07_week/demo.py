print("Welcome to the Great-Value Wordle Game! 💀\n")

secret_word = "apple"
guess       = " "
hint = " "
count_guess = 0

while secret_word != guess:
    print(f"HINT: {hint}")
    guess = input("Guess a word: ").lower()
    count_guess += 1
    for i, secret_letter in enumerate(secret_word):
        pass

secret_word = "tunnel"
guess       = "abcdef"
for i in range(len(secret_word)):
    guess_letter  = guess[i]
    secret_letter = secret_word[i]
    print(f"{secret_letter} <> {guess_letter}")