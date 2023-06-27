def sprawdz_zabytek(samochod):
    marka = samochod['marka']
    rocznik = samochod['rocznik']

    print("Informacje o samochodzie:")
    print(samochod)

    aktualny_rok = 2023

    wiek = aktualny_rok - rocznik

    if wiek >= 25:
        print(f"Gratulacje! Twój samochód {marka} może być zarejestrowany jako zabytek.")
    else:
        print(f"Twój samochód {marka} jest jeszcze zbyt młody.")


samochod = {
    'marka': 'Fiat',
    'model': '126p',
    'rocznik': 1980
}

sprawdz_zabytek(samochod)
