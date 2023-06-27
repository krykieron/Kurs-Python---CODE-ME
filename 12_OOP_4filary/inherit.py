class Wolf:
    paws = 4
    carnivore = True

    def __init__(self):
        print('Created Wolf!')

    def description(self):
        return "The wolf is the largest extant member of the family Canidae. " \
               "It is also distinguished from other Canis species by its less pointed ears and muzzle"

    def get_location(self):
        return '-> Europe 🌎'


class Dog(Wolf):
    kingdom = 'animals'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Dog - {self.name} is {self.age} years old"

    def bark(self):
        print('hau' * self.age)

    def description(self):
        desc = super().description()
        desc += '\n' + super().get_location()
        desc += "\n 🐕 The dog is a domesticated descendant of the wolf."
        return desc



figa = Dog("Figa", 3, "mix terrier")
print(figa)
figa.bark()
print(figa.description())

# w = Wolf()
# print(w.description())