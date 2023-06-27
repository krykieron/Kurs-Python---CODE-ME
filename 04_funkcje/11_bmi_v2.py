# Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na
# funkcję obliczającą bmi na podstawie danych użytkownika

# oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.

# --- calculate_bmi...
def calculate():
    weight = float(input("Enter your weight [kg]: "))
    height = float(input("Enter your height [m]: "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    return bmi


def get_bmi_state(bmi_value):
    if bmi_value < 18:
        return 'Niedowaga'
    elif bmi_value <= 25:
        return 'Waga prawidłowa'
    elif bmi_value <= 30:
        return "Nadwaga"
    else:
        return "Otyłość"


# -- main --
result_bmi = calculate()
print(get_bmi_state(result_bmi))