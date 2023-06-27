class Zegar:
    def __init__(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def wyswietl_czas(self):
        return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


class Kalendarz:
    def __init__(self, rok, miesiac, dzien):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien

    def ile_dni_w_miesiacu(self):
        if self.miesiac == 2:
            if self.czy_przestepny():
                return 29
            else:
                return 28
        elif self.miesiac in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def czy_przestepny(self):
        return (self.rok % 4 == 0 and self.rok % 100 != 0) or self.rok % 400 == 0


class ZegaroKalendarz(Zegar, Kalendarz):
    def __init__(self, rok, miesiac, dzien, godzina, minuta, sekunda, strefa_czasowa):
        Zegar.__init__(self, godzina, minuta, sekunda)
        Kalendarz.__init__(self, rok, miesiac, dzien)
        self.strefa_czasowa = strefa_czasowa

    def wyswietl_datetime(self):
        return f"{self.rok}-{self.miesiac:02d}-{self.dzien:02d} {self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d} {self.strefa_czasowa}"

    def wyswietl_widok_tygodniowy(self):
        dni_tygodnia = ["Pn", "Wt", "Śr", "Cz", "Pt", "So", "Nd"]
        dzien_tygodnia = self.oblicz_dzien_tygodnia()
        widok = ""

        for i in range(dzien_tygodnia):
            widok += "   "

        for dzien in range(1, self.ile_dni_w_miesiacu() + 1):
            widok += f"{dzien:2d} "

            if (dzien + dzien_tygodnia) % 7 == 0:
                widok += "\n"

        return widok

    def oblicz_dzien_tygodnia(self):
        dzien = (
                            self.dzien + self.oblicz_numer_miesiaca() + self.oblicz_numer_stulecia() + self.oblicz_numer_wieku()) % 7
        return dzien if dzien != 0 else 7

    def oblicz_numer_miesiaca(self):
        if self.miesiac < 3:
            return self.miesiac + 10
        else:
            return self.miesiac - 2

    def oblicz_numer_stulecia(self):
