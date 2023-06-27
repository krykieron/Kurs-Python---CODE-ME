import random

def dodaj_pomysl(pomysly, prezent, miejsce):
    pomysly.append((prezent, miejsce))

def losowy_prezent(pomysly):
    if not pomysly:
        print("Brak pomysłów na prezenty!")
        return

    wylosowany_indeks = random.randint(0, len(pomysly)-1)
    wylosowany_prezent, wylosowane_miejsce = pomysly[wylosowany_indeks]
    print("Sugerowany prezent: " + wylosowany_prezent)
    print("Miejsce, w którym możesz go zdobyć: " + wylosowane_miejsce)

# Tworzenie listy pomysłów na prezenty
pomysly = []

# Dodawanie pomysłów na prezenty
dodaj_pomysl(pomysly, "Zegarek", "Sklep z zegarkami")
dodaj_pomysl(pomysly, "Książka", "Księgarnia")
dodaj_pomysl(pomysly, "Koszulka", "Sklep odzieżowy")
dodaj_pomysl(pomysly, "Gra planszowa", "Sklep z grami")

# Losowanie prezentu i miejsca jego zdobycia
losowy_prezent(pomysly)
