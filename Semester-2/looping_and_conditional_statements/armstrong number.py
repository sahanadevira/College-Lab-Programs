num = int(input("Enter a number: "))

temp = num
power = len(str(temp))
total = 0

while temp>0:
    digit = temp%10
    total = total+(digit**power)
    temp = temp//10

if total == num:
    print(f"{num} is an armstrong number")

else:
    print(f"{num} is not an armstrong number")
