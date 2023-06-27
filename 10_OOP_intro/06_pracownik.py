class Pracownik:
    def __init__(self, stanowisko, wynagrodzenie, imie, nazwisko, staz_pracy, student=False):
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie
        self.imie = imie
        self.nazwisko = nazwisko
        self.staz_pracy = staz_pracy
        self.student = student

    def roczna_podwyzka(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * procent / 100

    def oblicz_podatek(self):
        if self.wynagrodzenie > 5000:
            return self.wynagrodzenie * 0.2
        else:
            return self.wynagrodzenie * 0.15

    def oblicz_skladke_zdrowotna(self):
        if self.student:
            return 0
        else:
            return self.wynagrodzenie * 0.05

    def generuj_email(self, nazwa_firmy):
        email = ""
        for char in self.imie + self.nazwisko + nazwa_firmy + ".com":
            if char.lower() not in "aeiou":
                email += char.lower()
        return email

pracownik = Pracownik("Monter", 3456, "Adam", "Kowalski", 2)
pracownik.roczna_podwyzka(5)


print("Stanowisko:", pracownik.stanowisko)
print("Wynagrodzenie:", pracownik.wynagrodzenie)
print("Imię:", pracownik.imie)
print("Nazwisko:", pracownik.nazwisko)
print("Staż pracy:", pracownik.staz_pracy)


podatek = pracownik.oblicz_podatek()
skladka_zdrowotna = pracownik.oblicz_skladke_zdrowotna()

print("Podatek:", podatek)
print("Skladka zdrowotna:", skladka_zdrowotna)

nazwa_firmy = "Love Python Company"
email = pracownik.generuj_email(nazwa_firmy)
print("Email:", email)
