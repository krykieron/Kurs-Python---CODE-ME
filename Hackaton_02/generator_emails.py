import csv

def read_student_data_from_csv(filename):
    student_data = {}

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                class_name, first_name, last_name, missing_tasks, grade = row
                key = f"{class_name}_{first_name}_{last_name}"
                student_data[key] = [first_name, last_name, int(missing_tasks), int(grade)]

    except FileNotFoundError:
        print(f"Plik '{filename}' nie został znaleziony.")

    return student_data


def read_message_from_file(filename):
    try:
        with open(filename, "r") as file:
            message = file.read()
    except FileNotFoundError:
        print(f"Plik '{filename}' nie został znaleziony.")
        return ""

    return message


def main():
    names = input("Podaj imiona i nazwiska uczniów (oddzielone przecinkami): ").split(",")
    missing_tasks = input("Podaj liczbę brakujących zadań dla każdego ucznia (oddzielone przecinkami): ").split(",")
    grades = input("Podaj aktualne oceny dla każdego ucznia (oddzielone przecinkami): ").split(",")


    student_data = read_student_data_from_csv("students.csv")

    message = read_message_from_file("message.txt")

    zaliczenie_date = "20 maja 2023"


    for i in range(len(names)):
        first_name = names[i].strip()
        last_name = names[i].strip()
        missing = int(missing_tasks[i].strip())
        grade = int(grades[i].strip())


        proposed_grade = grade + 1 if missing == 0 else 0


        personalized_message = message.format(
            first_name=first_name,
            last_name=last_name,
            missing_tasks=missing,
            grade=proposed_grade,
            zaliczenie_date=zaliczenie_date
        )


        print(personalized_message)


if __name__ == '__main__':
    main()