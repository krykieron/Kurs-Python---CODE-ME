# 9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
# drukowanymi lub zaczynając od dużej litery)


list1 = ["matematyka", "j. polski", "w-f", "muzyka"]
list2 = ["geografia", "j. ang", "w-f", "biologia"]
list3 = ["matematyka", "j. polski", "w-f", "historia"]
list4 = ["historia", "j. ang.", "w-f", "biologia"]
list5 = ["matematyka", "j. polski", "technika", "plastyka"]

all_subjects = []
for subject_list in [list1, list2, list3, list4, list5]:
    for subject in subject_list:
        all_subjects.append(subject.lower())

repeated_subjects = []
unique_subjects = set()
for subject in all_subjects:
    if subject in unique_subjects:
        repeated_subjects.append(subject)
    else:
        unique_subjects.add(subject)

if repeated_subjects:
    counter = {}
    max_count = 0
    most_popular = None
    for subject in repeated_subjects:
        if subject not in counter:
            counter[subject] = 1
        else:
            counter[subject] += 1
        if counter[subject] > max_count:
            max_count = counter[subject]
            most_popular = subject
    print("Najpopularniejszy przedmiot:", most_popular)
else:
    print("Nie ma powtórzeń przedmiotów.")