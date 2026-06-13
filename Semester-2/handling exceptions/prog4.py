try:

    number = int(input("Enter a number: "))

    print(f"Success! Your number is: {number}")

except ValueError as e:

    print(f"Error Message: {e}")
    print("That is not a valid number. Please enter digits only.")

