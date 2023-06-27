def odczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r") as plik:
            zawartosc = plik.read()
            print(zawartosc)

    except FileNotFoundError:
        print(f"Plik '{nazwa_pliku}' nie istnieje.")

    except IOError as e:
        print(f"Wystąpił błąd wejścia/wyjścia: {e}")

    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


def utworz_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "x") as plik:
            print(f"Plik '{nazwa_pliku}' został utworzony.")

    except FileExistsError:
        print(f"Plik '{nazwa_pliku}' już istnieje.")

    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


# Przykład 1: Odczyt pliku, który nie istnieje
odczytaj_plik("nieistniejacy_plik.txt")

# Przykład 2: Odczyt pliku otwartego w trybie "w"
odczytaj_plik("plik.txt")

# Przykład 3: Tworzenie pliku, który już istnieje
utworz_plik("plik.txt")
