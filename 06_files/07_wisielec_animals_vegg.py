# Wisielec.
# Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc.

import random


def get_category():
    message = """ 
    Witaj w grze wisielec

    wybierz kategorię:

    1 - "zwierzęta"
    2 - "warzywa"
    """

    user_choice = input(message)
    return user_choice


def get_words_list(category):
    file_to_open = {
        "1": "animals.txt",
        "2": "veggies.txt"
    }

    filename = file_to_open[category]
    with open(filename) as fopen:
        content = fopen.read()

    return content.split(", ")


def get_letter():
    while True:
        letter = input("Podaj literę -> ")

        if len(letter) > 1:
            print("To nie jest pojedyncza litera!")
        elif not letter.isalpha():
            print("Ten znak nie jest literą!")
        else:
            print(f"Podano literę {letter}")
            break

    return letter


def show_word_state(letters):
    print("".join(letters))


def main():
    category = get_category()
    words = get_words_list(category)
    word_to_guess = list(random.choice(words))

    print(word_to_guess)

    user_word = ['-'] * len(word_to_guess)
    show_word_state(user_word)

    tries = 5

    while tries > 0:
        letter = get_letter()

        if letter in word_to_guess:
            print(f'Litera {letter} występuje!')

            for index, value in enumerate(word_to_guess):
                if letter == value:
                    user_word[index] = letter
            show_word_state(user_word)
        else:
            print(f'Litter {letter} nie występuje w słowie')
            tries -= 1


main()