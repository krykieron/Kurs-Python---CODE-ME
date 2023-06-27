def gra_kamien_papier_nozyce():
    print("Witaj w grze Kamień - Papier - Nożyce!")

    def sprawdz_wybor(uzytkownik, komputer):
        if uzytkownik == komputer:
            return "Remis"
        elif (uzytkownik == "kamień" and komputer == "nożyce") or (uzytkownik == "papier" and komputer == "kamień") or (uzytkownik == "nożyce" and komputer == "papier"):
            return "Wygrałeś!"
        else:
            return "Przegrałeś!"

    while True:
        wybor_uzytkownika = input("Wybierz kamień, papier lub nożyce (q aby zakończyć): ").lower()

        if wybor_uzytkownika == "q":
            print("Dziękujemy za grę!")
            break

        if wybor_uzytkownika not in ["kamień", "papier", "nożyce"]:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            continue

        wybor_komputera = random.choice(["kamień", "papier", "nożyce"])

        wynik = sprawdz_wybor(wybor_uzytkownika, wybor_komputera)

        print(f"Twój wybór: {wybor_uzytkownika}")
        print(f"Wybór komputera: {wybor_komputera}")
        print(f"Wynik: {wynik}")
        print()

gra_kamien_papier_nozyce()
