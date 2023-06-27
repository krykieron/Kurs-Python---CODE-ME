class Orchid:
    królestwo_roślin = "Rośliny"

    def __init__(self, kolor, pora_kwitnienia, gatunek):
        self.kolor = kolor
        self.pora_kwitnienia = pora_kwitnienia
        self.gatunek = gatunek

    def opis(self):
        print("Storczyk:")
        print(f"Kolor: {self.kolor}")
        print(f"Pora kwitnienia: {self.pora_kwitnienia}")
        print(f"Gatunek: {self.gatunek}")
        print(f"Królestwo roślin: {Orchid.królestwo_roślin}")
        print()

# Tworzenie instancji storczyków
storczyk1 = Orchid("Biały", "Lato", "Białus_pospolitus")
storczyk2 = Orchid("Różowy", "Wiosna", "Różowywewawy")
storczyk3 = Orchid("Żółty", "Jesień", "Żółto płatkowy stepowy")

storczyk1.opis()
storczyk2.opis()
storczyk3.opis()