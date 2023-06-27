# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”,
# "nie, liczba x jest z poza zakresu”.

def sprawdz_zakres(liczba, zakres_poczatek, zakres_koniec):
    if liczba >= zakres_poczatek and liczba <= zakres_koniec:
        return f"tak, liczba {liczba} znajduje się w zadanym zakresie"
    else:
        return f"nie, liczba {liczba} jest z poza zakresu"

liczba = 10
zakres_poczatek = 5
zakres_koniec = 15

wynik = sprawdz_zakres(liczba, zakres_poczatek, zakres_koniec)
print(wynik)