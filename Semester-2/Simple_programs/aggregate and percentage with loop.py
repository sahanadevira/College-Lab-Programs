marks = []

for i in range (1,6):
    m = float(input(f"marks for subject {i}: "))
    marks.append(m)

aggregate = sum(marks)
percentage = (aggregate / 500)*100

if percentage >=90:
    grade = "o"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >=60:
    grade = "B+"
elif percentage >=55:
    grade = "B"
elif percentage >=50:
    grade = "C"
else:
    grade = "Fail"

print("Aggregate = ",aggregate)
print("Percentage = ", percentage)
print("Grade = ", grade)
