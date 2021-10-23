from typing import Final

K1 = 4
K2 = -0.2
T1: Final = 0.1
T2: Final = 0.01
T3: Final = 0.01
DELTA: Final = 1 
w = []
v = []

"""Data input area"""
while(True):
    print("Enter the number of iterations(more than 100)")
    iterations_count = input()

    if not iterations_count.isdecimal():
        print("Incorrect input.")
        continue

    if int(iterations_count) < 100:
        print("Need more than 100")
        continue
    else:
        break

while(True):
    print("Use the standard values K1 and K2?(Y/N)")
    inputValue = input()
    if inputValue == 'Y':
        print("Enter K1:")
        K1 = int(input())
        print("Enter K2:")
        K2 = int(input())
        break
    elif inputValue == 'N':
        print("The standard values K1=4 and K2=-0.2 are used")
        break
    else:
        print("Incorrect input.")
        continue
"""End of data input area"""