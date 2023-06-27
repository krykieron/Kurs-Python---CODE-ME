class Kraj:
    def __init__(self, powierzchnia, ludnosc, jezyk_urzedowy, stolica):
        self.powierzchnia = powierzchnia
        self.ludnosc = ludnosc
        self.jezyk_urzedowy = jezyk_urzedowy
        self.stolica = stolica

polska = Kraj(312696, 38386000, "polski", "Warszawa")
francja = Kraj(551695, 67064000, "francuski", "Paryż")
niemcy = Kraj(357582, 83149300, "niemiecki", "Berlin")

kraje = [polska, francja, niemcy]

for kraj in kraje:
    print("Powierzchnia:", kraj.powierzchnia)
    print("Ludność:", kraj.ludnosc)
    print("Język urzędowy:", kraj.jezyk_urzedowy)
    print("Stolica:", kraj.stolica)
    print()