print("SIMPLE INTEREST AND COMPOUND INTEREST")

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the Time period(in years): "))

SI = (p*t*r)/100
amount = p*((1+(r/100))**t)
CI = amount - p

print("Simple Interest : ",SI)
print("Compound Interest : ",CI)
