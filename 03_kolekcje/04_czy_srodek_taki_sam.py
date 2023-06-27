Pobierz od użytkownika parzystą listę elementów.Sprawdź czy 2 środkowe elementy są takie same.

elements = input("Podaj parzystą listę elementów, oddzielając je spacją: ")
elements_list = elements.split()

if len(elements_list) % 2 == 0:
    middle_index = len(elements_list) // 2
    if elements_list[middle_index - 1] == elements_list[middle_index]:
        print("Dwa środkowe elementy są takie same.")
    else:
        print("Środkowe elementy są różne.")
else:
    print("Błędnie wprowadzone dane.")