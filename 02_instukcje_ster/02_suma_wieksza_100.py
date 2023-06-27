# Pobierz  dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))

suma = liczba1 + liczba2

if suma > 100:
    print("Suma liczb wynosi:", suma)
else:
    print("Koniec")