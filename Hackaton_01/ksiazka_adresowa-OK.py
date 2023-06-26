wpisy = [
    {"imie": "Jan", "nazwisko": "Kowalski", "telefon": "123-456-789", "email": "jan.kowalski@example.com"},
    {"imie": "Anna", "nazwisko": "Nowak", "telefon": "987-654-321", "email": "anna.nowak@gmail.com"},
    {"imie": "Jan", "nazwisko": "Kaczmarek", "telefon": "665-123-456", "email": "anna.nowak@gmail.com"},
    {"imie": "Frodo", "nazwisko": "Baggins", "telefon": "222-343-545", "email": "frodo.baggins@op.pl"}
]

def wyswietl_wpisy():
    if len(wpisy) == 0:
        print("Książka adresowa jest pusta.")
    else:
        for indeks, wpis in enumerate(wpisy):
            print(f"\nWpis {indeks + 1}:")
            print(f"Imię: {wpis['imie']}")
            print(f"Nazwisko: {wpis['nazwisko']}")
            print(f"Telefon: {wpis['telefon']}")
            print(f"Email: {wpis['email']}")


def dodaj_wpis():
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    telefon = input("Podaj numer telefonu: ")
    email = input("Podaj adres email: ")
    nowy_wpis = {"imie": imie, "nazwisko": nazwisko, "telefon": telefon, "email": email}
    wpisy.append(nowy_wpis)
    print("Nowy wpis został dodany.")


def usun_wpis():
    if len(wpisy) > 0:
        indeks = int(input("Podaj numer wpisu do usunięcia: ")) - 1
        if 0 <= indeks < len(wpisy):
            del wpisy[indeks]
            print("Wpis został usunięty.")
        else:
            print("Nieprawidłowy numer wpisu.")
    else:
        print("Książka adresowa jest pusta.")


def menu():
    print(">> Książka Adresowa <<")
    print("Wpisz nr opcji:")
    print("1. Wyświetl wszystkie wpisy")
    print("2. Dodaj nowy wpis")
    print("3. Usuń wpis")
    print("4. Zakończ")

    while True:
        opcja = input("->")

        if opcja == "1":
            wyswietl_wpisy()
        elif opcja == "2":
            dodaj_wpis()
        elif opcja == "3":
            usun_wpis()
        elif opcja == "4":
            break
        else:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")


menu()