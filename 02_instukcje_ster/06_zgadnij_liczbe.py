my_number = 42

guess = int(input("Zgadnij liczbę od 1 do 100: "))

if guess == my_number:
    print("Gratulacje! Zgadłeś liczbę!")
else:
    print("Pudło! Nie zgadłeś liczby. Ukryta liczba to:", my_number)