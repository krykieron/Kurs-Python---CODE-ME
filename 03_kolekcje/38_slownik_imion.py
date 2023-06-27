# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

kraje = {
    'Polska': ['Anna', 'Maria', 'Katarzyna', 'Agnieszka', 'Małgorzata', 'Joanna', 'Monika', 'Barbara', 'Ewa', 'Karolina'],
    'Niemcy': ['Mia', 'Emma', 'Hannah', 'Emilia', 'Lina', 'Sophie', 'Marie', 'Charlotte', 'Amelie', 'Lena'],
    'Francja': ['Emma', 'Louise', 'Jade', 'Alice', 'Lina', 'Chloé', 'Mila', 'Manon', 'Léa', 'Camille'],
    'Włochy': ['Sophia', 'Emma', 'Giulia', 'Aurora', 'Alice', 'Greta', 'Bianca', 'Anna', 'Sofia', 'Marta'],
    'Hiszpania': ['Lucia', 'Sofia', 'Maria', 'Marta', 'Paula', 'Julia', 'Valeria', 'Daniela', 'Carmen', 'Emma'],
    'Wielka Brytania': ['Olivia', 'Amelia', 'Isla', 'Emily', 'Ava', 'Grace', 'Sophia', 'Mia', 'Charlotte', 'Poppy'],
    'Szwecja': ['Elsa', 'Alice', 'Maja', 'Ebba', 'Emilia', 'Olivia', 'Astrid', 'Wilma', 'Alva', 'Nellie'],
    'Holandia': ['Emma', 'Tess', 'Sophie', 'Julia', 'Anna', 'Lisa', 'Mila', 'Sara', 'Zoë', 'Eva'],
    'Norwegia': ['Nora', 'Emma', 'Sofie', 'Ella', 'Olivia', 'Maja', 'Emilie', 'Ida', 'Ingrid', 'Thea'],
    'Grecja': ['Sophia', 'Olivia', 'Maria', 'Eleni', 'Eva', 'Anna', 'Vasiliki', 'Katerina', 'Ioanna', 'Irene']
}

popularne = []
for imie in set(sum(kraje.values(), [])):
    liczba_krajow = sum(imie in kraje for kraje in kraje.values())
    if liczba_krajow >= 3:
        popularne.append(imie)

print("Popularne imiona:", popularne)