print("--- Logic gate verification with  binary input---")

def AND():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        b = int(input("Enter input_2: "))
        print(a&b)


def OR():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        b = int(input("Enter input_2: "))
        print(a|b)

def NOT():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        print(1 - a)        

def NAND():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        b = int(input("Enter input_2: "))
        print(1 - (a&b))
        
def NOR():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        b = int(input("Enter input_2: "))
        print (1 - (a|b))

def XOR():
    n = int(input("Enter number of test cases to check: "))
    for i in range(n):
        a = int(input("Enter input_1: "))
        b = int(input("Enter input_2: "))
        print (a^b)        

        
        

while True:
    print("---select gate type to check---")
    print("1.AND gate\n2.OR gate\n3.NOT gate\n4.NAND gate\n5.NOR gate\n6.X-OR gate\n7.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        AND()
    elif choice == 2:
        OR()
    elif choice == 3:
        NOT()
    elif choice == 4:
        NAND()
    elif choice == 5:
        NOR()
    elif choice == 6:
        XOR()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("invalid choice")
        
        
    
