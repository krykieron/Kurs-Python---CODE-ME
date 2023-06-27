my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

try:
    index = int(input("Podaj indeks: "))
    value = int(input("Podaj wartość: "))

    if index >= 0 and index < len(my_tuple):
        # Tworzenie nowej krotki z podmienioną wartością
        new_tuple = my_tuple[:index] + (value,) + my_tuple[index+1:]
        print("Krotka po podmianie wartości:", new_tuple)
    else:
        print("Błąd: Podany indeks jest poza zakresem krotki.")

except ValueError:
    print("Błąd: Podana wartość nie jest liczbą.")