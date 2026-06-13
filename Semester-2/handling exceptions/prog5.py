try:
    # Try converting input to a number
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    # Runs if the user types a string instead of a number
    print("That's not a valid number!")
except ZeroDivisionError:
    # Runs if the user types 0
    print("You cannot divide by zero!")
else:
    # Runs if both lines in 'try' succeeded
    print(f"Success! The result is {result}")
finally:
    # Runs no matter what
    print("Operation complete.")

