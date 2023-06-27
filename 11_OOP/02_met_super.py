class Zwierzę:
    def opis(self):
        return "Jestem zwierzęciem."


class Ssaki:
    def opis(self):
        return "Jestem ssakiem."


class Człowiek(Zwierzę, Ssaki):
    def opis(self):
        return super().opis()


człowiek = Człowiek()
print(człowiek.opis())