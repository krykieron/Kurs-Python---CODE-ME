#  Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random


def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Remis"
    elif (
            (player_choice == 'k' and computer_choice == 'n') or
            (player_choice == 'p' and computer_choice == 'k') or
            (player_choice == 'n' and computer_choice == 'p')
    ):
        return "Wygrałeś!"
    else:
        return "Komputer wygrał!"


choices = ['k', 'p', 'n']
rounds = int(input("Podaj liczbę rund: "))
player_wins = 0
computer_wins = 0

for i in range(rounds):
    player_choice = input("Wybierz: kamień (k), papier (p) lub nożyce (n): ").lower()

    if player_choice == 'koniec':
        print("Gra zakończona.")
        break

    if player_choice not in choices:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        continue

    computer_choice = random.choice(choices)
    result = play_game(player_choice, computer_choice)

    print("Komputer wybrał:", computer_choice)
    print(result)

    if result == "Wygrałeś!":
        player_wins += 1
    elif result == "Komputer wygrał!":
        computer_wins += 1

print("Wynik:")
print("Gracz:", player_wins)
print("Komputer:", computer_wins)
