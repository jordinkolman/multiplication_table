'''
Multiplication Table Creator

Jul 22 11:06 2022

@author: Jordin Kolman
'''

def multiplication_table():
    size = int(input("What size multiplication table would you like? (2-10): "))
    while (size < 2) or (size > 10):
        print("ERROR: Invalid entry - Enter a number between 2 and 10.")
        size = int(input("What size multiplication table would you like? (2-10): "))
    print()
    print()
    # Display Header
    print("         --- Multiplication Table (",size,"x",size,")---")
    print("    ",end="")
    size += 1
    for h in range(1,size):
        if h >= 10:
            print("     ",h, end="")
        else:
            print("     ",h, end="")
    print()
    for h in range(1,76):
        print("-",end="")
    print()

    # Display Multiplication Table
    # Outer loop starts new row

    for a in range(1,size):
        if a < 10:
            print(a," | ", end="")
        else:
            print(a,"|", end="")

    # Inner loop displays each column in the row
        for b in range(1,size):
            result = a * b
            if result % 2 == 0:
                type='#'
            else:
                type=' '
            if result >= 100:
                print(" ", result,type, end="")
            elif result >= 10:
                print("  ", result,type, end="")
            else:
                print("   ", result,type,end="")
        print()

multiplication_table()