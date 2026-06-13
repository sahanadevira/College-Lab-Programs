n = int(input("Enter a number: "))

print(f"Except_{n} ")

for i in range(1,11):
    if i == n:
        continue
    print(i)
