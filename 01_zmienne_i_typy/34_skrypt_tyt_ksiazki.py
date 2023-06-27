title = input("Podaj tytuł książki: ")
author = input("Podaj nazwisko autora: ")
pages = input("Podaj liczbę stron: ")

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print(title.isalpha())
print(author.isalpha())
print(pages.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print(title.title())
print(author.title())
# Połącz dane w jeden ciąg book za pomocą spacji
book = title + " " + author + " " + pages
print(book)
print(len(book))