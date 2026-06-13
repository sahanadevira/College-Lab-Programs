print("----bank balance updation----")

balance = float(input("Enter the balance amount: "))
transaction = input("Enter the transaction type(deposit/withdraw): ")
amount = float(input("Enter the amount: "))

if transaction == "deposit":
    balance += amount
elif transaction == "withdraw":
    if amount > balance:
        print("Insufficient balance amount")
    else:
        balance -= amount
print("updated balance: ",balance)
