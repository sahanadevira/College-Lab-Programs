mark1 = int(input("Enter Python mark: "))


mark2 = int(input("Enter English mark: "))


mark3 = int(input("Enter Chemistry mark: "))


mark4 = int(input("Enter Mathematics mark: "))


mark5 = int(input("Enter Physics mark: "))

aggregate = mark1+mark2+ mark3+ mark4+ mark5
percentage = (aggregate//500)*100

print(aggregate)
print(percentage)
if (percentage >=90):
    print("O grade")
elif (percentage >=80):
    print("A++ grade")
elif (percentage >=70):
    print("A grade")
elif (percentage >=60):
    print("B+ grade")
elif (percentage >=55):
    print("B grade")
elif (percentage >=50):
    print("c grade")

