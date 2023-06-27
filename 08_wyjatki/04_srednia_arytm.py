def oblicz_srednia():
    try:
        liczby = input("Podaj liczby oddzielone przecinkami: ")
        liczby = liczby.split(",")
        liczby = [float(x) for x in liczby]

        suma = sum(liczby)
        srednia = suma / len(liczby)

        return srednia

    except ValueError as e:
        with open("bledy.txt", "a") as file:
            file.write(f"Błąd wartości: {e}\n")
        return None

    except Exception as e:
        with open("bledy.txt", "a") as file:
            file.write(f"Inny błąd: {e}\n")
        return None


srednia = oblicz_srednia()

if srednia is not None:
    print("Średnia:", srednia)