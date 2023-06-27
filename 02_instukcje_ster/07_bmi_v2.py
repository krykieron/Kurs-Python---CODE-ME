weight = float(input("Enter your weight [kg]: "))
height = float(input("Enter your height [m]: "))
bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18:
    print('Niedowaga')
elif bmi <= 25:
    print('Waga prawidłowa')
elif bmi <= 30:
    print("Nadwaga")
else:
    print("Otyłość")