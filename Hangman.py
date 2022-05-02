introduction = input("Welcome! Please enter the phrase to guess: ")
word = ["_"] * len(introduction)
input_word = ""
missed = ""

correct_guesses = 0
word_length = 0
max_guesses = 6
guessed_characters = []

while max_guesses != 0:
    print("Your phrase to guess " + str(word))
    print("Chances Remaining   : " + str(max_guesses))
    print("Missed Letters/Digits: ", missed)
    input_word = input("Your guess (letters only) ")

    while word_length < len(introduction):
        if introduction[word_length] == input_word:
            word[word_length] = input_word
            correct_guesses += 1
        word_length += 1

    if input_word not in introduction:
        print("This character is not present in the name.")
        max_guesses -= 1
        missed += input_word
    word_length = 0

    if correct_guesses == len(introduction):
        print("Winner")
        break

    if max_guesses == 0:
        print("You are out of guesses. Game over!")

