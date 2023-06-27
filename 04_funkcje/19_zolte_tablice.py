# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
# ponownie wyświetl zmieniony słownik
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności.
# Dopisz odpowiednie komunikaty.

def sprawdz_zabytek(samochod):
    marka = samochod['marka']
    rocznik = samochod['rocznik']
    oryginalny = samochod['czy_oryginalny']

    print("Informacje o samochodzie:")
    print(samochod)

    aktualny_rok = 2023  # Zakładamy aktualny rok jako 2023

    wiek = aktualny_rok - rocznik

    if wiek >= 25 and oryginalny:
        print(f"Gratulacje! Twój samochód {marka} może być zarejestrowany jako zabytek.")
    elif wiek < 25:
        print(f"Twój samochód {marka} jest jeszcze zbyt młody.")
    else:
        print(f"Twój samochód {marka} nie spełnia warunku oryginalności.")


# Tworzenie słownika samochodu
samochod = {
    'marka': 'Fiat',
    'model': '126p',
    'rocznik': 1980,
    'czy_oryginalny': True
}

# Dopisanie klucza czy_oryginalny
samochod['czy_oryginalny'] = True

# Wywołanie funkcji sprawdz_zabytek
sprawdz_zabytek(samochod)
