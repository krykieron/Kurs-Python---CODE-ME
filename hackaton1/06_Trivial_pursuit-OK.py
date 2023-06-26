import random

pytania = {
    "Najbliższa ziemi gwiazda?": "słońce",
    "Waluta obowiązująca w Czechach?": "korona",
    "Pierwiastek z liczby 9 wynosi?": "3",
    "Stolica Niemiec?": "Berlin",
    "Najdłuższa rzeka Polski": "Wisła",
    "Stolica Wielkopolski": "Poznań",
    "Przepływa przez Wrocław": "Odra"
}

def losuj_pytanie():
    pytanie = random.choice(list(pytania.keys()))
    odpowiedz = pytania[pytanie]
    return pytanie, odpowiedz

def gra():
    punkty = 0
    liczba_pytan = 3

    for _ in range(liczba_pytan):
        pytanie, odpowiedz = losuj_pytanie()
        print(pytanie)
        odpowiedz_uzytkownika = input("Odpowiedź: ")

        if odpowiedz_uzytkownika.lower() == odpowiedz.lower():
            print("Poprawna odpowiedź!")
            punkty += 1
        else:
            print(f"Błędna odpowiedź. Poprawna odpowiedź to: {odpowiedz}")

        print()

    print(f"Gra zakończona. Zdobyłeś {punkty} punktów z {liczba_pytan} możliwych.")

# Uruchomienie gry
gra()
