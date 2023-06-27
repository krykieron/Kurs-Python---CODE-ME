def create_coffee_list():
    coffee_list = {
        "GH": {
            "nazwa": "Guatemala Huehuetenango",
            "waga_worka": 69,
            "odmiana": "arabica",
            "punktacja_sca": 83.75,
            "zadana_temperatura": 190,
            "strata_wagi": 0.19
        },
        "BS": {
            "nazwa": "Brazil Santos",
            "waga_worka": 60,
            "odmiana": "arabica",
            "punktacja_sca": 81.13,
            "zadana_temperatura": 197,
            "strata_wagi": 0.17
        },
        "BYB": {
            "nazwa": "Brazil Yellow Bourbon",
            "waga_worka": 59,
            "odmiana": "arabica",
            "punktacja_sca": 85,
            "zadana_temperatura": 193,
            "strata_wagi": 0.19
        },
        "CE": {
            "nazwa": "Colombia Excelso",
            "waga_worka": 70,
            "odmiana": "arabica",
            "punktacja_sca": 82.14,
            "zadana_temperatura": 191,
            "strata_wagi": 0.21
        },
        "PC": {
            "nazwa": "Peru Chanchamayo",
            "waga_worka": 69,
            "odmiana": "arabica",
            "punktacja_sca": 82.16,
            "zadana_temperatura": 191,
            "strata_wagi": 0.18
        },
        "ED": {
            "nazwa": "Ethiopia Djimmah",
            "waga_worka": 65,
            "odmiana": "arabica",
            "punktacja_sca": 77.68,
            "zadana_temperatura": 187,
            "strata_wagi": 0.15
        }
    }

    return coffee_list

def symulator_pieca():
    coffee_list = create_coffee_list()

    print("Dostępne w magazynie kawy:")
    for symbol, coffee in coffee_list.items():
        print(f"- {symbol}: {coffee['nazwa']}")
    chosen_coffee = input("Wybierz kawę (podaj symbol): ")

    coffee = coffee_list.get(chosen_coffee)
    if coffee:
        roaster = input("Wybierz piec (Coffeed - C, Toper - T): ")
        if roaster == "C":
            zasyp = 25
        elif roaster == "T":
            zasyp = 10
        else:
            print("Nieprawidłowy wybór pieca.")
            return

        waga_worka = coffee["waga_worka"]
        strata_wagi = coffee["strata_wagi"]
        waga_po_wypale = zasyp - (zasyp * strata_wagi)
        zostalo_kawy_na = waga_worka // zasyp

        print()
        print("Rozpoczynamy proces palenia kawy...")
        print(f"Wybrana kawa: {coffee['nazwa']} ({coffee['punktacja_sca']} pkt w SCA)")
        print(f"Zasypano: {zasyp} kg zielonych ziaren, podczas palenia odparowało {zasyp * strata_wagi} kg wody")
        print(f"Waga po wypale: {waga_po_wypale} kg")
        print(f"Pozostało kawy na {zostalo_kawy_na - 1} pełny(e) wypał(y) kawy w tym samym piecu")


    else:
        print("Nie znaleziono kawy o podanym symbolu.")


symulator_pieca()