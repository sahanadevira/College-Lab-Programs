def full_subtractor(a, b, bin):
    diff = a ^ b ^ bin
    borrow = ((not a) and b) or ((not (a ^ b)) and bin)
    return diff, int(borrow)

print("A B Bin Diff Borrow")

for a in range(2):
    for b in range(2):
        for bin in range(2):
            d, br = full_subtractor(a, b, bin)
            print(a, b, bin, d, br)
