class Dog:
    kingdom = 'animals'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Dog - {self.name} is {self.age} years old"

    def bark(self):
        print('hau' * self.age)


figa = Dog("Figa", 3, "mix terrier")
print(figa)
figa.bark()

