numbers = []
print("Give me 5 integers")
for _ in range(5):
    num = int(input("Give me a number ->"))
    numbers.append(num)

print(f"First and last item are the same? -> { numbers[0] == numbers[-1]}")