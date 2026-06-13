print("----check you monthly salary----")

salary = int(input("Enter the monthy salary amount: "))
absent = int(input("Enter the number of leaves taken: "))
month = int(input("Enter the number of days of the month: "))

deduction = ( salary / month )*absent

deduction = round(deduction,2)
print("The deduction amount: ",deduction)

salary -=deduction

print("you salary for this month: ",salary)
