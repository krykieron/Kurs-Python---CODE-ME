class Ssaki:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def opis(self):
        print(f"To jest {self.gatunek}, ssak.")

wilk = Ssaki("Wilk")
kon = Ssaki("Koń")
sysaki = Ssaki("Ssaki")

wilk.opis()
kon.opis()
sysaki.opis()