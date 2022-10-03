import random


def wordle():
    print("----- Jogando: Wordle -----")

    words = []
    count = 5
    file = open("words.txt", "r")
    for word in file:
        if len(word) == 6:
            words.append(word)
    selected_word = list(random.choice(words))
    selected_word.pop()

    guess = list(input("Sua palavra: "))

    while count > 0 and guess != selected_word:
        while len(guess) != 5:
            print("A palavra deve ter 5 letras!")
            guess = list(input("Sua palavra: "))

        for letter_guess in range(len(guess)):
            for letter_selected_word in range(len(selected_word)):
                if guess[letter_guess] in selected_word and guess[letter_guess] == selected_word[letter_guess]:
                    print("{}{}{}".format('\033[32m', guess[letter_guess].upper(), '\033[0;0m'), end=" ")
                    break
                elif guess[letter_guess] in selected_word and guess[letter_guess] != selected_word[letter_guess]:
                    print("{}{}{}".format('\033[33m', guess[letter_guess].upper(), '\033[0;0m'), end=" ")
                    break
                elif guess[letter_guess] not in selected_word:
                    print(guess[letter_guess].upper(), end=" ")
                    break
        print(" ")
        guess = list(input("Sua palavra: "))
        count -= 1

    if guess == selected_word:
        for letter_guess in range(len(guess)):
            print("{}{}{}".format('\033[32m', guess[letter_guess].upper(), '\033[0;0m'), end=" ")
        print(" ")
        print("{}Você ganhou!{}".format('\033[32m', '\033[0;0m'))
    else:
        for letter_selected_word in range(len(selected_word)):
            print("{}{}{}".format('\033[31m', selected_word[letter_selected_word].upper(), '\033[0;0m'), end=" ")
        print(" ")
        print("{}Você perdeu!{}".format('\033[31m', '\033[0;0m'))
