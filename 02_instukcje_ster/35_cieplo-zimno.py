import random

target_number = random.randint(1, 100)
max_attempts = 6

print("Zgadnij liczbę od 1 do 100 w 6 próbach.")

for attempt in range(1, max_attempts + 1):
    guess = int(input("Podaj swoją liczbę: "))

    if guess == target_number:
        print("Brawo! Zgadłeś!")
        break
    elif abs(target_number - guess) <= 5:
        print("Ciepło")
    else:
        print("Zimno")

if guess != target_number:
    print("Przegrałeś! Wylosowana liczba to:", target_number)